#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    a = len(sys.argv)
    result = 0

    for i in range(1, a):
        result = result + int(sys.argv[i])
    print("{}".format(result))
