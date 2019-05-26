"""
	A programe to Print the circular primes within any range
	@author-Subhamoy Paul

"""

from collections import deque
import time

"""
	Seive of Eratosthenes to calculate a range of prime numbers

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
	print(prime_list)		
	return prime_list

"""
	This function checks whether the number is palindrome 	

"""
def calc_rev(primeNumberList,num):
	rev=0
	temp=num
	while(num>0):
		rem=num%10
		rev=rev*10+rem
		num=num//10
	#print("Reverse of {} is {}".format(temp,rev))
	if rev in primeNumberList:
		return True
	else:
		return False

"""
	This function gives a list of the rotated numbers formed out of the original prime number
	for eg: num=197
	rotated values = [197,971,719]

"""

def calc_circular(possible_value_list):
	sum_list=[]
	for x in range(len(possible_value_list)):
		actualNumber_=''
		for each_number in possible_value_list:
			actualNumber_+=each_number
		print("Actual Number is: ",actualNumber_)			
		sum_list.append(actualNumber_)
		possible_value_list.rotate()
	print(sum_list)
	return sum_list

"""
	This function checks if the prime number is a Circular Prime by checking 
	whether the rotated values of that particular prime number, present in the list, 
	is a prime number. 

"""
def check_sum_if_prime(rotatedValuesList,primeNumberList_):
	_counter_=0
	length=len(rotatedValuesList)
	for each_rotated_value in rotatedValuesList:
		each_rotated_value=int(each_rotated_value)
		if each_rotated_value in primeNumberList_:
			_counter_+=1
	if _counter_== length:
		print("True")
		return True
	else:
		print("False")
		return False
"""
	main function runs the essential loops through the Prime List and performs 
	functions according to the length of the Deque List of the PrimeNumber. 

"""

def main():
	primes=seive(1000000)
	counter=0
	for i in primes:
		numberList=deque([x for x in str(i)])
		if len(numberList)==1: #if prime number has one digit, its going to be circular
			#print(i)
			counter+=1
			print("Counter at {}:{}".format(i,counter))
		if len(numberList)==2: #if prime number has two digits,we check if its palindrome is prime
			check_prime=calc_rev(primes,i)
			#print(check_prime)
			if check_prime is True:
				#print(i)
				counter+=1
				print("Counter at {}:{}".format(i,counter))
		if len(numberList)>=3: #if prime number has more than 3 digits, we check if its circular
			print(numberList)
			rotatedList=calc_circular(numberList)
			check_=check_sum_if_prime(rotatedList,primes)
			if check_ is True:
				counter+=1
				print("Counter at {}:{}".format(i,counter))
	return counter

if __name__ == '__main__':
	start=time.time()
	counterValue=main()
	print("Total Counter:",counterValue)
	print(time.time()-start)

	





