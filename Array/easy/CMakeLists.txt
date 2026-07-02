cmake_minimum_required(VERSION 3.16)
project(Array)

set(CMAKE_CXX_STANDARD 14)

file(GLOB SOURCES "*.cpp")

foreach(src ${SOURCES})
    get_filename_component(exec_name ${src} NAME_WE)
    add_executable(${exec_name} ${src}
    )
endforeach()