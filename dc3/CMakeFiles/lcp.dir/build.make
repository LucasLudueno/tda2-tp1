# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.9

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
CMAKE_COMMAND = /usr/local/bin/cmake

# The command to remove a file.
RM = /usr/local/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/lucas/git/tda2-tp1/dc3

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/lucas/git/tda2-tp1/dc3

# Include any dependencies generated for this target.
include CMakeFiles/lcp.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/lcp.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/lcp.dir/flags.make

CMakeFiles/lcp.dir/lcp.cpp.o: CMakeFiles/lcp.dir/flags.make
CMakeFiles/lcp.dir/lcp.cpp.o: lcp.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/lucas/git/tda2-tp1/dc3/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/lcp.dir/lcp.cpp.o"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/lcp.dir/lcp.cpp.o -c /home/lucas/git/tda2-tp1/dc3/lcp.cpp

CMakeFiles/lcp.dir/lcp.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/lcp.dir/lcp.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/lucas/git/tda2-tp1/dc3/lcp.cpp > CMakeFiles/lcp.dir/lcp.cpp.i

CMakeFiles/lcp.dir/lcp.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/lcp.dir/lcp.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/lucas/git/tda2-tp1/dc3/lcp.cpp -o CMakeFiles/lcp.dir/lcp.cpp.s

CMakeFiles/lcp.dir/lcp.cpp.o.requires:

.PHONY : CMakeFiles/lcp.dir/lcp.cpp.o.requires

CMakeFiles/lcp.dir/lcp.cpp.o.provides: CMakeFiles/lcp.dir/lcp.cpp.o.requires
	$(MAKE) -f CMakeFiles/lcp.dir/build.make CMakeFiles/lcp.dir/lcp.cpp.o.provides.build
.PHONY : CMakeFiles/lcp.dir/lcp.cpp.o.provides

CMakeFiles/lcp.dir/lcp.cpp.o.provides.build: CMakeFiles/lcp.dir/lcp.cpp.o


# Object files for target lcp
lcp_OBJECTS = \
"CMakeFiles/lcp.dir/lcp.cpp.o"

# External object files for target lcp
lcp_EXTERNAL_OBJECTS =

lcp: CMakeFiles/lcp.dir/lcp.cpp.o
lcp: CMakeFiles/lcp.dir/build.make
lcp: CMakeFiles/lcp.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/lucas/git/tda2-tp1/dc3/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable lcp"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/lcp.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/lcp.dir/build: lcp

.PHONY : CMakeFiles/lcp.dir/build

CMakeFiles/lcp.dir/requires: CMakeFiles/lcp.dir/lcp.cpp.o.requires

.PHONY : CMakeFiles/lcp.dir/requires

CMakeFiles/lcp.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/lcp.dir/cmake_clean.cmake
.PHONY : CMakeFiles/lcp.dir/clean

CMakeFiles/lcp.dir/depend:
	cd /home/lucas/git/tda2-tp1/dc3 && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/lucas/git/tda2-tp1/dc3 /home/lucas/git/tda2-tp1/dc3 /home/lucas/git/tda2-tp1/dc3 /home/lucas/git/tda2-tp1/dc3 /home/lucas/git/tda2-tp1/dc3/CMakeFiles/lcp.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/lcp.dir/depend
