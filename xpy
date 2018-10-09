#!/bin/sh
env PYTHONPATH=$(echo lib/cpb/) LD_LIBRARY_PATH=$(echo /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/lib/) python $1