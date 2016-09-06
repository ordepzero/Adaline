# -*- coding: utf-8 -*-
"""
Created on Sun Aug 28 21:09:11 2016

@author: PeDeNRiQue
"""

m = [[0.2, 0.4, 0.5],[0.3, 0.6, 0.7], [0.4, 0.8, 0.3]]
c = [-1, 0.3, 0.7]

m = np.array(m)
c = np.array(c)
r = m * c
print(r)
print(np.sum(r,axis=0).tolist())