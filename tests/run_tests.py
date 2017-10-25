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
    end = time.time()
    uko_time = end - start

    start_again = time.time()
    results = alg2.match(p)
    end_again = time.time()
    search_time = end_again - start_again

    return search_time, uko_time, results


# filenames = sys.argv[1:]
filenames = [
    'files/ailing.txt',
    'files/bluekite.txt',
    'files/egmf.txt',
    'files/hprt.txt',
    'files/index.txt',
    'files/random.txt',
    'files/rbs.txt',
    'files/stm2.txt',
    'files/tiger.txt',
    'files/y.tab.txt',

    'files/random_files/random_2chars_500000_1',
    'files/random_files/random_5chars_500000_1',
    'files/random_files/random_10chars_500000_1',
    'files/random_files/random_25chars_500000_1',
    'files/random_files/random_50chars_500000_1',
    'files/random_files/random_75chars_500000_1',

    'files/random_files/random_2chars_1000000_1',
    'files/random_files/random_5chars_1000000_1',
    'files/random_files/random_10chars_1000000_1',
    'files/random_files/random_25chars_1000000_1',
    'files/random_files/random_50chars_1000000_1',
    'files/random_files/random_75chars_1000000_1',

    'files/random_files/random_2chars_2000000_1',
    'files/random_files/random_5chars_2000000_1',
    'files/random_files/random_10chars_2000000_1',
    'files/random_files/random_25chars_2000000_1',
    'files/random_files/random_50chars_2000000_1',
    'files/random_files/random_75chars_2000000_1'

    # 'files/random_files/random_2chars_4000000_1',
    # 'files/random_files/random_5chars_4000000_1',
    # 'files/random_files/random_10chars_4000000_1',
    # 'files/random_files/random_25chars_4000000_1',
    # 'files/random_files/random_50chars_4000000_1',
    # 'files/random_files/random_75chars_4000000_1',

    # 'files/random_files/random_2chars_800000_1',
    # 'files/random_files/random_5chars_800000_1',
    # 'files/random_files/random_10chars_800000_1',
    # 'files/random_files/random_25chars_800000_1',
    # 'files/random_files/random_50chars_800000_1',
    # 'files/random_files/random_75chars_800000_1'
]
lengths = [5, 10, 25, 50, 75, 100, 200]  # largo de los patrones a testear
out = open("out.csv", 'w')  # csv output
import os

# escribimos el header del archivo csv con los resultados
out.write(
    "Archivo" + "\t" +
    "Tamaño" + "\t" +
    "No se que" + "\t" +
    "Colussi Total" + "\t" +
    "Ukkonen Total" + "\t" +
    "Ukkonen constr" + "\t" +
    "Ukkonen match" + "\t" +
    "DC3 Total" + "\t" +
    "DC3 constr" + "\t" +
    "DC3 match" + "\t" +
    "Resultado" + "\t" +
    "Patron" + "\t" +
    "\n"
)

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
        dc3_search_time, dc3_time, dc3_results = test_dc3(filename, p)
        print("Testing Ukkonen ...")
        uko_search_time, uko_time, uko_results = test_uko(filename, p)

        # Analizamos si los tres algoritmos tuvieron el mismo resultado
        result = str(False)
        if col_results == dc3_results:
            if len(col_results) > 0 and uko_results:
                result = str(True)
            elif len(col_results) == 0 and not uko_results:
                result = str(True)

        # escribimos el resultado de la ejecucion en el archivo csv
        out.write(
            os.path.basename(filename) + "\t" +
            str(len(t1)) + "\t" +
            str(len(set(t1))) + "\t" +
            "{0:.5f}".format(col_time) + "\t" +
            "{0:.5f}".format(uko_time + uko_search_time) + "\t" +
            "{0:.5f}".format(uko_time) + "\t" +
            "{0:.5f}".format(uko_search_time) + "\t" +
            "{0:.5f}".format(dc3_time + dc3_search_time) + "\t" +
            "{0:.5f}".format(dc3_time) + "\t" +
            "{0:.5f}".format(dc3_search_time) + "\t" +
            str(col_results == dc3_results) + "\t" +
            str(len(p)) + "\t" # porque al imprimir todos los caracteres, habias /n y /t y se desformateaba el archivo
        )
        out.write("\n")
