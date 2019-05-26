import time

# def hcf(first, second):
#   while second > 0:
#     first, second = second, first % second
#   return first

lim=1_000_000
def counting(lim):
	phi=[x for x in range(lim+1)]
	res=0
	for x in range(2,lim+1):
		if phi[x]==x:
			for y in range(x,lim+1,x):
				phi[y]=phi[y]//(x)*(x-1)
		res+=phi[x]
	return res

def main():
	soln=counting(lim)
	print(soln)

if __name__ == '__main__':
	start_time=time.process_time()
	main()
	end_time=time.process_time()
	print("Time Elapsed: {}".format(end_time-start_time))

