//
// Created by ryuzo on 2021/11/03.
//

#include "globalEncodedImageContent.h"

#include <utility>


globalEncodedImageContent::globalEncodedImageContent() {
    content_array.reserve(1024 * 8);
}

void globalEncodedImageContent::updateContent(std::string content, int index) {
    mutex.lock();
    content_array[index] = content.c_str();
    mutex.unlock();
}

std::string globalEncodedImageContent::getContent(int index) {
    std::string content;
    mutex.lock();
    content = content_array[index];
    mutex.unlock();
    return content;
}

int globalEncodedImageContent::convertFrame(cv::Mat frame) {
    //clock_t start = clock();
    std::vector<uchar> buff;
    for (int x = 0; x < x_len; ++x) {
        for (int y = 0; y < y_len; ++y) {
            cv::Mat divided_image(frame, cv::Rect(x, y, x_len, y_len));
            cv::imencode(".jpg", divided_image, buff, std::vector<int>());
            std::string encoded_content_part(buff.begin(), buff.end());
            std::string content_part = std::to_string(x) + "_" + std::to_string(y) + "_" + std::to_string(x_len) + "_" +
                                       std::to_string(y_len) + "_" + encoded_content_part;
            updateContent(content_part, cod2index(x, y));
        }
    }
    //clock_t end = clock();
    //std::cout << (double)(end - start) / CLOCKS_PER_SEC << std::endl;
    return 0;
}

int globalEncodedImageContent::cod2index(int x, int y) {
    return y * (x_len - 1) + x;
}

std::string globalEncodedImageContent::getNextContent() {
    std::string content = getContent(index_now);
    if (index_now >= max_index){
        index_now = 0;
    }
    return content;
}

