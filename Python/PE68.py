import time

def main():
	ways_=[1]+[0]*100
	for x in range(1,100):
		for j in range(x,101):
			ways_[j]=ways_[j]+ways_[j-x]
	print(ways_)
	print(f"Number of ways 100 can be written: {ways_[-1]}")

if __name__ == '__main__':
	start=time.perf_counter()
	main()
	print(f"Time Elapsed: {time.perf_counter()-start}")