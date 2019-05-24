import time

def fib(n):
	mem={}
	for x in range(1,n+1):
		if (x<=2):
			mem[x]=1
		else:
			mem[x]=mem[x-1]+mem[x-2]
	return mem

def extract(fib_Dict):
	sum_=0
	for v in fib_Dict.values():
		if v<=4000000:
			if v%2==0:
				sum_+=v
	return sum_  


if __name__ == '__main__':
	start=time.clock()
	fibonacci_=fib(100)
	print(fibonacci_)
	extract_=extract(fibonacci_)
	print("Answer is: {}".format(extract_))
	end=time.clock()
	print("Execution Time: {}".format(end-start))