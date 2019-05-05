cmake_minimum_required(VERSION 3.0)
project(test_package LANGUAGES NONE)

include("${CMAKE_BINARY_DIR}/conan_paths.cmake")

list(APPEND CMAKE_MODULE_PATH ${CMAKE_CURRENT_SOURCE_DIR})
find_package(UseLATEX 2.4.9 REQUIRED)

if(NOT DEFINED LATEX_USE_LATEX_LOCATION)
	message(FATAL_ERROR "UseLATEX not included properly")
endif()
