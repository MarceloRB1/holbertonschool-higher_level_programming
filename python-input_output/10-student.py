#!/usr/bin/python3
""" Module Student"""


class Student:
    def __init__(self, first_name, last_name, age):
        """ constructor of the class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ return a dict of the class"""
        Mydict = vars(self)
        Mydict2 = dict()
        if attrs is None:
            return Mydict

        for key, value in Mydict.items():
            for key_att in attrs:
                if key is key_att:
                    Mydict2[key] = value
        return Mydict2
