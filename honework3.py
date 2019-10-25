# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 19:02:11 2019

@author: Hwayne
"""

import numpy as np
import matplotlib.pyplot as plt
import math

x=np.linspace(0,2*math.pi,1000)
y1=np.cos(x)*2+3
y2=(np.sin(x)**2)*5


plt.figure(figsize=(8,4))


plt.plot(x, y1, label = '2CosX+3', color = 'blue', linewidth = 2 )
plt.plot(x, y2, label = '5(SinX^2)',color = 'red', linewidth = 4)

plt.title=('homework3')
plt.xlabel=('Time(s)')
plt.ylabel=('Concussion')



plt.ylim(-2 , 6)
plt.legend()
plt.show()