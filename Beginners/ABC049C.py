# -*- coding: utf-8 -*-
import itertools

S = str(input())

S = S.replace('dream', 'A')
S = S.replace('erase', 'B')
S = S.replace('Aer', '')
S = S.replace('Br', '')
S = S.replace('A', '')
S = S.replace('B', '')

if S != "":
    print("NO")
else:
    print("YES")
