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

	for i in range(1000,n+1):
		if (primeList[i]):
			prime_list.append(i)
			
	return prime_list

def calculate_permutations(mystr):
    if len(mystr) <= 1:
        return [mystr]
    else:
        perms_list = []
        for x in calculate_permutations(mystr[:-1]):
            for i in range(len(x)+1):
                perms_list.append(x[:i] + mystr[-1] + x[i:])
        return perms_list

def check(myList):
	for i in range(len(myList)):
		for j in range(i+1,len(myList)):
			diff_=myList[j]-myList[i]
			if myList[j]+diff_ in myList:
				return(str(myList[i])+str(myList[j])+str(myList[j]+diff_))

def main():
	primes=seive(10000)
	primes_=[x for x in primes if x>1487 ]
	#print(primes_)
	for i in primes:
		permList=calculate_permutations(str(i))
		permList_=list(set([int(x) for x in permList if int(x) in primes_]))
		permList_.sort()
		#print(permList_)
		if len(permList_)>=3:
			if check(permList_):
				print(check(permList_))
				break

if __name__ == '__main__':
	main()
		
		
