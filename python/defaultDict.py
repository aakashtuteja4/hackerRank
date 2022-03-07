# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 23:03:41 2022
@author: Aakash Tuteja
"""
# Initalise a Default Dict
from collections import defaultdict
d = defaultdict(list)

# Read inputs into Dict
m, n = map(int, input().split())
for i in range(m+n):
    temp = input()
    if i < m:
        d['A'].append(temp)
    else:
        d['B'].append(temp)

# iterate over both keys
for val in d['B']:
    string = ''
    for key, value in enumerate(d['A']):
        if val == value:
            string += str(key+1) + ' '
    if len(string)>=1:
        print(string[:-1])
    else:
        print('-1')

