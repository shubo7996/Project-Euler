import time

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

def main():
	primes_=seive(1000)
	target=2
	while True:
		ways_=[1]+[0]*target
		for x in range(0,len(primes_)):
			for y in range(primes_[x],target+1):
				ways_[y]=ways_[y]+ways_[y-primes_[x]]

		if ways_[target]>5000:
			break
		target+=1
	print(f"First Value which can be written as the sum of primes in over five thousand different ways: {target}")

if __name__ == '__main__':
	start=time.perf_counter()
	main()
	print(f"Time Elapsed: {time.perf_counter()-start}")
