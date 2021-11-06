//
// Created by ryuzo on 2021/11/03.
//

#ifndef SERVER_GLOBALENCODEDIMAGECONTENT_H
#define SERVER_GLOBALENCODEDIMAGECONTENT_H

#include <sys/socket.h>
#include <arpa/inet.h>
#include <unistd.h>
#include <mqueue.h>
#include <cstdint>
#include <iostream>
#include <utility>
#include <chrono>
#include <mutex>
#include <thread>
#include <opencv2/opencv.hpp>
#include <atomic>
#include "raspicam/src/raspicam_cv.h"

#include "udp.h"
#include "tcp.h"
#include "errorhandling.h"
#include "base64.h"

class globalEncodedImageContent {
private:
    static const int height = 480;
    static const int width = 640;
    static const int height_divide = 6;
    static const int width_divide = 6;
    static const int x_len = width / width_divide;
    static const int y_len = height / height_divide;
    static const int max_index = width_divide * height_divide - 1;    // counting by 0 start

    std::string _content;
    std::mutex _mutex;
    //std::vector<std::mutex> mutex_array;
    std::vector<std::string> content_array;
    std::mutex mutex;

    int index_now = 0;

public:
    int public_height = height;
    int public_width = width;
    globalEncodedImageContent();
    int convertFrame(cv::Mat frame);
    void updateContent(std::string content, int index);
    int cod2index(int x, int y);
    std::string getContent(int index);
    std::string getNextContent();
};


#endif //SERVER_GLOBALENCODEDIMAGECONTENT_H
