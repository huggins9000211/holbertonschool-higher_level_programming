#!/usr/bin/python3
"""Lookup func"""


def inherits_from(obj, a_class):
    """Lookup func"""
    if issubclass(type(obj), a_class):
        return True
    return False
