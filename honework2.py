# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 10:55:15 2019

@author: Hwayne
"""

import matplotlib.pyplot as plt
import numpy as np

data=np.random.normal(0,1000, 1000)

plt.hist(data)

plt.title("Histogram")
plt.xlabel("Value")
plt.ylabel("Frequenc")
