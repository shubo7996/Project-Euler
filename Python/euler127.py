from sympy import factorint
from operator import mul
from functools import reduce
import time

def gcd(a,b):
	while b!=0:
		a,b=b,a%b	
	return a

def rad(n):
	prime_factor=factorint(n)
	return reduce(mul,list(prime_factor.keys()))

def main():
	limit=1000
	counter,sum_=0,0
	for a in range(1,limit):
		for b in range(a+1,limit):
			c=a+b
			if b//a is 0:
				continue
			else:				
				if c<limit:
					if gcd(a,b)==1 and gcd(a,c)==1 and gcd(b,c)==1 and rad(a*b*c)<c:
						counter+=1
						sum_+=c
	print(f"Counter: {counter}")
	print(f"Sum: {sum_}")

if __name__ == '__main__':
	start=time.perf_counter()
	main()
	end=time.perf_counter()
	print(f"Time Elapsed: {end-start}")