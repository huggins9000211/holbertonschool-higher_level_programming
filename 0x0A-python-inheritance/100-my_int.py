#!/usr/bin/python3
"""MY list"""


class MyInt(int):
    """Mylist claass"""

    def __eq__(self, value):
        """test"""
        return super().__ne__(value)

    def __ne__(self, value):
        """test"""
        return super().__eq__(value)
