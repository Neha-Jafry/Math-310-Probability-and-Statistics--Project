import random 
import numpy as np 
import matplotlib.pyplot as plt
from numpy.random import choice
from math import comb
  
    
def path(start1, start2):
    curr1=start1
    curr2=start2
    i=0
    path1=[start1]
    path2=[start2]
    while curr2-curr1 !=0:
        p=[choice([-1,1], p=[0.5, 0.5]), choice([-1,1], p=[0.5, 0.5])]
        curr1+=p[0]
        curr2+=p[1]
        path1.append(curr1)
        path2.append(curr2)
        i+=1
    return path1, path2, i-1

s_path=path(1, 5)
plt.plot(s_path[0])
plt.plot(s_path[1])
plt.show()

n=[]
for _ in range(100):
    n.append(path(1, 5)[2])
plt.hist(n)
plt.show()

print(n)
m=[]
for i in n:
    if i < 500:
        m.append(i)
plt.hist(m)
plt.show()
