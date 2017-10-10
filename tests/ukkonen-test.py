#!/usr/bin/python

import sys
import unittest
sys.path.insert(0, 'ukkonen') # ../ukkonen

from ukkonen import Ukkonen

class TestEstadisticoClass(unittest.TestCase):
    def test_banana(self):
        s = "banana$"
        match = 'ana'
        algorithm = Ukkonen(s)

        self.assertEqual(algorithm.match('ana'), True)

if __name__ == '__main__':
    unittest.main()
