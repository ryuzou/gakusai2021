cmake_minimum_required(VERSION 3.16)
project(Server)

set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -pthread -lrt -O2 -lraspicam_cv")

find_package(OpenCV REQUIRED)
find_package(raspicam REQUIRED)
include_directories(${OpenCV_INCLUDE_DIRS})
include_directories(${raspicam_CV_DIRS})

add_executable(Server main.cpp json/json11.cpp json/json11.hpp errorhandling.h tcp.h globalEncodedImageContent.cpp globalEncodedImageContent.h base64.cpp base64.h)
target_link_libraries(Server ${OpenCV_LIBS} ${raspicam_CV_LIBS})