#include <stdio.h> //printf(), fprintf(), perror(), getc()
#include <sys/socket.h> //socket(), bind(), sendto(), recvfrom()
#include <arpa/inet.h> // struct sockaddr_in, struct sockaddr, inet_ntoa(), inet_aton()
#include <stdlib.h> //atoi(), exit(), EXIT_FAILURE, EXIT_SUCCESS
#include <string.h> //memset(), strcmp()
#include <unistd.h> //close()
#include <mqueue.h>
#include <cstdint>
#include <iostream>
#include <mutex>
#include <thread>
#include <pthread.h>
#include <opencv2/opencv.hpp>
#include <atomic>

#define MSG_FAILURE -1

#define MAX_MSGSIZE 1024
#define MAX_BUFSIZE (MAX_MSGSIZE + 1)

pthread_mutex_t mutex = PTHREAD_MUTEX_INITIALIZER;
std::string globalEncodedImageContent("");
std::atomic<bool> stop_tx_thread_flag(false);

void RxCommunicatorThread(){    //Thread for Receiving data from client. TCP connection.

}

void TxCommunicatorThread(){    //Thread for Transferring data. Mainly transferring webcam image. UDP connection.
    std::string encodedImageContent;
    while (!stop_tx_thread_flag){
        pthread_mutex_lock(&mutex);
        // Getting encoded image content from main process, critical behavior.
        encodedImageContent = globalEncodedImageContent;
        // Ending critical process.

        pthread_mutex_unlock(&mutex);
        if (!(encodedImageContent == "")){
            printf("test");
        }
    }
}

int main(int argc, char* argv[]) {
    // Some initial stuff for opencv.
    cv::VideoCapture cap;
    cv::Mat frame;
    std::vector<uchar> buff;

    //Initializing threads;
    std::thread Rx(RxCommunicatorThread);
    std::thread Tx(TxCommunicatorThread);

    // Setting up camera streaming via opencv.
    cap.open(0);
    if (!cap.isOpened()){
        printf("Could not open stream");
        return -1;
    }
    int vidWidth = cap.get(cv::CAP_PROP_FRAME_WIDTH);
    int vidHeight = cap.get(cv::CAP_PROP_FRAME_HEIGHT);
    std::cout << "Video Width is " << vidWidth << std::endl;
    std::cout << "Video Height is " << vidHeight << std::endl;
    cap >> frame;
    while (!frame.empty()){
        // Encoding camera stream with webp.
        cv::imencode(".webp", frame, buff, std::vector<int>()); // Didn't need libwebp?
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