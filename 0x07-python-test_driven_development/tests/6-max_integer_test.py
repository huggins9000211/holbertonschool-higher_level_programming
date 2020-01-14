#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_func(self):
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([4, 5, 6]), 6)
        self.assertEqual(max_integer([-5, 5, 6]), 6)
        self.assertEqual(max_integer([0]), 0)
        self.assertEqual(max_integer([5.5]), 5.5)
        self.assertEqual(max_integer("test"), 't')
        self.assertEqual(max_integer(["test"]), 'test')
        
        
        with self.assertRaises(TypeError):
            max_integer(5)
            print(max_integer(["test", 0]))