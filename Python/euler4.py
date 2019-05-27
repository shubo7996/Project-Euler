import time

def checkPalindrome(n):
	rev=0
	temp=n
	while(temp>0):
		dig=temp%10
		rev=rev*10+dig
		temp=temp//10

	if rev==n:
		return True
	else:
		return False

def checkProduct():
	max=0
	for i in range(100,1000):
		for j in range(100,1000):
			p=i*j
			if (checkPalindrome(p) and p>max):
				max=p

	print("Largest Palindrome is {}".format(max))

if __name__ == '__main__':
	start=time.perf_counter()
	checkProduct()
	print(f"Time Elapsed: {time.perf_counter()-start}")
