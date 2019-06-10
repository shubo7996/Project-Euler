import time

start=time.perf_counter()
power_list=[]
i=2
while True:
	val=1
	for _ in range(2,10):
		val*=i
		if sum(map(int,str(val)))==i and len(list(map(int,str(val))))>=2:
			power_list.append(val)
	if len(power_list)==30 or i==100:
 		break
	i+=1
print(sorted(power_list)[-1])
end=time.perf_counter()
print(f"Time Elapsed: {end-start}")

