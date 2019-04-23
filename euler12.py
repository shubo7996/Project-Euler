'''
@Solution-Subhamoy Paul
'''

"""
	Method 1

"""
"""
def isTriangular(num):
	if num<0:
		return False

	sum=0
	n=1

	while(sum<=num):
		sum+=n
		#print(sum)
		if(sum==num):
			if(checkFactors(num)):
				return True			
		n+=1

	return False

def checkFactors(num):
	counter=0
	for i in range(1,num+1):
		if num%i==0:
			counter+=1
	if counter>=500:
		return True

if __name__ == '__main__':
	for num in range(76_000_000,77_000_000):
		if (isTriangular(num)):
			print('{} is Triangular with more than 500 factors'.format(num))
		#else:
		#	print("Not Triangular!")
"""


"""
	Method 2
"""


from sympy import factorint
import time

start=time.perf_counter()

for x in range(100,100_000_00):
	list_sum=sum([num for num in range(x+1)])
	vals_=1
	fact_dict=factorint(list_sum)
	
	for vals in fact_dict.values():
		vals_*=(vals+1)
	
	if (vals_)>500:
		print(list_sum)
		break
		
print(f"Time taken: {time.perf_counter()-start}")
