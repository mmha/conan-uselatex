# -*- coding: utf-8 -*-

from conans import ConanFile, CMake, tools
import os


class TestPackageConan(ConanFile):
    generators = "cmake_paths"

    def build(self):
        cmake = CMake(self)
        cmake.configure()

    def test(self):
        pass