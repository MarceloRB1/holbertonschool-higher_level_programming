#!/usr/bin/python3
""" Module class to json"""


def class_to_json(obj):
    """ Create a dictionary of a class"""
    return vars(obj)
