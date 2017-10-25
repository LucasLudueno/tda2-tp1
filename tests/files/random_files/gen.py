import sys
import string
import random
l = [500000] # tamaños de los archivos a generar
s = set(string.printable)-set(string.whitespace) # generar archivos con estos caracteres
n = [2,5,10,25,50,75,len(s)] # tamanio del alfabetp
for n_i in n:
	a = random.sample(s,n_i) # caracter al azar
	for l_i in l:
		for i in range(2):
			# generar 2 archivos por cada tamanio de archivo por cada tamanio de alfabeto
			filename = "random_"+str(n_i)+"chars_"+str(l_i)+"_"+str(i+1)
			f = open(filename,"w")
			for i in range(l_i):
				f.write(random.choice(a))
			print('Finished file \"'+filename+'\"')
