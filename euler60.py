from Euler_Prime import seive,isPrime
import time

s_=seive(100000)
#prime_list=[]
#for x in range(2,len(seive)):
#	for y in range(x+1,len(seive)):
#		if (str(x)+str(y) in s_) or (str(y)+str(x) in s_):
#			prime_list.append(y)

for x in range(0,len(s_)-10):
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
