import random 
import numpy as np 
import matplotlib.pyplot as plt
from numpy.random import choice
from math import comb
  
class RandomWalk:
    def __init__(self, start, probs, noOfSteps, noMove=False):
        self.start = start
        if noMove:
            self.steps=[choice([-1, 0, 1], p=probs)
                for _ in range(noOfSteps)]   
        else:
            self.steps=[choice([-1,1], p=probs)
                for _ in range(noOfSteps)]
        self.path=[start]
        self.curr=self.start
        self.distCounter={}
        for i in self.steps:
            self.curr+=i
            self.path.append(self.curr)
            if self.curr not in self.distCounter:
                self.distCounter[self.curr]=1
            else:
                self.distCounter[self.curr]+=1
            
    def pathPlot(self):
        p=plt.plot(self.path)
        return p

    def distancePlot(self):
        p=plt.bar(list(self.distCounter.keys()), list(self.distCounter.values()))
        return p

    def distance(self):
        return self.curr

# plots

# scenario 1: starting point 2, uniform probabilities, step choice= [-1, 1]
walk = RandomWalk(2, [0.5, 0.5], 100)
p1 = walk.pathPlot()
# scenario 2: starting point 100, uniform probabilities, step choice= [-1, 1]
walk = RandomWalk(10, [0.5, 0.5], 100)
p2 = walk.pathPlot()
# scenario 3: starting point 100, uniform probabilities, step choice= [-1, 0, 1]
walk = RandomWalk(2, [0.33,0.34,0.33], 100, noMove=True)
p3 = walk.pathPlot()
# scenario 4: starting point 100, uniform probabilities, step choice= [-1, 0 1]
walk = RandomWalk(10, [0.33,0.34,0.33], 100, noMove=True)
p4 = walk.pathPlot()
# scenario 5: starting point 2, non-uniform probabilities, step choice= [-1, 1]
walk = RandomWalk(2, [0.2, 0.8], 100)
p5 = walk.pathPlot()
walk = RandomWalk(2, [0.7, 0.3], 100)
p6 = walk.pathPlot()
# scenario 5: starting point 2, non-uniform probabilities, step choice= [-1, 0, 1]
walk = RandomWalk(2, [0.2, 0.2, 0.6], 100, noMove=True)
p7 = walk.pathPlot()
walk = RandomWalk(2, [0.6, 0.2, 0.2], 100, noMove=True)
p8 = walk.pathPlot()
walk = RandomWalk(2, [0.2, 0.6, 0.2], 100, noMove=True)
p9 = walk.pathPlot()
plt.xlabel('Step Number')
plt.ylabel('Distance from Start')
plt.legend(['p1','p2','p3','p4','p5','p6','p7','p8','p9'])
plt.show()

# scenario 1: starting point 2, uniform probabilities, step choice= [-1, 1]
walk = RandomWalk(2, [0.5, 0.5], 1000)
p1 = walk.distancePlot()
plt.xlabel('Distance from Start')
plt.ylabel('frequency')
plt.show()
# scenario 2: starting point 100, uniform probabilities, step choice= [-1, 1]
walk = RandomWalk(10, [0.5, 0.5], 1000)
p2 = walk.distancePlot()
plt.xlabel('Distance from Start')
plt.ylabel('frequency')
plt.show()
# scenario 3: starting point 100, uniform probabilities, step choice= [-1, 0, 1]
walk = RandomWalk(2, [0.33,0.34,0.33], 1000, noMove=True)
p3 = walk.distancePlot()
plt.xlabel('Distance from Start')
plt.ylabel('frequency')
plt.show()
# scenario 4: starting point 100, uniform probabilities, step choice= [-1, 0 1]
walk = RandomWalk(10, [0.33,0.34,0.33], 1000, noMove=True)
p4 = walk.distancePlot()
plt.xlabel('Distance from Start')
plt.ylabel('frequency')
plt.show()
# scenario 5: starting point 2, non-uniform probabilities, step choice= [-1, 1]
walk = RandomWalk(2, [0.2, 0.8], 1000)
p5 = walk.distancePlot()
plt.xlabel('Distance from Start')
plt.ylabel('frequency')
plt.show()
walk = RandomWalk(2, [0.7, 0.3], 1000)
p6 = walk.distancePlot()
plt.xlabel('Distance from Start')
plt.ylabel('frequency')
plt.show()
# scenario 5: starting point 2, non-uniform probabilities, step choice= [-1, 0, 1]
walk = RandomWalk(2, [0.2, 0.2, 0.6], 1000, noMove=True)
p7 = walk.distancePlot()
plt.xlabel('Distance from Start')
plt.ylabel('frequency')
plt.show()
walk = RandomWalk(2, [0.6, 0.2, 0.2], 1000, noMove=True)
p8 = walk.distancePlot()
plt.xlabel('Distance from Start')
plt.ylabel('frequency')
plt.show()
walk = RandomWalk(2, [0.2, 0.6, 0.2], 1000, noMove=True)
p9 = walk.distancePlot()
plt.xlabel('Distance from Start')
plt.ylabel('frequency')
plt.show()

# average distance
def avg_dist(prob, noMove=False):
    avg=0
    for _ in range(1000):
        if noMove:
            walk = RandomWalk(2, prob, 1000, noMove)
        else:
            walk = RandomWalk(2, prob, 1000, noMove)
        avg += walk.distance()
    return avg/1000

# # uniform probabilities
# print(avg_dist([0.5, 0.5]))
# print(avg_dist([0.33, 0.34, 0.33], noMove=True))
# # non-uniform probabilities
# print(avg_dist([0.3, 0.7]))
# print(avg_dist([0.2, 0.2, 0.6], noMove=True))
