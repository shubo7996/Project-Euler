"""
	Solution @SubhamoyPaul

"""

import time

def pent_gen():
	pen_list=[]
	for x in range(1,250):
		pen=(x*((3*x)-1))//2
		neg_pen=((-x)*((3*(-x))-1))//2
		pen_list.extend([pen,neg_pen])
	return pen_list

def main():
	penta=pent_gen()
	print(penta)
	part,sign=[1],[1,1,-1,-1]
	num,mil=0,10_00_000
	while(part[num]>0):
		num+=1
		part_x,i=0,0
		while(penta[i]<=num):
			part_x+=part[num-penta[i]]*sign[i%4]
			i+=1
		part.append(part_x%mil)
	print(f"Answer is: {num}")
	

if __name__ == '__main__':
	start=time.perf_counter()
	main()
	print(f"Time Elapsed: {time.perf_counter()-start}")