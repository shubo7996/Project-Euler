import time

def fib(n):
	mem={}
	for x in range(1,n+1):
		if (x<=2):
			mem[x]=1
		else:
			mem[x]=mem[x-1]+mem[x-2]
	return mem

def find_index(fib_Dict):
	sum_=0
	for k,v in fib_Dict.items():
		if len(str(v))==1000:
			print(k)
			break  


if __name__ == '__main__':
	start=time.clock()
	fibonacci_=fib(10000)
	print(fibonacci_)
	find_index(fibonacci_)
	end=time.clock()
	print("Execution Time: {}".format(end-start))