//
// Created by ryuzo on 2021/09/28.
//

#ifndef SERVER_UDP_H
#define SERVER_UDP_H

#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <unistd.h>
#include <iostream>

#include "errorhandling.h"


class udp {
    int sock;
    struct sockaddr_in addr{};

public:
    explicit udp(){
        logger log(LOGLEVEL_DEBUG);
        sock = socket(AF_INET, SOCK_DGRAM, 0);
        memset(&addr, 0, sizeof(struct sockaddr_in));
        addr.sin_family = AF_INET;
    }
    int send(const std::string& content){
        logger log(LOGLEVEL_DEBUG);
        struct sockaddr_in _a = addr;
        int ret = sendto(sock, content.c_str(), content.length(), 0, (struct sockaddr *)&addr, sizeof(addr));
        if (ret == -1){
            log.error("Connection error:.");
        }
        return ret;
    }
    int send_setup(const char *destination_addr, int port){
        inet_pton(AF_INET, destination_addr, &addr.sin_addr);
        addr.sin_port = htons(port);
        return 0;
    }

    ~udp(){
        close(sock);
    }
};


#endif //SERVER_UDP_H
