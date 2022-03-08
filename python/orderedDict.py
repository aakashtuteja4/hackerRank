# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 19:32:41 2022
@author: Aakash Tuteja
"""
# Initalise a Default Dict
from collections import OrderedDict
d = OrderedDict()

# Read inputs into Dict
m = int(input())

# create dictionary
for i in range(m):
    temp = input().split(' ')
    num = int(temp[-1])
    del temp[-1]
    key = ' '.join(temp)
    try:
        num += d[key]
        d[key] = num
    except:
        d[key] = num

# Print the output
for a in d:
    print('{} {}'.format(a, d[a]))
