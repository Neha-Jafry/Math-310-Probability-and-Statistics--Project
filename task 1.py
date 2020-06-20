import random 
import numpy as np 
import matplotlib.pyplot as plt
from numpy.random import choice
from math import comb
  

def path(start, data):
    path=[start]
    curr=start
    avg_dist=0
    for i in data:
        curr+=i
        avg_dist+=i
        path.append(curr+i)
    print(abs(avg_dist))
    return path





probs=[0.5, 0.5]
sample=[choice([-1,1], p=probs)
        for _ in range(10000)]

expectation=(0.4*(-1)+0.6)*1000
path= path(2,sample)
plt.plot(path)
plt.show()
