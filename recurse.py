import time
import sys

sys.setrecursionlimit(1000)
start=time.perf_counter()


def non_recurse(num):
	prod=1
	for x in range(2,num+1):
		prod*=x
	return prod
non_recurse(997)

print(f"Non recursive took: {time.perf_counter()-start} ms")
#0.018870274000000003 

'''
def recurse(num):
	if num==1:
		return 1
	else:
		return num*recurse(num-1)

#print(recurse(997))
print(f"recursive took: {time.perf_counter()-start} ms")
#0.018870274000000003 

'''