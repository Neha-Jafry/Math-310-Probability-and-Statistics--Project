import random
import numpy as np
import matplotlib.pyplot as plt
from numpy.random import uniform
from math import comb


def path(start, data):
    path = [start]
    curr = start
    avg_dist = 0
    for i in data:
        curr += i
        avg_dist += i
        path.append(curr+i)
    print(avg_dist)
    return path


sample = [uniform(low=0.0, high=1.0)
          for _ in range(10000)]


path = path(0, sample)


plt.plot(path)
plt.show()
