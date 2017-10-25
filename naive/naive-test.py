from naive import Naive

P = 'GCAGAGAG'
T = 'GCATCGCAGAGAGTATACAGTACGGCAGAGAG'
algorithm = Naive(T)
print (algorithm.match(P))