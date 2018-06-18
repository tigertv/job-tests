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
print th1.getName()
'''
data = [1, 1, 1, 1, 0, 1,9,0,3,5,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,5,3,2,0,1,1,4,0, 1, 0, 1, 0, 1, 1, 1]

def myfunc(data, indexFrom, indexTo):
	for i in range(indexFrom, indexTo):
		if data[i]:  
			data[i] += data[i - 1] 

data2 = data[:]
data3 = data[:]
length = len(data)
middle = length/2
print 'middle='+str(middle)
print 'length='+str(length)

print time.ctime()
myfunc(data2, 1, middle)
myfunc(data2, middle, length)
print time.ctime()

#myfunc(data3, middle, length)
#myfunc(data3, 1, middle)


th1 = th.Thread(name='th-1', target=myfunc, args=(data3, 1, middle) )
th2 = th.Thread(name='th-2', target=myfunc, args=(data3, middle, length) )
th2.start()
th1.start()
print 'dddd'

print time.ctime()
'''
for i in range(1, length):
    if data[i]:  
	        data[i] += data[i - 1] 
'''

print data
print data2
print data3
#print time.ctime()
