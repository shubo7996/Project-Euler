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
	for num in range(76000000,77000000):
		if (isTriangular(num)):
			print('{} is Triangular with more than 500 factors'.format(num))
		#else:
		#	print("Not Triangular!")

