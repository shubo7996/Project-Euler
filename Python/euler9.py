"""Fibonacci Method"""

'''
import math

lists=[]
for x in range(1,1000):
	if x%2==1:
		lists.append(x)
#print(lists)

for i in lists:
	a2,b2,c2=1,0,0
	if i*i in lists and i*i%2==1:
		a2=int(i)*int(i)
		#print(a2)
		term=(a2+1)//2
		#print("{} is {}th term".format(a2,term))
		b2=pow(len(lists[:term-1]),2)
		#print(b2)
		c2=pow(len(lists[:term]),2)
		#print(c2)
		if (a2+b2==c2):
			#print(int(math.sqrt(a2)),int(math.sqrt(b2)),int(math.sqrt(c2)))
			if int(math.sqrt(a2))+int(math.sqrt(b2))+int(math.sqrt(c2))==1000:
				print(int(math.sqrt(a2))*int(math.sqrt(b2))*int(math.sqrt(c2)))
'''

import time

start = time.perf_counter()

for num in range(1, 1000):
    for dig in range(num, 1000 - num):
        i = 1000 - num - dig
        if num*num + dig*dig == i*i:
            print(num, dig, i)
            print("Product: {}".format(num * dig * i))
               
print("Time Elapsed: {}".format(time.perf_counter() - start))