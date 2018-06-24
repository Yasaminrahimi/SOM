import math
import random
import sys
import numpy as np

A1 = [0, 0, 1, 1, 0, 0, 0, 
      0, 0, 0, 1, 0, 0, 0, 
      0, 0, 0, 1, 0, 0, 0, 
      0, 0, 1, 0, 1, 0, 0, 
      0, 0, 1, 0, 1, 0, 0, 
      0, 1, 1, 1, 1, 1, 0, 
      0, 1, 0, 0, 0, 1, 0, 
      0, 1, 0, 0, 0, 1, 0, 
      1, 1, 1, 0, 1, 1, 1]

B1 = [1, 1, 1, 1, 1, 1, 0, 
      0, 1, 0, 0, 0, 0, 1, 
      0, 1, 0, 0, 0, 0, 1, 
      0, 1, 0, 0, 0, 0, 1, 
      0, 1, 1, 1, 1, 1, 0, 
      0, 1, 0, 0, 0, 0, 1, 
      0, 1, 0, 0, 0, 0, 1, 
      0, 1, 0, 0, 0, 0, 1, 
      1, 1, 1, 1, 1, 1, 0]

C1 = [0, 0, 1, 1, 1, 1, 1, 
      0, 1, 0, 0, 0, 0, 1, 
      1, 0, 0, 0, 0, 0, 0, 
      1, 0, 0, 0, 0, 0, 0, 
      1, 0, 0, 0, 0, 0, 0, 
      1, 0, 0, 0, 0, 0, 0, 
      1, 0, 0, 0, 0, 0, 0, 
      0, 1, 0, 0, 0, 0, 1, 
      0, 0, 1, 1, 1, 1, 0]

D1 = [1, 1, 1, 1, 1, 0, 0, 
      0, 1, 0, 0, 0, 1, 0, 
      0, 1, 0, 0, 0, 0, 1, 
      0, 1, 0, 0, 0, 0, 1, 
      0, 1, 0, 0, 0, 0, 1, 
      0, 1, 0, 0, 0, 0, 1, 
      0, 1, 0, 0, 0, 0, 1, 
      0, 1, 0, 0, 0, 1, 0, 
      1, 1, 1, 1, 1, 0, 0]

E1 = [1, 1, 1, 1, 1, 1, 1, 
      0, 1, 0, 0, 0, 0, 1, 
      0, 1, 0, 0, 0, 0, 0, 
      0, 1, 0, 1, 0, 0, 0, 
      0, 1, 1, 1, 0, 0, 0, 
      0, 1, 0, 1, 0, 0, 0, 
      0, 1, 0, 0, 0, 0, 0, 
      0, 1, 0, 0, 0, 0, 1, 
      1, 1, 1, 1, 1, 1, 1]

J1 = [0, 0, 0, 1, 1, 1, 1, 
      0, 0, 0, 0, 0, 1, 0, 
      0, 0, 0, 0, 0, 1, 0, 
      0, 0, 0, 0, 0, 1, 0, 
      0, 0, 0, 0, 0, 1, 0, 
      0, 0, 0, 0, 0, 1, 0, 
      0, 1, 0, 0, 0, 1, 0, 
      0, 1, 0, 0, 0, 1, 0, 
      0, 0, 1, 1, 1, 0, 0]

K1 = [1, 1, 1, 0, 0, 1, 1, 
      0, 1, 0, 0, 1, 0, 0, 
      0, 1, 0, 1, 0, 0, 0, 
      0, 1, 1, 0, 0, 0, 0, 
      0, 1, 1, 0, 0, 0, 0, 
      0, 1, 0, 1, 0, 0, 0, 
      0, 1, 0, 0, 1, 0, 0, 
      0, 1, 0, 0, 0, 1, 0, 
      1, 1, 1, 0, 0, 1, 1]

A2 = [0, 0, 0, 1, 0, 0, 0, 
      0, 0, 0, 1, 0, 0, 0, 
      0, 0, 0, 1, 0, 0, 0, 
      0, 0, 1, 0, 1, 0, 0, 
      0, 0, 1, 0, 1, 0, 0, 
      0, 1, 0, 0, 0, 1, 0, 
      0, 1, 1, 1, 1, 1, 0, 
      0, 1, 0, 0, 0, 1, 0, 
      0, 1, 0, 0, 0, 1, 0]

B2 = [1, 1, 1, 1, 1, 1, 0, 
      1, 0, 0, 0, 0, 0, 1, 
      1, 0, 0, 0, 0, 0, 1, 
      1, 0, 0, 0, 0, 0, 1, 
      1, 1, 1, 1, 1, 1, 0, 
      1, 0, 0, 0, 0, 0, 1, 
      1, 0, 0, 0, 0, 0, 1, 
      1, 0, 0, 0, 0, 0, 1, 
      1, 1, 1, 1, 1, 1, 0]

C2 = [0, 0, 1, 1, 1, 0, 0, 
      0, 1, 0, 0, 0, 1, 0, 
      1, 0, 0, 0, 0, 0, 1, 
      1, 0, 0, 0, 0, 0, 0, 
      1, 0, 0, 0, 0, 0, 0, 
      1, 0, 0, 0, 0, 0, 0, 
      1, 0, 0, 0, 0, 0, 1, 
      0, 1, 0, 0, 0, 1, 0, 
      0, 0, 1, 1, 1, 0, 0]

D2 = [1, 1, 1, 1, 1, 0, 0, 
      1, 0, 0, 0, 0, 1, 0, 
      1, 0, 0, 0, 0, 0, 1, 
      1, 0, 0, 0, 0, 0, 1, 
      1, 0, 0, 0, 0, 0, 1, 
      1, 0, 0, 0, 0, 0, 1, 
      1, 0, 0, 0, 0, 0, 1, 
      1, 0, 0, 0, 0, 1, 0, 
      1, 1, 1, 1, 1, 0, 0]

E2 = [1, 1, 1, 1, 1, 1, 1, 
      1, 0, 0, 0, 0, 0, 0, 
      1, 0, 0, 0, 0, 0, 0, 
      1, 0, 0, 0, 0, 0, 0, 
      1, 1, 1, 1, 1, 0, 0, 
      1, 0, 0, 0, 0, 0, 0, 
      1, 0, 0, 0, 0, 0, 0, 
      1, 0, 0, 0, 0, 0, 0, 
      1, 1, 1, 1, 1, 1, 1]

J2 = [0, 0, 0, 0, 0, 1, 0, 
      0, 0, 0, 0, 0, 1, 0, 
      0, 0, 0, 0, 0, 1, 0, 
      0, 0, 0, 0, 0, 1, 0, 
      0, 0, 0, 0, 0, 1, 0, 
      0, 0, 0, 0, 0, 1, 0, 
      0, 1, 0, 0, 0, 1, 0, 
      0, 1, 0, 0, 0, 1, 0, 
      0, 0, 1, 1, 1, 0, 0]

K2 = [1, 0, 0, 0, 0, 1, 0, 
      1, 0, 0, 0, 1, 0, 0, 
      1, 0, 0, 1, 0, 0, 0, 
      1, 0, 1, 0, 0, 0, 0, 
      1, 1, 0, 0, 0, 0, 0, 
      1, 0, 1, 0, 0, 0, 0, 
      1, 0, 0, 1, 0, 0, 0, 
      1, 0, 0, 0, 1, 0, 0, 
      1, 0, 0, 0, 0, 1, 0]

A3 = [0, 0, 0, 1, 0, 0, 0, 
      0, 0, 0, 1, 0, 0, 0, 
      0, 0, 1, 0, 1, 0, 0, 
      0, 0, 1, 0, 1, 0, 0, 
      0, 1, 0, 0, 0, 1, 0, 
      0, 1, 1, 1, 1, 1, 0, 
      1, 0, 0, 0, 0, 0, 1, 
      1, 0, 0, 0, 0, 0, 1, 
      1, 1, 0, 0, 0, 1, 1]

B3 = [1, 1, 1, 1, 1, 1, 0, 
      0, 1, 0, 0, 0, 0, 1, 
      0, 1, 0, 0, 0, 0, 1, 
      0, 1, 1, 1, 1, 1, 0, 
      0, 1, 0, 0, 0, 0, 1, 
      0, 1, 0, 0, 0, 0, 1, 
      0, 1, 0, 0, 0, 0, 1, 
      0, 1, 0, 0, 0, 0, 1, 
      1, 1, 1, 1, 1, 1, 0]

C3 = [0, 0, 1, 1, 1, 0, 1, 
      0, 1, 0, 0, 0, 1, 1, 
      1, 0, 0, 0, 0, 0, 1, 
      1, 0, 0, 0, 0, 0, 0, 
      1, 0, 0, 0, 0, 0, 0, 
      1, 0, 0, 0, 0, 0, 0, 
      1, 0, 0, 0, 0, 0, 1, 
      0, 1, 0, 0, 0, 1, 0, 
      0, 0, 1, 1, 1, 0, 0]

D3 = [1, 1, 1, 1, 0, 0, 0, 
      0, 1, 0, 0, 1, 0, 0, 
      0, 1, 0, 0, 0, 1, 0, 
      0, 1, 0, 0, 0, 1, 0, 
      0, 1, 0, 0, 0, 1, 0, 
      0, 1, 0, 0, 0, 1, 0, 
      0, 1, 0, 0, 0, 1, 0, 
      0, 1, 0, 0, 1, 0, 0, 
      1, 1, 1, 1, 0, 0, 0]

E3 = [1, 1, 1, 1, 1, 1, 1, 
      0, 1, 0, 0, 0, 0, 1, 
      0, 1, 0, 0, 1, 0, 0, 
      0, 1, 1, 1, 1, 0, 0, 
      0, 1, 0, 0, 1, 0, 0, 
      0, 1, 0, 0, 0, 0, 0, 
      0, 1, 0, 0, 0, 0, 0, 
      0, 1, 0, 0, 0, 0, 1, 
      1, 1, 1, 1, 1, 1, 1]

J3 = [0, 0, 0, 0, 1, 1, 1, 
      0, 0, 0, 0, 0, 1, 0, 
      0, 0, 0, 0, 0, 1, 0, 
      0, 0, 0, 0, 0, 1, 0, 
      0, 0, 0, 0, 0, 1, 0, 
      0, 0, 0, 0, 0, 1, 0, 
      0, 0, 0, 0, 0, 1, 0, 
      0, 1, 0, 0, 0, 1, 0, 
      0, 0, 1, 1, 1, 0, 0]

K3 = [1, 1, 1, 0, 0, 1, 1, 
      0, 1, 0, 0, 0, 1, 0, 
      0, 1, 0, 0, 1, 0, 0, 
      0, 1, 0, 1, 0, 0, 0, 
      0, 1, 1, 0, 0, 0, 0, 
      0, 1, 0, 1, 0, 0, 0, 
      0, 1, 0, 0, 1, 0, 0, 
      0, 1, 0, 0, 0, 1, 0, 
      1, 1, 1, 0, 0, 1, 1]
clusters = []
sample = []
sample.append(A1)
sample.append(B1)
sample.append(C1)
sample.append(D1)
sample.append(E1)
sample.append(J1)
sample.append(K1)
sample.append(A2)
sample.append(B2)
sample.append(C2)
sample.append(D2)
sample.append(E2)
sample.append(J2)
sample.append(K2)
sample.append(A3)
sample.append(B3)
sample.append(C3)
sample.append(D3)
sample.append(E3)
sample.append(J3)
sample.append(K3)
minimum = np.zeros((21,))


"""def makecluster (clusters):
    for k in range (25):
        cluster = np.random.rand(63,)
        clusters.append(cluster)
    return clusters"""

def findmindis (clusters, sample, minimum):
    character = ["A1","B1","C1","D1","E1","J1","K1","A2","B2","C2","D2","E2","J2","K2","A3","B3","C3","D3","E3","J3","K3"]
    for k in range (25):
        cluster = np.random.rand(63,)
        clusters.append(cluster)
    Alpha = 0.6
    epoch = 0
    while epoch < 1000 :
        Alpha = Alpha*0.5
        distance = np.zeros((25,))
        subtract = np.zeros((63,), dtype=int)
        for i in range (21):
            for j in range (25):
                subtract =  np.subtract(sample[i], clusters[j])
                distance[j] = np.inner(subtract.transpose(),subtract)
            k = distance.argmin()
            minimum[i] = k
            subtract =  np.subtract(sample[i], clusters[k])
            clusters[k] = clusters[k] + Alpha*subtract
        epoch += 1
    for i in range (21):
        print ( str(character[i]) + " is belong to cluster " + str(minimum[i]) )
    return clusters

          


    
def main ():
    (findmindis(clusters, sample, minimum))
    
        
        

