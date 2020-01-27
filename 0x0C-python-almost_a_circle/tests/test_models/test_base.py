#!/usr/bin/python3
""" tests """
import unittest
from models.base import Base

class Test_base(unittest.TestCase):
    def test_1(self):
        myBase = Base()
        self.assertEqual(myBase.id, 1)
        myBase2 = Base()
        self.assertEqual(myBase2.id, 2)
        myBase3 = Base(89)
        self.assertEqual(myBase3.id, 89)
        myBase4 = Base("test")
        self.assertEqual(myBase4.id, "test")
        myBase5 = Base()
        self.assertEqual(myBase5.id, 3)
        myBase6 = Base([1, 2, 3])
        self.assertEqual(myBase6.id, [1, 2, 3])
        myBase7 = Base((2,))
        self.assertEqual(myBase7.id, (2,))
