import time
import math

def checkpal(n):
	if n>int(1E8):
		return False
	if n==int(str(n)[-1::-1]):
		return True
	else:
		return False

def main():
	pal_list=list()
	# for x in range(1,int(math.sqrt(int(1E8)))+1):
	# 	if checkpal(x):
	# 		pal_list.append(x)
	main=0
	final_sum=0
	# for outer in range(1,len(pal_list)):
	#  	main=(pal_list[outer]*pal_list[outer])
	#  	for inner in range(outer+1,len(pal_list)):
	#  		main+=(pal_list[inner]*pal_list[inner])
	#  		if main in pal_list:
	#  			final_sum+=main
	# print(final_sum)
	for outer in range(1,int(math.sqrt(int(1E8)))+1):
		main=(outer*outer)
		for inner in range(outer+1,int(math.sqrt(int(1E8)))+1):
			main+=(inner*inner)
			if checkpal(main) and main not in pal_list:
				final_sum+=main
				pal_list.append(main)
	print(final_sum)
	
	
if __name__ == '__main__':
	start=time.time()
	main()
	end=time.time()
	print(f"Time Elapsed: {end-start}")