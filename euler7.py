
"""
	#Problem 7:- Finding the 10001st Prime Number

"""

import time

def sumofPrimes(n):

	primeList=[True]*(n+1)

	p=2
	while (p*p<=n):
		#its a prime number if primeList[p] is False
		if primeList[p]==True:
			i=p*2
			while i<=n:
				primeList[i]=False
				i+=p
		p+=1

	counter=0
	for i in range(2,n+1):
		if (primeList[i]):
			counter+=1
			if counter==10001:
				print("10001st Prime Number is: {}".format(i))
				break


if __name__ == '__main__':
	start=time.perf_counter()
	n=1000000
	sumofPrimes(n)
	print(f"Time Elapsed: {time.perf_counter()-start}")

