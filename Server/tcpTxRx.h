//
// Created by ryuzo on 2021/10/24.
//

#ifndef SERVER_TCPTXRX_H
#define SERVER_TCPTXRX_H


#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <unistd.h>
#include <iostream>

#define BUFFER_SIZE 256

class tcpTxRx {
    int Sock{};
    int dstSock{};
    struct sockaddr_in addr{};
    struct sockaddr_in client;
    int numrcv{};
    char buffer[BUFFER_SIZE]{};

public:
    tcpTxRx(const int port){
        Sock = socket(AF_INET, SOCK_STREAM, 0);
        memset(&addr, 0, sizeof(struct sockaddr_in));
        addr.sin_family = AF_INET;
        addr.sin_addr.s_addr = htonl(INADDR_ANY);
        addr.sin_port = htons(port);
    }
    int send(const std::string& content){
        return 0;
    }
    int receive_setup(){
        bind(Sock, (struct sockaddr *)&addr, sizeof(addr));
        listen(Sock, 1);
        return 0;
    }
    char *recieve(){
        numrcv = recv(dstSock, buffer, BUFFER_SIZE, 0);
        if(numrcv == 0 || numrcv == -1) {
            close(dstSock);
        }
        return buffer;
    }

    char *connect() {
        dstSock = accept(Sock, (struct sockaddr *)&client, reinterpret_cast<socklen_t *>(sizeof(client)));
        return inet_ntoa(addr.sin_addr);
    }

    ~tcpTxRx(){
        close(Sock);
    }
};


#endif //SERVER_TCPTXRX_H
