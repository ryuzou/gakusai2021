#include <sys/socket.h> //socket(), bind(), sendto(), recvfrom()
#include <arpa/inet.h> // struct sockaddr_in, struct sockaddr, inet_ntoa(), inet_aton()
#include <unistd.h> //close()
#include <mqueue.h>
#include <cstdint>
#include <iostream>
#include <mutex>
#include <thread>
#include <opencv2/opencv.hpp>
#include <atomic>

#include "udpTx.h"

pthread_mutex_t mutex = PTHREAD_MUTEX_INITIALIZER;

std::string globalEncodedImageContent;
std::atomic<bool> stop_tx_thread_flag(false);
std::atomic<bool> stop_rx_thread_flag(false);

void RxCommunicatorThread() {    // Thread for Receiving data from client. TCP connection.
    mqd_t mqd;
    const int flags = O_WRONLY | O_CREAT;
    const char *mq_name = "/tmp/gakusai2021.1"; // Name of message queue.
    mqd = mq_open(mq_name, flags);
    if (mqd == -1){

    }
    while (!stop_rx_thread_flag) {
        // Getting movement data from client via tcp.
        // Sending the data to python process with message queue.

    }
    mq_close(mqd);
}

void TxCommunicatorThread() {    // Thread for Transferring data. Mainly transferring webcam image. UDP connection.
    std::string encodedImageContent;
    udpTx udp("192.168.0.1", 50041);
    while (!stop_tx_thread_flag) {
        pthread_mutex_lock(&mutex);
        // Getting encoded image content from main process, critical behavior.
        encodedImageContent = globalEncodedImageContent;
        // Ending critical process.
        pthread_mutex_unlock(&mutex);
        if (!(encodedImageContent.empty())) {  // Check if there is a worthwhile content.
            udp.send(encodedImageContent);  // Send encoded image via udp.
        }
    }
}

int main(int argc, char *argv[]) {
    // Some initial stuff for opencv.
    cv::VideoCapture cap;
    cv::Mat frame;
    std::vector<uchar> buff;

    //Initializing threads;
    std::thread Rx(RxCommunicatorThread);
    std::thread Tx(TxCommunicatorThread);

    // Setting up camera streaming via opencv.
    cap.open(0);
    if (!cap.isOpened()) {
        printf("Could not open stream");
        return -1;
    }
    double vidWidth = cap.get(cv::CAP_PROP_FRAME_WIDTH);
    double vidHeight = cap.get(cv::CAP_PROP_FRAME_HEIGHT);
    std::cout << "Video Width is " << vidWidth << std::endl;
    std::cout << "Video Height is " << vidHeight << std::endl;
    cap >> frame;
    while (!frame.empty()) {
        // Encoding camera stream with webp.
        cv::imencode(".jpg", frame, buff, std::vector<int>()); // Didn't need libwebp?
        std::string encoded_content(buff.begin(), buff.end());
        pthread_mutex_lock(&mutex);
        // Passing encoded image content to thread, critical behavior.
        globalEncodedImageContent = encoded_content;
        // Finished passing data. Finished critical behavior.
        pthread_mutex_unlock(&mutex);
        cap >> frame;
    }
    cap.release();
}