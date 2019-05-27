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

def calc_sum(listOfPrime):	
	consq_prime_length=0
	consq_prime_sum=0
	lastj=len(listOfPrime)

	for i in range(len(listOfPrime)):
		for j in range(i+consq_prime_length,lastj):
			soln=sum(listOfPrime[i:j])
	
			if soln<1000000:
				if soln in listOfPrime:
					consq_prime_length=j-i
					consq_prime_sum=soln
			else:
				lastj=j+1
				break

	return consq_prime_sum


		
if __name__=='__main__':
	n=1000000
	primeList_=seive(n)
	print(primeList_)
	sum_=calc_sum(primeList_)
	print("Sum of Prime Numbers: {}".format(sum_))