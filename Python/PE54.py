from Euler_Prime import seive,isPrime
import time
import math

def comb(x,y):
	length_x=math.floor(math.log10(x))+1
	length_y=math.floor(math.log10(y))+1
	if isPrime(int(x*(10**length_y)+y)) and isPrime(int(y*(10**length_x)+x)):
		return True
	return False



s_=seive(10000)
#prime_list=[]
#for x in range(2,len(seive)):
#	for y in range(x+1,len(seive)):
#		if (str(x)+str(y) in s_) or (str(y)+str(x) in s_):
#			prime_list.append(y)
'''
for x in range(10000,len(s_)-10):
	first_number=s_[x]
	second_number=s_[x+1]
	if second_number>first_number and isPrime(int(str(first_number)+str(second_number))) and isPrime(int(str(second_number)+str(first_number))):
		third_number=s_[x+2]
		if third_number>second_number and isPrime(int(str(first_number)+str(third_number))) and isPrime(int(str(third_number)+str(first_number))) and isPrime(int(str(second_number)+str(third_number))) and isPrime(int(str(third_number)+str(second_number))):
			fourth_number=s_[x+3]
			if fourth_number>third_number and isPrime(int(str(first_number)+str(fourth_number))) and isPrime(int(str(fourth_number)+str(first_number))) and isPrime(int(str(second_number)+str(fourth_number))) and isPrime(int(str(fourth_number)+str(second_number))) and isPrime(int(str(third_number)+str(fourth_number))) and isPrime(int(str(fourth_number)+str(third_number))):
				fifth_number=s_[x+4]
				if fifth_number>fourth_number and isPrime(int(str(first_number)+str(fifth_number))) and isPrime(int(str(fifth_number)+str(first_number))) and isPrime(int(str(second_number)+str(fifth_number))) and isPrime(int(str(fifth_number)+str(second_number))) and isPrime(int(str(third_number)+str(fifth_number))) and isPrime(int(str(fifth_number)+str(third_number))) and isPrime(int(str(fourth_number)+str(fifth_number))) and isPrime(int(str(fifth_number)+str(fourth_number))):
					final_sum=first_number+second_number+third_number+fourth_number+fifth_number
					print(final_sum)
'''
for a in s_:
	for b in s_:
		if b<a:
			continue
		if comb(a,b):
			for c in s_:
				if c<b:
					continue
				if comb(a,c) and comb(b,c):
					for d in s_:
						if d<c:
							continue
						if comb(a,d) and comb(b,d) and comb(c,d):
							for e in s_:
								if e<d:
									continue
								if comb(a,e) and comb(b,e) and comb(c,e) and comb(d,e):
									final_sum=a+b+c+d+e

print(final_sum)


