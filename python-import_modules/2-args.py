#!/usr/bin/python3
import sys
num_args = len(sys.argv) - 1

if num_args == 0:
    print("0 arguments.")
else:
    print("{} {}:".format(num_args, "argument" if num_args == 1 else "arguments"))
    for i in range(1, len(sys.argv)):
        print("{}: {}".format(i, sys.argv[i]))
