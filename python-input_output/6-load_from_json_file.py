#!/usr/bin/python3
""" Module load_from_json_file"""
import json


def load_from_json_file(filename):
    """ create an Object from a JSON file """
    with open(filename, encoding="utf-8") as File:
        return json.load(File)
