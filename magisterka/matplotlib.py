#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 10:47:32 2020

@author: marcysio
"""


import numpy as np
from matplotlib import pyplot as plt
import pandas as pd

f = pd.read_csv('26.11.21/AlAlAl_siatka.csv', delimiter=',') 
                #skipinitialspace=(True), decimal=',')

time = f['timestamp']
temp = f['data']

# g = pd.read_csv('csv/1Pc_rozciaganie2.TRA', delimiter=';', skipinitialspace=(True), decimal=',')

# strain2 = g['Strain']
# force2 = g['Standard force']

# h = pd.read_csv('csv/1Pc_rozciaganie3.TRA', delimiter=';', skipinitialspace=(True), decimal=',')

# strain3 = h['Strain']
# force3 = h['Standard force']

t1 = time[0]
for t in time:
    if t < t1:
        t1 = t


tim = []
for t in time:
    t = t - t1
    t = t / 1000
    t = int(t)
    tim.append(t)

tem = []
for t in temp:
    t = t[21:-3]
    tem.append(t)
    

# t1 = tim[0]
# ti = []
# te = []
# n = 0
# while n < len(tim):
#     i = 0
#     j = 0
#     for t in tim:
#         if t1 > t:
#             j = i
#             t1 = t
#         i += 1

#     ti.append(tim[j])
#     te.append(tem[j])
#     tim.pop(j)
#     tem.pop(j)
    
#     n += 1



###
#matplotlib
###

# styling
# print{plt.style.available}
# plt.style.use(classic)

# plot point
plt.scatter(tim,tem, color='b',label='siatka')
#plt.plot(stra2,forc2, color='r',label='2 próba')
#plt.plot(stra3,forc3, color='g',label='3 próba')

#change label of xaxis
# plt.xticks(ticks=,labels=)

#plot labels
plt.xlabel('Time [s]')
plt.ylabel('Tepmerature [C]')
plt.title(label, kwargs)

#plot grid
plt.grid(True)

#plot legend (if labels are defined, else: (labelx,labely))
#plt.legend()

#make sure it looks good
plt.tight_layout()

#save plot to file
# plt.savefig('siatka.png')

#print plot
plt.show()
