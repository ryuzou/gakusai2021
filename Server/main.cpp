#include <sys/socket.h>
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

#include "udp.h"
#include "tcp.h"
#include "errorhandling.h"
#include "globalEncodedImageContent.h"

std::atomic<bool> stop_tx_thread_flag(false);
std::atomic<bool> stop_rx_thread_flag(false);
std::atomic<bool> recieve_addr_set_flag(false);

std::string recieve_addr;

class tcpImageContent {
private:
    std::string _content;
    std::mutex _mutex;

public:
    void convertContent(cv::Mat frame){
        std::vector<uchar> buff;
        cv::imencode(".jpg", frame, buff, std::vector<int>());
        std::string encoded_content_part(buff.begin(), buff.end());
        updateContent(encoded_content_part);
    }
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
RxCommunicatorThread(std::string movementCode) {    // Thread for Receiving data from destination_addr. TCP connection.
    logger log(LOGLEVEL_DEBUG);
    int i;
    char *buff;
    mqd_t mqd;
    const int flags = O_WRONLY | O_CREAT;
    mode_t mode = 0777;
    const char *mq_name = "/gakusai2021.1";// Name of message queue.
    char *sendedMovementCode = const_cast<char *>(movementCode.c_str());
    mqd = mq_open(mq_name, flags, mode, NULL);
    if (mqd == -1) {
        log.error("Message queue open failed at RxCommunicatorThread, Exiting.");
    }

    //tcp connection setup.
    const char *connected_adder;
    char *recieve_data;
    tcp tcp(8000);
    tcp.receive_setup();
    connected_adder = tcp.connect();
    std::cout << "Connected from " << connected_adder << std::endl;

    recieve_addr = connected_adder;
    recieve_addr_set_flag = true;

    // initial connection
    recieve_data = tcp.recieve();


    while (!stop_rx_thread_flag) {
        // Getting movement data from destination_addr via tcp.
        recieve_data = tcp.recieve();
        log.debug(recieve_data);

        // Sending the data to python process with message queue.
        buff = (char *) calloc(strlen(sendedMovementCode) + 1, sizeof(char));
        strcpy(buff, sendedMovementCode);
        if (mq_send(mqd, buff, strlen(buff), 0) == -1) {
            log.error("Message Queue send faild at RxCommunicatorThread, Exiting.");
        }
    }
    if (mq_close(mqd) == -1)
        log.error("Message queue close failed at RxCommunicatorThread, Exiting anyway.");
}

void TxCommunicatorThread(tcpImageContent *tcpImg) {    // Thread for Transferring data. Mainly transferring webcam image. UDP connection.
    logger log(LOGLEVEL_DEBUG);
    std::string encodedImageContent;
    while (!recieve_addr_set_flag){}
    const char *tcp_server_addr = recieve_addr.c_str();
    log.debug(tcp_server_addr);
    //udp udp;
    //udp.send_setup(tcp_server_addr, 8092);
    tcp tcp(8092);
    tcp.send_setup(tcp_server_addr, 8092);
    while (!stop_tx_thread_flag) {
        //encodedImageContent = globalEncodedImageContent->getNextContent();
        encodedImageContent = tcpImg->getContent();
        const int content_size = encodedImageContent.length();
        if (!(encodedImageContent.empty())) {  // Check if there is a worthwhile content.
            //udp.send(encodedImageContent);  // Send encoded image via udp.
            tcp.send_content(encodedImageContent);
        }
    }
}
/**
int main(int argc, char *argv[]) {
    // Some initial stuff for opencv.
    raspicam::RaspiCam_Cv Camera;
    cv::Mat frame;
    std::vector<uchar> buff;

    //setup
    Camera.set( cv::CAP_PROP_FORMAT, CV_8UC1 );

    std::string movementCode(R"({"joystick": {"r": 0, "sita": 0}, "shoot": 0, "LR": 0})");

    //Initializing threads;
    //globalEncodedImageContent globalEncodedImageContent;
    tcpImageContent tcpImg;

    std::thread Rx(RxCommunicatorThread, movementCode);
    //std::thread Tx(TxCommunicatorThread, &globalEncodedImageContent);
    std::thread Tx(TxCommunicatorThread, &tcpImg);
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
        //globalEncodedImageContent.convertFrame(frame);
        tcpImg.convertContent(frame);
        Camera.grab();
        Camera.retrieve(frame);
    }
    Camera.release();
    return 0;
}**/
int main(int argc, char *argv[]){
    std::string movementCode(R"({"joystick": {"r": 0, "sita": 0}, "shoot": 0, "LR": 0})");
    std::thread Rx(RxCommunicatorThread, movementCode);
    while (1){}
    return 0;
}