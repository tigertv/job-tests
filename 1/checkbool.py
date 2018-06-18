#!/usr/bin/python

import os
import sys
from functools import reduce

def fun(k,m):
	print k+m

fun('mmm',m='kkk')

def cheeseshop(kind, *arguments, **keywords):
	print("-- Do you have any", kind, "?")
	print("-- I'm sorry, we're all out of", kind)
	for arg in arguments:
		print(arg)
	print("-" * 40)
	for kw in keywords:
			print(kw, ":", keywords[kw])

cheeseshop('kind', 'sdfadd.', 'sdfasdaar', man='kia',woman='kaa')

a={'dad':'d'}
#a=[]
#a=None

if a:
	if 'ddad' in a:
		if a['ddad']:
			print 'a'
		else:
			print 'Not a'

c = [1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1]
b = reduce( lambda x, y: x + y, c)
#print b

y=0

def funct(x):
	global y
	y=x
	return x+1

d = list(map(funct, [1,2,3,4]))
print d
print y
	
'''
d = list(map((lambda x:
	x+x
	)
	, [1,2,3,4]))
print d
'''
