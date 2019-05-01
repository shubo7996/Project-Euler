import time

start=time.perf_counter()

num=2**1000
tot=0
while(num>0):
	dig=num%10
	tot=tot+dig
	num=num//10

print(tot)
print(f"Time Elapsed: {time.perf_counter()-start}")