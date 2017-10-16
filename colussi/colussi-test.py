import sys
import time
import unittest
sys.path.insert(0, 'colussi')
from colussi import Colussi

P = 'GCAGAGAG'
T = 'GCATCGCAGAGAGTATACAGTACG'
algorithm = Colussi(T)
print (algorithm.match(P))