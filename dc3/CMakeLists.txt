cmake_minimum_required(VERSION 3.5)
project(dc3)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_FLAGS "-O3")
set(SOURCE_FILES main.cpp search.cpp dc3.cpp)
add_executable(dc3 ${SOURCE_FILES})
