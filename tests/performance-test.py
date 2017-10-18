#!/usr/bin/python

import sys
import time

sys.path.insert(0, 'ukkonen')
sys.path.insert(0, 'colussi')

from ukkonen import Ukkonen
from colussi import Colussi

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

algorithms = [Ukkonen, Colussi]

pattern = "pattern"

def main():
    for file_name in TEST_FILES:
        read_file = open('tests/files/' + file_name, 'r')
        content = read_file.read()

        print ""
        print "File: " + file_name

        for algorithm in algorithms:
            initial_time = time.time()

            alg = algorithm(content)
            alg.match(pattern)

            final_time = time.time()

            print alg.name() + " : " + str(final_time - initial_time)


if __name__ == "__main__":
    main()
