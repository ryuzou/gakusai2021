# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.16

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/pi/gakusai2021/Server

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/pi/gakusai2021/Server/cmake-build-debug

# Utility rule file for uninstall.

# Include the progress variables for this target.
include raspicam/CMakeFiles/uninstall.dir/progress.make

raspicam/CMakeFiles/uninstall:
	cd /home/pi/gakusai2021/Server/cmake-build-debug/raspicam && /usr/bin/cmake -P /home/pi/gakusai2021/Server/cmake-build-debug/raspicam/cmake_uninstall.cmake

uninstall: raspicam/CMakeFiles/uninstall
uninstall: raspicam/CMakeFiles/uninstall.dir/build.make

.PHONY : uninstall

# Rule to build all files generated by this target.
raspicam/CMakeFiles/uninstall.dir/build: uninstall

.PHONY : raspicam/CMakeFiles/uninstall.dir/build

raspicam/CMakeFiles/uninstall.dir/clean:
	cd /home/pi/gakusai2021/Server/cmake-build-debug/raspicam && $(CMAKE_COMMAND) -P CMakeFiles/uninstall.dir/cmake_clean.cmake
.PHONY : raspicam/CMakeFiles/uninstall.dir/clean

raspicam/CMakeFiles/uninstall.dir/depend:
	cd /home/pi/gakusai2021/Server/cmake-build-debug && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/pi/gakusai2021/Server /home/pi/gakusai2021/Server/raspicam /home/pi/gakusai2021/Server/cmake-build-debug /home/pi/gakusai2021/Server/cmake-build-debug/raspicam /home/pi/gakusai2021/Server/cmake-build-debug/raspicam/CMakeFiles/uninstall.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : raspicam/CMakeFiles/uninstall.dir/depend

