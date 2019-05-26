"""
    d2d3d4=406 is divisible by 2
    d3d4d5=063 is divisible by 3
    d4d5d6=635 is divisible by 5
    d5d6d7=357 is divisible by 7
    d6d7d8=572 is divisible by 11
    d7d8d9=728 is divisible by 13
    d8d9d10=289 is divisible by 17

"""
import time
from itertools import permutations

def check_div(num):
	if int(num[0])==0:
		return False
	if len(num)<10:
		return False
	if int(num[7:10])%17==0:
		if int(num[6:9])%13==0:
			if int(num[5:8])%11==0:
				if int(num[4:7])%7==0:
					if int(num[3:6])%5==0:
						if int(num[2:5])%3==0:
							if int(num[1:4])%2==0:
								#yield num
								return True
	return False


def main():
	perm_=permutations('1406357289',10)
	sum_=0
	for x in perm_:
		num_=''.join(x)
		#print(num_)
		if check_div(num_) is True:
			sum_+=int(num_)
	print("Answer is:{}".format(sum_))

if __name__ == '__main__':
	start=time.clock()
	main()
	print("Execution Time: {}".format(time.clock()-start))
	#if check_div('1406357289'):
	#	print("Its working~")
