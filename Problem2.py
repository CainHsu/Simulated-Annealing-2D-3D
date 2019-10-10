from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import math
import random

from matplotlib import animation

x = np.linspace(-10, 10, 10000)
y = x**2
plt.plot(x, y)
plt.show()


# return 1: accept the current answer, 0 deny.

def Judge(deltaE, T):
    # accept when new answer is smaller
    if deltaE < 0:
        return 1
    # if new answer is bigger, accept new answer when the probablity is appropriate
    # as the T becomes smaller, it is harder and harder to accept bigger answer
    else:
        probability = math.exp(-deltaE/T)
        if probability > random.random():
            return 1
        else:
            return 0


# add random disturbance
def Disturbance(low, high, x_old):
    if random.random() > 0.5:
        x_new = x_old + (high - x_old) * random.random()*0.001
    else:
        x_new = x_old - (x_old - low) * random.random()*0.001
    return x_new


# target func
def ObjFun(fun_x):
    fun_y = fun_x**2
    return fun_y


low = -10
high = 10
tmp = 1e5
tmp_min = 1e-5
alpha = 0.99


# initialization
x_old = (high-low) * random.random() + low
x_new = x_old
value_old = ObjFun(x_old)
value_new = value_old

counter = 0
record_x = []
record_y = []
while(tmp > tmp_min and counter <= 10000):
    x_new = Disturbance(low, high, x_old)
    value_new = ObjFun(x_new)
    deltaE = value_new - value_old
    if Judge(deltaE, tmp) == 1:
        value_old = value_new
        record_x.append(x_new)
        record_y.append(value_new)
        x_old = x_new
    if deltaE < 0:
        tmp = tmp*alpha
    else:
        counter += 1


length = len(record_x)
index = [i+1 for i in range(length)]
plt.plot(index, record_y)
plt.plot(index, record_x)

plt.show()
print "The answer is:",record_x[-1]
