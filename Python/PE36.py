import itertools
import math
import time

start=time.time()
def isPrime(num):
	sqrt=int(math.sqrt(num))+1
	for x in range(3,sqrt):
		if num%x==0:
			print(f"{num}--->{x}")
			return False
	return True

perm_=itertools.permutations('1234567',7)
new_array=[]
for x in perm_:
	num_=''.join(x)
	primeCheck=isPrime(int(num_))
	#print(primeCheck)
	if primeCheck is True and num_[:3]=='765':
		new_array.append(int(num_))
print("Answer is:",new_array[-1])
print(f'Execution Time: {time.time()-start}')