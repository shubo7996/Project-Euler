"""
	author@Subhamoy paul
"""


import time

def palin(num,count=0):
	rev=int(num)+int(num[::-1])
	if str(rev)==(str(rev))[::-1]:
		return True
	else:
		if count<50:
			count+=1
			return palin(str(rev),count)
		else:
			return False

if __name__ == '__main__':
	start=time.perf_counter()
	counter_=0
	for x in range(1,10001):
		if not palin(str(x)):
			counter_+=1
	print(f"Number of Non Lychrel Numbers are: {counter_}")		
	print(f"Time Elapsed: {time.perf_counter()-start}")