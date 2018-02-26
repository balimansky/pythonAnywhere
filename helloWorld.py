#! /usr/bin/python

import numpy as np
import matplotlib as mlp
import matplotlib.pyplot as plt
from scipy import linalg, optimize
from numpy import poly1d

p = poly1d([3,4,5])
print (p)
print (p.deriv()(4))
print (p(4))

#a = np.array([2,3,4])
#print (a)

# np.info(optimize.fmin)
