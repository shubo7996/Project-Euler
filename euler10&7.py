"""
	#Problem 10- Programe to find the sum of all the primes below two million(Seive of Erastosthenes)

"""

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

	sum=0 
	for i in range(2,n+1):
		if (primeList[i]):
			sum+=i

"""
	#Problem 7:- Finding the 10001st Prime Number

"""
	counter=0
	for i in range(2,n+1):
		if (primeList[i]):
			counter+=1
			if counter==10001:
				print("10001st Prime Number is: {}".format(i))
				break

	
	return sum


if __name__ == '__main__':
	n=2000001
	sumVal=sumofPrimes(n)
	print("Sum of Prime Numbers in range of {} is: {}".format(n,sumVal))

