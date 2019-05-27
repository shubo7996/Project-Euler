import time

def fib(n):
	mem={}
	flag=False
	for x in range(1,n+1):
		if (x<=2):
			mem[x]=1
		elif flag is not True:
			mem[x]=mem[x-1]+mem[x-2]
			flag=_extract(mem[x])
		else:
			break	
	return sum(list(filter(lambda x: not x%2,list(mem.values())))) 

def _extract(fib_num):
	if fib_num>4000000:
		return True

if __name__ == '__main__':
	start=time.perf_counter()
	print(fib(100))
	end=time.perf_counter()
	print("Execution Time: {}".format(end-start))

