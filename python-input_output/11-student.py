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
        MyDict = {}

        if attrs is None:
            return self.__dict__

        for atr in attrs:
                if atr in self.__dict__:
                    MyDict[atr] = self.__dict__[atr]
        return MyDict

    def reload_from_json(self, json):
        """
            replaces all atrributes of the Student instance
            json: allwas be a dictionary
        """
        if json == {}:
            return
        self.__dict__ = json
