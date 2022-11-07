#!/usr/bin/python3
""" Module from_json_string """
import json


def from_json_string(my_str):
    """ return an objetc represented by JSON string """
    return json.loads(my_str)
