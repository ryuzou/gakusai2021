//
// Created by ryuzo on 2021/11/03.
//

#include "globalEncodedImageContent.h"

#include <utility>


globalEncodedImageContent::globalEncodedImageContent() {
    content_array.reserve(1200);
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
    //clock_t start = clock();
    for (int x = 0; x < x_len; ++x) {
        for (int y = 0; y < y_len; ++y) {
            std::vector<uchar> buff;
            cv::Mat divided_image(frame, cv::Rect(x, y, x_len, y_len));
            cv::imencode(".jpg", divided_image, buff, std::vector<int>());
            auto *enc_msg = reinterpret_cast<unsigned char*>(buff.data());  // base64 encode, mainly for debug, delete this for speed up. //todo
            std::string encoded_content_part = base64_encode(enc_msg, buff.size());
            std::string content_part = std::to_string(x) + "_" + std::to_string(y) + "_" + std::to_string(x_len) + "_" +
                                       std::to_string(y_len) + "&" + encoded_content_part;
            updateContent(content_part, cod2index(x, y));
        }
    }
    //clock_t end = clock();
    //std::cout << (double)(end - start) / CLOCKS_PER_SEC << std::endl;
    return 0;
}

int globalEncodedImageContent::cod2index(int x, int y) {
    return y * x_len + x;
}

std::string globalEncodedImageContent::getNextContent() {
    std::string content = getContent(index_now);
    std::cout << content << "\n" << index_now <<std::endl;
    index_now++;
    if (index_now > max_index){
        index_now = 0;
    }
    return content;
}

