'''
	Solution@SubhamoyPaul
'''

import math
import time

start=time.perf_counter()

def sieve(x):
	primeList=[True]*(x+1)
	p=2
	while(p*p<=x):
		if primeList[p]==True:
			i=p*2
			while(i<=x):
				primeList[i]=False
				i+=p
		p+=1

	prime_numbers=[]
	for num in range(2,x+1):
		if (primeList[num]):
			prime_numbers.append(num)

	return prime_numbers

prime_sq=sieve(int(int(5E7)**(1/2)))
prime_thrd=sieve(int(int(5E7)**(1/3)))
prime_frth=sieve(int(int(5E7)**(1/4)))
power_sum=set()
for x in prime_sq:
	for y in prime_thrd:
		for z in prime_frth:
			prod_sum=x**2+y**3+z**4
			if prod_sum>5E7:
				break
			power_sum.add(prod_sum)
print(f"Result: {len(power_sum)}")
print(f"Time Elapsed: {time.perf_counter()-start}")