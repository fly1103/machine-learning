#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import kNN
datingDataMat,datingLabels = kNN.file2matrix('datingTestSet2.txt')

import matplotlib
import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(datingDataMat[:,1],datingDataMat[:,2])
plt.show()