#!/usr/bin/python3
import sys
if __name__ == "__main__":
    argv = sys.argv
    argc = len(argv) - 1
    if argc == 0:
        print("0 arguments.")
    elif (argc == 1):
        print("1 argument:")
        print("1: {}".format(argv[1]))
    else:
        print("{} arguments:".format(argc))
        for i in range(argc):
            i = i + 1
            print("{}: {}".format(i, argv[i]))
