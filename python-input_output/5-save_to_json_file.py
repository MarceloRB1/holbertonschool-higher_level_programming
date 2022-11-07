#!/usr/bin/python3
""" Module save to json_file"""
import json


def save_to_json_file(my_obj, filename):
    """ Save te obj in a JSON file """
    with open(filename, mode="w") as File:
        json.dump(my_obj, File)
