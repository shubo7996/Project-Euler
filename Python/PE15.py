import math
def sumOfFactors(num):
	sum_=0
	for x in range(1,num//2+1):
		if num%x==0:
			#print(f"{num}--->{x}")
			sum_+=x
	return sum_

summ=0
for y in range(1,10000):
	first_sum=sumOfFactors(y)
	second_sum=sumOfFactors(first_sum)
	if second_sum==y:
		print(first_sum,second_sum)
		summ+=y

print(summ)