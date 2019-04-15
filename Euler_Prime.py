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

def isPrime(n):
    if (n <= 1):
    	return False
    if (n == 2):
    	return True
    if (n % 2 == 0):
    	return False
    if (n < 9):
    	return True
    if (n % 3 == 0):
    	return False
            
    counter = 5;            
    while((counter * counter) <= n):
        if (n % counter == 0):
        	return False
        if (n % (counter + 2) == 0):
        	return False;
        counter += 6
            

    return True