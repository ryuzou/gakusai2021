#include <sys/socket.h>
#include <sys/time.h>
#include <arpa/inet.h>
#include <unistd.h>
#include <mqueue.h>
#include <cstdint>
#include <iostream>
#include <mutex>
#include <thread>
#include <opencv2/opencv.hpp>
#include <atomic>
#include "raspicam/src/raspicam_cv.h"

#include "udpTx.h"
#include "tcpTxRx.h"
#include "errorhandling.h"

std::atomic<bool> stop_tx_thread_flag(false);
std::atomic<bool> stop_rx_thread_flag(false);

class _globalEncodedImageContent {
private:
    std::string _content;
    std::mutex _mutex;

public:
    void updateContent(const std::string& content){
        _mutex.lock();
        _content = content;
        _mutex.unlock();
    }
    std::string getContent(){
        std::string content;
        _mutex.lock();
        content = _content;
        _mutex.unlock();
        return content;
    }
};

void
RxCommunicatorThread(std::string defualtMovementCode) {    // Thread for Receiving data from client. TCP connection.
    int i;
    char *buff;
    mqd_t mqd;
    const int flags = O_WRONLY | O_CREAT;
    mode_t mode = 0777;
    const char *mq_name = "/gakusai2021.1"; // Name of message queue.
    char *sendedMovementCode = const_cast<char *>(defualtMovementCode.c_str());
    bool tcp_succeed_flag(false);
    mqd = mq_open(mq_name, flags, mode);
    if (mqd == -1) {
        error_exit("Message queue open failed at RxCommunicatorThread, Exiting.");
    }
    while (!stop_rx_thread_flag) {
        // Getting movement data from client via tcp.
        // Sending the data to python process with message queue.
        buff = (char *) calloc(strlen(sendedMovementCode) + 1, sizeof(char));
        strcpy(buff, sendedMovementCode);
        if (!tcp_succeed_flag) {
            if (mq_send(mqd, buff, strlen(buff), 0) == -1) {
                error_exit("Message Queue send faild at RxCommunicatorThread, Exiting.");
            }

        }
    }
    if (mq_close(mqd) == -1)
        error_exit("Message queue close failed at RxCommunicatorThread, Exiting anyway.");
}

void TxCommunicatorThread(_globalEncodedImageContent *globalEncodedImageContent) {    // Thread for Transferring data. Mainly transferring webcam image. UDP connection.
    std::string encodedImageContent;
    udpTx udp(50041);
    while (!stop_tx_thread_flag) {
        encodedImageContent = globalEncodedImageContent->getContent();
        if (!(encodedImageContent.empty())) {  // Check if there is a worthwhile content.
            udp.send(encodedImageContent);  // Send encoded image via udp.
        }
    }
}

int main(int argc, char *argv[]) {
    // Some initial stuff for opencv.
    raspicam::RaspiCam_Cv Camera;
    cv::Mat frame;
    std::vector<uchar> buff;

    //setup
    Camera.set( cv::CAP_PROP_FORMAT, CV_8UC1 );

    std::string stringDefualtMovementCode(R"({"joystick": {"r": 0, "sita": 0}, "shoot": 0, "LR": 0})");

    tcpTxRx tcp(80800);
    tcp.receive_setup();
    std::cout << "connected from" << tcp.connect();

    //Initializing threads;
    _globalEncodedImageContent globalEncodedImageContent;

    std::thread Rx(RxCommunicatorThread, stringDefualtMovementCode);
    std::thread Tx(TxCommunicatorThread, &globalEncodedImageContent);
    // Setting up camera streaming via opencv.
    if (!Camera.open()) {std::cerr<<"Error opening the camera"<<std::endl;return -1;}

    double vidWidth = Camera.get(cv::CAP_PROP_FRAME_WIDTH);
    double vidHeight = Camera.get(cv::CAP_PROP_FRAME_HEIGHT);
    std::cout << "Video Width is " << vidWidth << std::endl;
    std::cout << "Video Height is " << vidHeight << std::endl;
    Camera.grab();
    Camera.retrieve(frame);
    std::vector<int> v;
    while (!frame.empty()) {
        clock_t start = clock();
        // Encoding camera stream with webp.
        cv::imencode(".jpg", frame, buff, std::vector<int>()); // Didn't need libwebp?
        std::string encoded_content(buff.begin(), buff.end());
        globalEncodedImageContent.updateContent(encoded_content);
        Camera.grab();
        Camera.retrieve(frame);
        clock_t end = clock();
        std::cout << "duration = " << (double)(end - start) / CLOCKS_PER_SEC << "sec.\n";
    }
    Camera.release();
    return 0;
}