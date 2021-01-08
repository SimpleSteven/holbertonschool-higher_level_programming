#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_normal_cases(self):
        '''Normal cases should pass without raise
          any error'''
        self.assertAlmostEqual(max_integer([1, 2, 9, 3]), 9)
        self.assertAlmostEqual(max_integer([1.99, 2.89, 9.1, 3.8998]), 9.1)
        self.assertAlmostEqual(max_integer([-1.99, 2.89, -9.1, 3.8998]), 3.8998)
        self.assertAlmostEqual(max_integer([-1.99, 2.89, -100e+1000, 3.8998]), 3.8998)
        self.assertAlmostEqual(max_integer([-1.99, 2.89, 100e+1000, 3.8998]), 100e+1000)
        self.assertAlmostEqual(max_integer(["a", "b", "c"]), "c")
        self.assertAlmostEqual(max_integer("aaeeiioouu"), "u")
        self.assertAlmostEqual(max_integer(), None)

    def test_non_numbers(self):
        '''Raise an error, is the list, doesn't contain
        just numbers'''
        self.assertRaises(TypeError, max_integer, [True, "2", "3"])
        self.assertRaises(TypeError, max_integer, True)
        self.assertRaises(TypeError, max_integer, [1, 2], [1, 2])
        self.assertRaises(TypeError, max_integer, [1, 2, "hol", "berton"])