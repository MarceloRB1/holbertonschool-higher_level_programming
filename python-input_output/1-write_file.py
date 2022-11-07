#!/usr/bin/python3
""" Module write_file"""


def write_file(filename="", text=""):
    """ write_file and print character writed """
    with open(filename, "w") as File:
        return File.write(text)
