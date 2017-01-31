#!usr/bin/env python

# Derek Bean
# ME 599 
# 1/31/2017

# Plot a sine wave from 0 to 4 pi to match the example given in the lab instructions

import math 
import matplotlib.pyplot as plt
import numpy as np

x_val = np.linspace(0, 4*math.pi, num=100)

y_val = [math.sin(x) for x in x_val]

plt.figure(1)
plt.plot(x_val, y_val, 'b-')
plt.xlabel('x')
plt.ylabel('x')
plt.axis([0, 4*math.pi, -1, 1])
plt.title('A sine curve')
plt.show()
