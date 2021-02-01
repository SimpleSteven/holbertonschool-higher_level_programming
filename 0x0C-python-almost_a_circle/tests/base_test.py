#!/usr/bin/python3
''' **** Test cases for: ****
    **** base.py of task ****
    **** 1. Base Class   **** '''

import unittest
from models.base import Base


class Base_Edge_Cases(unittest.TestCase):
    ''' **** Test the edge cases **** '''

    def test_non_error(self):
        """ **** Normal cases **** """
        instance1 = Base()
        self.assertEqual(instance1.id, 1)
        instance2 = Base(20)
        self.assertEqual(instance2.id, 20)
        instance3 = Base()
        self.assertEqual(instance3.id, 2)

    #
    # def value_error_tests(self):
    #     ''' **** All the ValueError cases ****'''
    #     # Non integer argument passed
    #     self.assertRaises(ValueError, instance1 = Base,)
