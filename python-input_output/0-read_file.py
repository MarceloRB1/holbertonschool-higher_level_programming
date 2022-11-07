#!/usr/bin/python3
""" Module read_file"""


def read_file(filename=""):
    """ read_file and print in stdout"""
    with open(filename, encoding='utf-8') as File:
        print(File.read(), end="")
