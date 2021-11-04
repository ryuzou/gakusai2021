//
// Created by ryuzo on 2021/11/03.
//

#include "globalEncodedImageContent.h"



globalEncodedImageContent::globalEncodedImageContent() {
    content_array.reserve(1024 * 8);
}

void globalEncodedImageContent::updateContent(std::string content, int index) {
    mutex.lock();
    content_array[index] = content;
    //std::cout << content_array[index] << "\n" << index << std::endl;
    mutex.unlock();
    //std::cout << index << std::endl;
}

std::string globalEncodedImageContent::getContent(int index) {
    std::string content("0");
    mutex.lock();
    content = content_array[index];
    mutex.unlock();
    return content;
}

int globalEncodedImageContent::convertFrame(cv::Mat frame) {
    int x_cod = 0;
    int y_cod = 0;
    for (int y = 0; y < height_divide; ++y) {
        for (int x = 0; x < width_divide; ++x) {
            //clock_t start = clock();
            x_cod = x * x_len;
            y_cod = y * y_len;
            std::vector<uchar> buff;
            //std::cout << x_cod << "   " << y_cod << std::endl;
            cv::Mat divided_image(frame, cv::Rect(x_cod, y_cod, x_len, y_len));
            cv::imencode(".jpg", divided_image, buff, std::vector<int>());
            std::string encoded_content_part = base64_encode(buff.data(), buff.size());   // base64 encode, mainly for debug, delete this for speed up. //todo
            std::string content_part = std::to_string(x * x_len) + "_" + std::to_string(y * y_len) + "_" + std::to_string(x_len) + "_" +
                                       std::to_string(y_len) + "_" + std::to_string(clock()) + "&" + encoded_content_part;
            updateContent(content_part, cod2index(x, y));
            clock_t end = clock();
            //std::cout << (double)(end - start) / CLOCKS_PER_SEC << std::endl;
            //std::cout << end << std::endl;
        }
    }
    clock_t end = clock();
    //std::cout << (double)(end - start) / CLOCKS_PER_SEC << std::endl;
    return 0;
}

int globalEncodedImageContent::cod2index(int x, int y) {
    return y * height_divide + x;
}

std::string globalEncodedImageContent::getNextContent() {
    std::string content = getContent(index_now);
    index_now++;
    if (index_now > max_index){
        index_now = 0;
    }
    return content;
}

