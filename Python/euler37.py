"""
	Problem 37- A Program to find out all the Truncatable Prime Numbers.
	A Truncatable Prime is a Prime Number which when stripped from eaither left or right 
	by 1 digit leaves a Prime number in every stage.
	for eg:- 3137
	from left:-3137,137,37,7(All are Prime)
	from right:-3137,313,31,3(All are Prime)

	@author-Subhamoy Paul

"""

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

def fromLeft(num,_primes_):
	counter=0
	if len(num)==1:
		return False
	for i in range(len(num)):
		if int(num[i:]) in _primes_:
			counter+=1
	if counter==len(num):
		return True

def fromRight(num,_primes_):
	counter=0
	if len(num)==1:
		return False
	for i in range(len(num),0,-1):
		if int(num[:i]) in _primes_:
			counter+=1
	if counter==len(num):
		return True

def main():
	primes=seive(1000000)
	#print(primes)
	_sum_=0
	count=0
	for i in primes:
		_left=fromLeft(str(i),primes)
		if _left is True:
			right_=fromRight(str(i),primes)
			if right_ is True:
				print("{} is a Truncatable Prime!".format(int(i)))
				count+=1
				_sum_+=int(i)
	print("Total Number of Truncatable Primes: {}".format(count))
	print("Total Sum of the Truncatable Primes: {}".format(_sum_))

if __name__ == '__main__':
	main()