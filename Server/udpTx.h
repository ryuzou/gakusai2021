//
// Created by ryuzo on 2021/09/28.
//

#ifndef SERVER_UDPTX_H
#define SERVER_UDPTX_H

#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <unistd.h>
#include <iostream>


class udpTx {
    int sock;
    struct sockaddr_in addr{};
public:
    udpTx(const int port){
        sock = socket(AF_INET, SOCK_DGRAM, 0);
        memset(&addr, 0, sizeof(struct sockaddr_in));
        addr.sin_family = AF_INET;
        addr.sin_addr.s_addr = htonl(INADDR_ANY);
        addr.sin_port = htons(port);
    }
    int send(const std::string& content){
        sendto(sock, content.c_str(), content.length(), 0, (struct sockaddr *)&addr, sizeof(addr));
        return 0;
    }

    ~udpTx(){
        close(sock);
    }
};


#endif //SERVER_UDPTX_H
