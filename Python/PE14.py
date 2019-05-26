def factorial(n):
	if n<=1:
		return 1
	else:
		return(n*factorial(n-1))

def main():
	sum_=0
	fact_=factorial(100)
	print(fact_)
	sum_list=list(str(fact_))
	for x in sum_list:
		sum_+=int(x)
	print(sum_)

if __name__ == '__main__':
	main()