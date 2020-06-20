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
    avg_dist=0
    while curr2-curr1 !=0:
        p=[choice([-1,1], p=[0.5, 0.5]), choice([-1,1], p=[0.5, 0.5])]
        curr1+=p[0]
        curr2+=p[1]
        path1.append(curr1)
        path2.append(curr2)
        avg_dist+=(curr2-curr1)
        i+=1
    return path1, path2, i-1

s_path=path(1, 5)
plt.plot(s_path[0])
plt.plot(s_path[1])
plt.show()

avg=0
for _ in range(100):
    avg+=(path(1, 5)[2]/100)
# avg/=100
print(avg)