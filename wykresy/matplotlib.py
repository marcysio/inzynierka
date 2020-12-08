#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 10:47:32 2020

@author: marcysio
"""

import numpy as np
from matplotlib import pyplot as plt
import pandas as pd

f = pd.read_csv('csv/1Pc_rozciaganie1.TRA', delimiter=';', skipinitialspace=(True), decimal=',')

strain1 = f['Strain']
force1 = f['Standard force']

g = pd.read_csv('csv/1Pc_rozciaganie2.TRA', delimiter=';', skipinitialspace=(True), decimal=',')

strain2 = g['Strain']
force2 = g['Standard force']

h = pd.read_csv('csv/1Pc_rozciaganie3.TRA', delimiter=';', skipinitialspace=(True), decimal=',')

strain3 = h['Strain']
force3 = h['Standard force']

n = 0
s1 = 0
stra1 = []
forc1 = []
for s in strain1:
    if s1 < s and s < 5:
        stra1.append(s)
        forc1.append(force1[n])
        s1 = s
    n += 1

n = 0
s1 = 0
stra2 = []
forc2 = []
for s in strain2:
    if s1 < s and s < 5:
        stra2.append(s)
        forc2.append(force2[n])
        s1 = s
    n += 1

n = 0
s1 = 0
stra3 = []
forc3 = []
for s in strain3:
    if s1 < s and s < 5:
        stra3.append(s)
        forc3.append(force3[n])
        s1 = s
    n += 1



###
#matplotlib
###

#styling
#print{plt.style.available}
#plt.style.use(classic)

#plot line
plt.plot(stra1,forc1, color='b',label='1 próba')
plt.plot(stra2,forc2, color='r',label='2 próba')
plt.plot(stra3,forc3, color='g',label='3 próba')

#change label of xaxis
#plt.xticks(ticks=,labels=)

#plot labels
plt.xlabel('Wydłużenie [%]')
plt.ylabel('Siła [kN]')
#plt.title(label, kwargs)

#plot grid
plt.grid(True)

#plot legend (if labels are defined, else: (labelx,labely))
plt.legend()

#make sure it looks good
plt.tight_layout()

#save plot to file
#plt.savefig('plot.png')

#print plot
plt.show()