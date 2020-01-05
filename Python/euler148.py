# Lucas's Theorem

#  Basic Idea is to convert a row(which is base 10), to the base p (prime)[7 in this case],
#  add 1 to each of the digits and finally multiply each of the digits
#  For Eg: Lets Take 18th Row and prime base is 7 here.
#  18(base-10)-->24(base-7)-->35-->15
#  This prooves that in the 18th row, there are 15 elements which are not divisible by 7


from math import log,ceil
import time 

def convertIntoBase(arr,index):
	arr[0]+=1;i=0
	while (arr[i]==index):
		arr[i]=0;i+=1;arr[i]+=1

def addAndMultiply(arr,size):
	t=1
	for x in range(size):
		t*=arr[x]+1
	return t

def main():
	mainCounter=0
	size=(int)(ceil(log(1_000_000_000)/log(7)))
	arr=[0]*(size)
	for x in range(1_000_000_000):
		mainCounter+=addAndMultiply(arr,size)
		convertIntoBase(arr,7)
	print(mainCounter)

if __name__ == '__main__':
	start=time.perf_counter()
	main()
	print(f"Time Elapsed:{time.perf_counter()-start}")
