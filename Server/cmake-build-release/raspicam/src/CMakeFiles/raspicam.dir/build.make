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
CMAKE_BINARY_DIR = /home/pi/gakusai2021/Server/cmake-build-release

# Include any dependencies generated for this target.
include raspicam/src/CMakeFiles/raspicam.dir/depend.make

# Include the progress variables for this target.
include raspicam/src/CMakeFiles/raspicam.dir/progress.make

# Include the compile flags for this target's objects.
include raspicam/src/CMakeFiles/raspicam.dir/flags.make

raspicam/src/CMakeFiles/raspicam.dir/raspicam.cpp.o: raspicam/src/CMakeFiles/raspicam.dir/flags.make
raspicam/src/CMakeFiles/raspicam.dir/raspicam.cpp.o: ../raspicam/src/raspicam.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/pi/gakusai2021/Server/cmake-build-release/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object raspicam/src/CMakeFiles/raspicam.dir/raspicam.cpp.o"
	cd /home/pi/gakusai2021/Server/cmake-build-release/raspicam/src && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/raspicam.dir/raspicam.cpp.o -c /home/pi/gakusai2021/Server/raspicam/src/raspicam.cpp

raspicam/src/CMakeFiles/raspicam.dir/raspicam.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/raspicam.dir/raspicam.cpp.i"
	cd /home/pi/gakusai2021/Server/cmake-build-release/raspicam/src && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/pi/gakusai2021/Server/raspicam/src/raspicam.cpp > CMakeFiles/raspicam.dir/raspicam.cpp.i

raspicam/src/CMakeFiles/raspicam.dir/raspicam.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/raspicam.dir/raspicam.cpp.s"
	cd /home/pi/gakusai2021/Server/cmake-build-release/raspicam/src && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/pi/gakusai2021/Server/raspicam/src/raspicam.cpp -o CMakeFiles/raspicam.dir/raspicam.cpp.s

raspicam/src/CMakeFiles/raspicam.dir/raspicam_still.cpp.o: raspicam/src/CMakeFiles/raspicam.dir/flags.make
raspicam/src/CMakeFiles/raspicam.dir/raspicam_still.cpp.o: ../raspicam/src/raspicam_still.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/pi/gakusai2021/Server/cmake-build-release/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building CXX object raspicam/src/CMakeFiles/raspicam.dir/raspicam_still.cpp.o"
	cd /home/pi/gakusai2021/Server/cmake-build-release/raspicam/src && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/raspicam.dir/raspicam_still.cpp.o -c /home/pi/gakusai2021/Server/raspicam/src/raspicam_still.cpp

raspicam/src/CMakeFiles/raspicam.dir/raspicam_still.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/raspicam.dir/raspicam_still.cpp.i"
	cd /home/pi/gakusai2021/Server/cmake-build-release/raspicam/src && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/pi/gakusai2021/Server/raspicam/src/raspicam_still.cpp > CMakeFiles/raspicam.dir/raspicam_still.cpp.i

raspicam/src/CMakeFiles/raspicam.dir/raspicam_still.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/raspicam.dir/raspicam_still.cpp.s"
	cd /home/pi/gakusai2021/Server/cmake-build-release/raspicam/src && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/pi/gakusai2021/Server/raspicam/src/raspicam_still.cpp -o CMakeFiles/raspicam.dir/raspicam_still.cpp.s

raspicam/src/CMakeFiles/raspicam.dir/private/private_impl.cpp.o: raspicam/src/CMakeFiles/raspicam.dir/flags.make
raspicam/src/CMakeFiles/raspicam.dir/private/private_impl.cpp.o: ../raspicam/src/private/private_impl.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/pi/gakusai2021/Server/cmake-build-release/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Building CXX object raspicam/src/CMakeFiles/raspicam.dir/private/private_impl.cpp.o"
	cd /home/pi/gakusai2021/Server/cmake-build-release/raspicam/src && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/raspicam.dir/private/private_impl.cpp.o -c /home/pi/gakusai2021/Server/raspicam/src/private/private_impl.cpp

raspicam/src/CMakeFiles/raspicam.dir/private/private_impl.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/raspicam.dir/private/private_impl.cpp.i"
	cd /home/pi/gakusai2021/Server/cmake-build-release/raspicam/src && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/pi/gakusai2021/Server/raspicam/src/private/private_impl.cpp > CMakeFiles/raspicam.dir/private/private_impl.cpp.i

raspicam/src/CMakeFiles/raspicam.dir/private/private_impl.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/raspicam.dir/private/private_impl.cpp.s"
	cd /home/pi/gakusai2021/Server/cmake-build-release/raspicam/src && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/pi/gakusai2021/Server/raspicam/src/private/private_impl.cpp -o CMakeFiles/raspicam.dir/private/private_impl.cpp.s

raspicam/src/CMakeFiles/raspicam.dir/private/threadcondition.cpp.o: raspicam/src/CMakeFiles/raspicam.dir/flags.make
raspicam/src/CMakeFiles/raspicam.dir/private/threadcondition.cpp.o: ../raspicam/src/private/threadcondition.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/pi/gakusai2021/Server/cmake-build-release/CMakeFiles --progress-num=$(CMAKE_PROGRESS_4) "Building CXX object raspicam/src/CMakeFiles/raspicam.dir/private/threadcondition.cpp.o"
	cd /home/pi/gakusai2021/Server/cmake-build-release/raspicam/src && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/raspicam.dir/private/threadcondition.cpp.o -c /home/pi/gakusai2021/Server/raspicam/src/private/threadcondition.cpp

raspicam/src/CMakeFiles/raspicam.dir/private/threadcondition.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/raspicam.dir/private/threadcondition.cpp.i"
	cd /home/pi/gakusai2021/Server/cmake-build-release/raspicam/src && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/pi/gakusai2021/Server/raspicam/src/private/threadcondition.cpp > CMakeFiles/raspicam.dir/private/threadcondition.cpp.i

raspicam/src/CMakeFiles/raspicam.dir/private/threadcondition.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/raspicam.dir/private/threadcondition.cpp.s"
	cd /home/pi/gakusai2021/Server/cmake-build-release/raspicam/src && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/pi/gakusai2021/Server/raspicam/src/private/threadcondition.cpp -o CMakeFiles/raspicam.dir/private/threadcondition.cpp.s

raspicam/src/CMakeFiles/raspicam.dir/private_still/private_still_impl.cpp.o: raspicam/src/CMakeFiles/raspicam.dir/flags.make
raspicam/src/CMakeFiles/raspicam.dir/private_still/private_still_impl.cpp.o: ../raspicam/src/private_still/private_still_impl.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/pi/gakusai2021/Server/cmake-build-release/CMakeFiles --progress-num=$(CMAKE_PROGRESS_5) "Building CXX object raspicam/src/CMakeFiles/raspicam.dir/private_still/private_still_impl.cpp.o"
	cd /home/pi/gakusai2021/Server/cmake-build-release/raspicam/src && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/raspicam.dir/private_still/private_still_impl.cpp.o -c /home/pi/gakusai2021/Server/raspicam/src/private_still/private_still_impl.cpp

raspicam/src/CMakeFiles/raspicam.dir/private_still/private_still_impl.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/raspicam.dir/private_still/private_still_impl.cpp.i"
	cd /home/pi/gakusai2021/Server/cmake-build-release/raspicam/src && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/pi/gakusai2021/Server/raspicam/src/private_still/private_still_impl.cpp > CMakeFiles/raspicam.dir/private_still/private_still_impl.cpp.i

raspicam/src/CMakeFiles/raspicam.dir/private_still/private_still_impl.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/raspicam.dir/private_still/private_still_impl.cpp.s"
	cd /home/pi/gakusai2021/Server/cmake-build-release/raspicam/src && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/pi/gakusai2021/Server/raspicam/src/private_still/private_still_impl.cpp -o CMakeFiles/raspicam.dir/private_still/private_still_impl.cpp.s

# Object files for target raspicam
raspicam_OBJECTS = \
"CMakeFiles/raspicam.dir/raspicam.cpp.o" \
"CMakeFiles/raspicam.dir/raspicam_still.cpp.o" \
"CMakeFiles/raspicam.dir/private/private_impl.cpp.o" \
"CMakeFiles/raspicam.dir/private/threadcondition.cpp.o" \
"CMakeFiles/raspicam.dir/private_still/private_still_impl.cpp.o"

# External object files for target raspicam
raspicam_EXTERNAL_OBJECTS =

raspicam/src/libraspicam.so.SOVERSION: raspicam/src/CMakeFiles/raspicam.dir/raspicam.cpp.o
raspicam/src/libraspicam.so.SOVERSION: raspicam/src/CMakeFiles/raspicam.dir/raspicam_still.cpp.o
raspicam/src/libraspicam.so.SOVERSION: raspicam/src/CMakeFiles/raspicam.dir/private/private_impl.cpp.o
raspicam/src/libraspicam.so.SOVERSION: raspicam/src/CMakeFiles/raspicam.dir/private/threadcondition.cpp.o
raspicam/src/libraspicam.so.SOVERSION: raspicam/src/CMakeFiles/raspicam.dir/private_still/private_still_impl.cpp.o
raspicam/src/libraspicam.so.SOVERSION: raspicam/src/CMakeFiles/raspicam.dir/build.make
raspicam/src/libraspicam.so.SOVERSION: /opt/vc/lib/libmmal_core.so
raspicam/src/libraspicam.so.SOVERSION: /opt/vc/lib/libmmal_util.so
raspicam/src/libraspicam.so.SOVERSION: /opt/vc/lib/libmmal.so
raspicam/src/libraspicam.so.SOVERSION: raspicam/src/CMakeFiles/raspicam.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/pi/gakusai2021/Server/cmake-build-release/CMakeFiles --progress-num=$(CMAKE_PROGRESS_6) "Linking CXX shared library libraspicam.so"
	cd /home/pi/gakusai2021/Server/cmake-build-release/raspicam/src && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/raspicam.dir/link.txt --verbose=$(VERBOSE)
	cd /home/pi/gakusai2021/Server/cmake-build-release/raspicam/src && $(CMAKE_COMMAND) -E cmake_symlink_library libraspicam.so.SOVERSION libraspicam.so.SOVERSION libraspicam.so

raspicam/src/libraspicam.so: raspicam/src/libraspicam.so.SOVERSION
	@$(CMAKE_COMMAND) -E touch_nocreate raspicam/src/libraspicam.so

# Rule to build all files generated by this target.
raspicam/src/CMakeFiles/raspicam.dir/build: raspicam/src/libraspicam.so

.PHONY : raspicam/src/CMakeFiles/raspicam.dir/build

raspicam/src/CMakeFiles/raspicam.dir/clean:
	cd /home/pi/gakusai2021/Server/cmake-build-release/raspicam/src && $(CMAKE_COMMAND) -P CMakeFiles/raspicam.dir/cmake_clean.cmake
.PHONY : raspicam/src/CMakeFiles/raspicam.dir/clean

raspicam/src/CMakeFiles/raspicam.dir/depend:
	cd /home/pi/gakusai2021/Server/cmake-build-release && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/pi/gakusai2021/Server /home/pi/gakusai2021/Server/raspicam/src /home/pi/gakusai2021/Server/cmake-build-release /home/pi/gakusai2021/Server/cmake-build-release/raspicam/src /home/pi/gakusai2021/Server/cmake-build-release/raspicam/src/CMakeFiles/raspicam.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : raspicam/src/CMakeFiles/raspicam.dir/depend

