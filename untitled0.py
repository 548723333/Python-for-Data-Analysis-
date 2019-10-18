# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 10:59:13 2019

@author: Hwayne
"""
import matplotlib.pyplot as plt

data=[2.26,1.98,1.79,1.54,1.56,1.58,1.55,1.47,1.45,1.44,1.43,1.41,1.39,1.42,1.40,1.38,1.37,1.33,1.31,1.30,1.28,1.29,1.25,1.24,1.24,1.24,1.24,1.24,1.24,1.24]
plt.hist(data)
plt.title("Histogram")
plt.xlabel("Value")
plt.ylabel("Frequenc")

