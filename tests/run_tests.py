# coding=utf-8
from subprocess import call
import time
import sys
import random

sys.path.insert(0, '../ukkonen')
sys.path.insert(0, '../colussi')
from colussi import Colussi
from ukkonen import Ukkonen


def test_dc3(filename, p):
    results_file = "results_file"
    call(["../dc3/dc3_match", filename, p, results_file])
    f = open(results_file)
    results = []
    dc3_time = float(f.readline())  # tiempo que tomó armar el suffix array
    search_time = float(f.readline())  # tiempo que tomó la búsqueda
    for l in f.readlines():
        results += [int(l)]
    return search_time, dc3_time, results


def test_col(filename, p):
    start = time.time()
    f = open(filename)
    t = f.read()
    alg1 = Colussi(t)
    results = alg1.match(p)
    end = time.time()
    col_time = end - start
    return col_time, results


def test_uko(filename, p):
    start = time.time()
    f = open(filename)
    t = f.read()
    alg2 = Ukkonen(t)
    results = alg2.match(p)
    end = time.time()
    uko_time = end - start
    print("Ukkonen -> ", str(end - start))
    return uko_time, results


filenames = sys.argv[1:]
lengths = [5, 10, 25, 50, 75, 100, 200]  # largo de los patrones a testear
out = open("out.csv", 'w')  # csv output
import os

for filename in filenames:
    print("\n\n")
    print("File: " + os.path.basename(filename))
    f1 = open(filename)
    t1 = f1.read().rstrip()  # saco \n final
    i = 0

    for l in lengths:
        # Patron al azar de longitud l
        print("Pattern length: " + str(l))
        pos = random.randint(0, len(t1) - 1)
        p = t1[pos:pos + l]
        print("Testing Colussi ...")
        col_time, col_results = test_col(filename, p)
        print("Testing DC3 ...")
        search_time, dc3_time, dc3_results = test_dc3(filename, p)
        # print("Testing Ukkonen ...")
        # uko_time, uko_results = test_uko(filename, p)
        uko_time = 0.0

        result = str(
            col_results == dc3_results)  # En lugar de esto que se fije si uko_results = col_results = dc3_results

        out.write(os.path.basename(filename) + "\t" + str(len(t1)) + "\t" + str(
            len(set(t1))) + "\t" + p + "\t" + "{0:.3f}".format(
            col_time) + "\t" + "{0:.3f}".format(uko_time) + "\t" + "{0:.3f}".format(
            dc3_time) + "\t" + str(col_results == dc3_results) + "\t")
