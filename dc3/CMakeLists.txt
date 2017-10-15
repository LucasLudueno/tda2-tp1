cmake_minimum_required(VERSION 3.5)
project(new_version)

set(CMAKE_CXX_STANDARD 11)

set(SOURCE_FILES main.cpp search.cpp dc3.cpp)
add_executable(dc3 ${SOURCE_FILES})
