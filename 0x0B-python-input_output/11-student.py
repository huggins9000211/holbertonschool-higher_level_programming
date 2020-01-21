#!/usr/bin/python3
"""File I/O"""


class Student():
    """File I/O"""

    def __init__(self, first_name, last_name, age):
        """File I/O"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """File I/O"""
        return (self.__dict__)
