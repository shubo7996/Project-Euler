def seive(n):
	primeList=[True]*(n+1)
	prime_list=[]
	p=2
	while(p*p<=n):
		if primeList[p] is True:
			i=p*2
			while (i<=n):
				primeList[i]=False
				i=i+p
		p+=1

	for i in range(2,n+1):
		if (primeList[i]):
			prime_list.append(i)

	return prime_list

def is_prime(n):
	for i in range(2,n+1):
		if n%i==0:
			return False
	return True

primes1000=seive(1000)
print("Primes Numbers in range of 1000: {}".format(primes1000))
duplicatePrimes=primes1000[:]
#print(duplicatePrimes)
largest=0


for b in primes1000:
	for a in primes1000:
		i=0
		while True:
			quadraticEqn=i**2 + a*i + b #n^2+an+b
			print("Quadratic Equations are: {}".format(quadraticEqn))
			if quadraticEqn not in duplicatePrimes:
				if is_prime(quadraticEqn):
					duplicatePrimes.append(quadraticEqn)
				else:
					if (i-1)>largest:
						largest=(i-1)
						prod=a*b
					break
			i+=1
		i=0
		while True:
			quadraticEqn=i**2 - a*i + b
			print("Quadratic Equations are: {}".format(quadraticEqn))
			if quadraticEqn not in duplicatePrimes:
				if is_prime(quadraticEqn) and quadraticEqn>0 :
					duplicatePrimes.append(quadraticEqn)
				else:
					if (i-1)>largest:
						largest=(i-1)
						prod=-1*a*b
					break
			i+=1

print("Highest Product"prod)