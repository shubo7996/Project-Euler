"""
	A Programe to find out the number which are palindrome in either base
	@author-Subhamoy Paul
"""

import time 

def check_if_palindrome(s):
	if (len(s)-1)<0:
		return True

	else:
		if s[0]==s[-1]:
			return check_if_palindrome(s[1:-1])
		else:
			return False

def main():
	sum_=0
	for i in range(0,1000000):
		check_pal=check_if_palindrome(str(i))
		if check_pal is True:
			_Binary=str(bin(i))[2:]
			#print('Binary for {}: {}'.format(i,_Binary))
			check_bin_pal=check_if_palindrome(str(_Binary))
			if check_bin_pal is True:
				print(i,_Binary)
				sum_+=i
	print('Sum Of Palindome Digits in either base is: ',sum_)

if __name__ == '__main__':
	start=time.time()
	main()
	print("Execution Time:{}".format(time.time()-start))