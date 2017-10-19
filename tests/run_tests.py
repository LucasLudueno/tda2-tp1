from subprocess import call
import time
import sys
sys.path.insert(0, '../ukkonen')
sys.path.insert(0, '../colussi')
from colussi import Colussi
from ukkonen import Ukkonen

filename = sys.argv[1]
p = sys.argv[2]

start = time.time()
f = open(filename)
t = f.read()
alg1 = Colussi(t)
result_col = alg1.match(p)
end = time.time()
print("Colussi -> ", str(end-start))

start = time.time()
f = open(filename)
t = f.read()
alg2 = Ukkonen(t)
result_uko = alg2.match(p)
end = time.time()
print("Ukkonen -> ", str(end-start))

start = time.time()
sa_file = "sa_file"
results_file = "results_file"
call(["../dc3/dc3_match",filename,p,results_file])
f = open(results_file)
result_dc3 = []
for l in f.readlines():
	result_dc3 += [int(l)]
end = time.time()
print("DC3 -> ", str(end-start))

if result_col == result_dc3:
	if len(result_col) > 0 and result_uko == True:
		print("Test OK - Found ",str(len(result_col)), " matches")
	elif len(result_col) == 0 and result_uko == False:
		print("Test OK - Found ",str(len(result_col)), " matches")
	else:
		print(len(result_col))
		print(len(result_dc3))
		print(result_uko)
		print("Test ERROR 1")
else:
	print("Test ERROR 2")	
