import time

start=time.perf_counter() 

arr=[]

func=lambda x,y:x**y

for x in range(1,100):
	for y in range(1,100):
		arr.append(sum(list(map(int,str(func(x,y))))))

print(max(arr))

end=time.perf_counter()

print("Time Elapsed: {}".format(end-start))


		