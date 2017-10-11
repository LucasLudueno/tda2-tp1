#!/usr/bin/python

import sys
import time
import unittest
sys.path.insert(0, 'ukkonen') # ../ukkonen

from ukkonen import Ukkonen

TEST_FILES = [
    'ailing.txt',
    'bluekite.txt',
    'egmf.txt',
    'hprt.txt',
    'index.txt',
    'random.txt',
    'rbs.txt',
    'stm2.txt',
    'tiger.txt',
    'y.tab.txt'
]

def main():
    for file_name in TEST_FILES:
        read_file = open('tests/files/' + file_name, 'r')
        content = read_file.read()

        initial_time = time.time()

        Ukkonen(content)
        # DC3(content)
        # Colussi(content)

        final_time = time.time()

        print "Run: " + file_name
        print "Time: " + str(final_time - initial_time)
        print ""


if __name__ == "__main__":
  main()
