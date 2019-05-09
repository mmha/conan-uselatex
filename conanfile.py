# -*- coding: utf-8 -*-

from conans import ConanFile, tools
import os


class UseLATEXConan(ConanFile):
    name = "uselatex"
    version = "2.4.9"
    description = "Compile LaTeX with CMake"
    topics = ("uselatex", "cmake", "tex", "latex")
    url = "https://github.com/bincrafters/conan-uselatex"
    homepage = "https://gitlab.kitware.com/kmorel/UseLATEX"
    author = "Bincrafters <bincrafters@gmail.com>"
    license = "BSD-3-Clause"
    no_copy_source = True

    exports = ["LICENSE.md"]

    _source_subfolder = "source_subfolder"

    def system_requirements(self):
        pack_names = []
        os_info = tools.OSInfo()
        if os_info.with_apt:
            pack_names = ["texlive-latex-base", "imagemagick"]
        elif os_info.with_pacman:
            pack_names = ["texlive-core", "imagemagick"]
        elif os_info.with_yum:
            pack_names = ["texlive-latex", "imagemagick"]

        for package in pack_names:
            installer = tools.SystemPackageTool()
            installer.install(package)

    def source(self):
        source_url = "https://gitlab.kitware.com/kmorel/UseLATEX"
        sha256 = "a0bb9b1a8b8beea0e2758c2f86bfbc1a5d4f45f11d93aab3f7473ea21a857643"
        tools.get("{0}/-/archive/Version{1}/UseLATEX-Version{1}.tar.gz".format(source_url, self.version), sha256=sha256)
        extracted_dir = "UseLATEX-Version" + self.version

        os.rename(extracted_dir, self._source_subfolder)


    def package(self):
        self.copy(pattern="UseLATEX.cmake", src=self._source_subfolder)


    def package_id(self):
        self.info.header_only()
