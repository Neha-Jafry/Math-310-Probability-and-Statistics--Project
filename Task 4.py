from numpy.random import uniform
import matplotlib.pyplot as plt
import scipy.stats
import numpy as np
import random 
from math import comb
  
class RandomWalk:
    def __init__(self, start, noOfSteps):
        self.start = start
        self.steps=uniform(low=0, high=1, size=noOfSteps)
        self.path=[start]
        self.dist=[0]
        self.curr=start
        for i in self.steps:
            self.curr+=i
            self.path.append(self.curr)
            self.dist.append(self.curr-self.start)
            
    def pathPlot(self):
        p=plt.plot(self.path)
        return p

    def distancePlot(self):
        p=plt.hist(self.dist)
        return p

    def distance(self):
        return self.curr

def avg_dist():
    avg=0
    for i in range(1000):
        walk = RandomWalk(2, 1000)
        avg += walk.distance()
    return avg/1000

# print average distance
print(avg_dist())

# plots
# scenario 1: starting point 2
walk = RandomWalk(2, 100)
p1 = walk.pathPlot()
# scenario 2: starting point 100
walk = RandomWalk(10, 100)
p2 = walk.pathPlot()
plt.xlabel('Step Number')
plt.ylabel('Distance from Start')
plt.legend(['p1','p2'])
plt.show()

# scenario 1: starting point 2
# walk = RandomWalk(2, 100)
# p1 = walk.distancePlot()
# plt.xlabel('Distance from Start')
# plt.ylabel('frequency')
# plt.title('Scenario 1')
# plt.show()
# # scenario 2: starting point 100
# walk = RandomWalk(10, 100)
# p2 = walk.distancePlot()
# plt.xlabel('Distance from Start')
# plt.ylabel('frequency')
# plt.title('Scenario 2')
# plt.show()
