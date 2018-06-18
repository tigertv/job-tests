#!/usr/bin/python
import threading as th
import time

def loop1_10():
	for i in range(1, 11):
		#time.sleep(1)
		print i

class myCl:
	@staticmethod
	def func():
		print 'it\'s a function'

a = myCl()
th1 = th.Thread(name='th-1', target=myCl.func())
th1.start()
'''
th2 = th.Thread(name='th-2', target=loop1_10)
th2.start()
th3 = th.Thread(name='th-3', target=loop1_10)
th3.start()
'''


print th1.getName()
