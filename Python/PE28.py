def factorial(n):
	if n<=1:
		return 1
	else:
		return(n*factorial(n-1))

def main():
	sum_=0
	for x in range(3,100000):
		summ=0
		numList=list(str(x))
		for y in numList:
			fact_=factorial(int(y))
			summ+=fact_
		if summ==x:
			sum_+=x
	print(sum_)

if __name__ == '__main__':
	main()