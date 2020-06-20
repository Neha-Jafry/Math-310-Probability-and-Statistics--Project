import random
import math
import numpy as np
import matplotlib.pyplot as plt
from numpy.random import choice
from numpy.random import uniform
from math import comb


def starting_point():
    r = uniform(low=0, high=100)
    angle = uniform(low=0, high=2*math.pi)
    return (r*math.cos(angle), r*math.sin(angle))

def point_of_intersection(x, y, dx, dy):
    m = (y-dy)/(x-dx)
    c = y - (m*x)
    newX1 = ((-2*m*c) + math.sqrt((2*m*c)**2 -
                                  (4*((m**2) + 1)*((c**2)-(100**2)))))/(2*((m**2)+1))
    newY1 = (m*newX1) + c
    newX2 = -newX1
    newY2 = -newY1
    return (newX1, newY1, newX2, newY2)

def forAverage(start1, start2):
    i=0
    x1, y1, x2, y2 = start1[0],start1[1],start2[0],start2[1]
    while math.sqrt((x2-x1)**2+(y2-y1)**2)>1:
        angle1 = uniform(low=0, high=2*math.pi)
        angle2 = uniform(low=0, high=2*math.pi)
        step1 = uniform(low=0, high=1)
        step2 = uniform(low=0, high=1)
        dx1 = step1 * math.cos(angle1)
        dy1 = step1 * math.sin(angle1)
        x1 += dx1
        y1 += dy1
        dx2 = step2 * math.cos(angle2)
        dy2 = step2 * math.sin(angle2)
        x2 += dx2
        y2 += dy2
        if math.sqrt(x1**2 + y1**2) > 100:
            x1 -= dx1
            y1 -= dy1
            newX1, newY1, newX2, newY2 = point_of_intersection(
                x1, y1, dx1, dy1)
            d1 = math.sqrt(((x1-newX1)**2) + ((y1-newY1)**2))
            d2 = math.sqrt(((x1-newX2)**2) + ((y1-newY2)**2))
            if d2 > d1:
                x1 = -newX1
                y1 = -newY1
            else:
                x1 = -newX1
                y1 = -newY1
        if math.sqrt(x2**2 + y2**2) > 100:
            x2 -= dx2
            y2 -= dy2
            newX1, newY1, newX2, newY2 = point_of_intersection(
                x2, y2, dx2, dy2)
            d1 = math.sqrt(((x2-newX1)**2) + ((y2-newY1)**2))
            d2 = math.sqrt(((x2-newX2)**2) + ((y2-newY2)**2))
            if d2 > d1:
                x2 = -newX1
                y2 = -newY1
            else:
                x2 = -newX1
                y2 = -newY1
        i+=1
    return i

def walkPath(start1, start2):
    path1=[]
    path2=[]
    i=0
    x1, y1, x2, y2 = start1[0],start1[1],start2[0],start2[1]
    while math.sqrt((x2-x1)**2+(y2-y1)**2)>1:
        angle1 = uniform(low=0, high=2*math.pi)
        angle2 = uniform(low=0, high=2*math.pi)
        step1 = uniform(low=0, high=1)
        step2 = uniform(low=0, high=1)
        dx1 = step1 * math.cos(angle1)
        dy1 = step1 * math.sin(angle1)
        x1 += dx1
        y1 += dy1
        dx2 = step2 * math.cos(angle2)
        dy2 = step2 * math.sin(angle2)
        x2 += dx2
        y2 += dy2
        if math.sqrt(x1**2 + y1**2) > 100:
            x1 -= dx1
            y1 -= dy1
            newX1, newY1, newX2, newY2 = point_of_intersection(
                x1, y1, dx1, dy1)
            d1 = math.sqrt(((x1-newX1)**2) + ((y1-newY1)**2))
            d2 = math.sqrt(((x1-newX2)**2) + ((y1-newY2)**2))
            if d2 > d1:
                path1.append([newX1, newY1])
                a, b = zip(*path1)
                plt.plot(a, b, color='blue')
                path1 = []
                x1 = -newX1
                y1 = -newY1
            else:
                path1.append([newX2, newY2])
                a, b = zip(*path1)
                plt.plot(a, b, color='blue')
                path1 = []
                x1 = -newX1
                y1 = -newY1
            path1.append([x1, y1])
            path2.append([x2, y2])
        if math.sqrt(x2**2 + y2**2) > 100:
            x2 -= dx2
            y2 -= dy2
            newX1, newY1, newX2, newY2 = point_of_intersection(
                x2, y2, dx2, dy2)
            d1 = math.sqrt(((x2-newX1)**2) + ((y2-newY1)**2))
            d2 = math.sqrt(((x2-newX2)**2) + ((y2-newY2)**2))
            if d2 > d1:
                path2.append([newX1, newY1])
                a, b = zip(*path2)
                plt.plot(a, b, color='orange')
                path2 = []
                x2 = -newX1
                y2 = -newY1
            else:
                path2.append([newX2, newY2])
                a, b = zip(*path2)
                plt.plot(a, b, color='orange')
                path2 = []
                x2 = -newX1
                y2 = -newY1
            path1.append([x1, y1])
            path2.append([x2, y2])
        i+=1
    a, b = zip(*path1)
    c, d = zip(*path2)
    plt.plot(a, b, color='blue')
    plt.plot(c, d, color='orange')
    plt.axis([-110, 110, -110, 110])
    plt.show()

s1= starting_point()
s2= starting_point()
walkPath(s1, s2)

s1 = starting_point()
s2 = starting_point()
lst=[]
for i in range(100):
    lst.append(forAverage(s1, s2))
plt.hist(lst)
plt.show()