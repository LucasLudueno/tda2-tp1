#!/usr/bin/python

import sys
import unittest
sys.path.insert(0, '../ukkonen') # ../ukkonen

from ukkonen import Ukkonen

class TestEstadisticoClass(unittest.TestCase):
    def test_banana(self):
        s = "banana$"
        algorithm = Ukkonen(s)

        self.assertEqual(algorithm.match('banana'), True)
        self.assertEqual(algorithm.match('banana$'), True)
        self.assertEqual(algorithm.match('bana'), True)
        self.assertEqual(algorithm.match('ana'), True)
        self.assertEqual(algorithm.match('ban'), True)
        self.assertEqual(algorithm.match('b'), True)

        self.assertEqual(algorithm.match('aba'), False)
        self.assertEqual(algorithm.match('anab'), False)
        self.assertEqual(algorithm.match('baa'), False)

if __name__ == '__main__':
    unittest.main()
