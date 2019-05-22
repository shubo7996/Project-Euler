import time
import sys

limit=12000
minSumProd=[sys.maxsize]*(limit+1)

def factorization(n,remain,maxFact,_sum,terms):
	if (remain==1):
		if(_sum>n):
			raise AssertionError()
		terms+=n-_sum
		if (terms<=limit and n<minSumProd[terms]):
			minSumProd[terms]=n
	else:
		for x in range(2,maxFact+1):
			if (remain%x==0):
				factor=x
				factorization(n,remain//factor,min(factor,maxFact),_sum+factor,terms+1)

def main():
	for x in range(2,limit*2+1):
		factorization(x,x,x,0,0)
	result=sum(set(minSumProd[2:]))
	print(result)

if __name__ == '__main__':
	start=time.process_time()
	main()
	end=time.process_time()
	print("Time Elapsed: {}".format(end-start))
