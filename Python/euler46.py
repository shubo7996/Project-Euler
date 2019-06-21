import itertools
def seive(n):
	primeList=[True]*(n+1)
	prime_list=[]
	composite_list=[]
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

	for x in range(1,n+1):
		if primeList[x] is False:
			composite_list.append(x)

	return(prime_list,composite_list)

def check(num_,primelist):
	k=1
	while(2*k*k)<num_:
		p=num_-2*k*k
		if p in primelist:
			return True
		k=k+1
	return False
		

prime_,compos_=seive(6000)
#print(prime_)
odd_compos=[]
for i in compos_:
	if i%2==1:
		odd_compos.append(i)

#print(odd_compos)
for x in odd_compos:
	if check(x,prime_) is False:
		print(x)
		break


