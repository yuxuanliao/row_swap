# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 17:57:58 2022

@author: yxliao
"""

import numpy as np
A = np.arange(25).reshape(5,5)
b = A[[0,4],:]
C = A[[4,0],:]
A[[0,4],:] = C
A[[4,0],:] = b
print(A)

