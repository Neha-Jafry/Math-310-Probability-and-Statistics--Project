import random
import math
import numpy as np
import matplotlib.pyplot as plt
from numpy.random import choice
from math import comb


def point_of_intersection(x, y, dx, dy):
    m = (y-dy)/(x-dx)
    c = y - (m*x)
    newX1 = ((-2*m*c) + math.sqrt((2*m*c)**2 -
                                  (4*((m**2) + 1)*((c**2)-(100**2)))))/(2*((m**2)+1))
    newY1 = (m*newX1) + c
    newX2 = -newX1
    newY2 = -newY1
    return (newX1, newY1, newX2, newY2)


def path(start, step, angle):
    path = [start]
    x = 0
    y = 0
    curr = (x, y)
    for i in range(len(step)):
        dx = step[i] * math.cos(math.radians(angle[i]))
        dy = step[i] * math.sin(math.radians(angle[i]))
        x += dx
        y += dy
        if math.sqrt(x**2 + y**2) > 100:
            x = x-dx
            y = y-dy
            newX1, newY1, newX2, newY2 = point_of_intersection(
                x, y, dx, dy)
            d1 = math.sqrt(((x-newX1)**2) + ((y-newY1)**2))
            d2 = math.sqrt(((x-newX2)**2) + ((y-newY2)**2))
            if d2 > d1:
                path.append([newX1, newY1])
                a, b = zip(*path)
                plt.plot(a, b)
                path = []
                x = -newX1
                y = -newY1
            else:
                path.append([newX2, newY2])
                a, b = zip(*path)
                plt.plot(a, b)
                path = []
                x = -newX1
                y = -newY1
        curr = [x, y]
        path.append(curr)

    a, b = zip(*path)
    plt.plot(a, b)
    plt.axis([-150, 150, -150, 150])
    plt.show()


step_sample = [choice([0, 0.5, 1]) for _ in range(10000)]
angle_sample = [choice(range(0, 360)) for _ in range(10000)]

path([0, 0], step_sample, angle_sample)
