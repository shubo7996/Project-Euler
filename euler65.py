'''
	Solution@Subhamoy Paul

'''

import time

def digital_sum(n):
	sum_=0
	while(n>0):
		d=n%10
		sum_+=d
		n=n//10
	return sum_

def main():
	num=2
	den=1
	convergence_list=[2]
	for x in range(2,101):
		temp=den
		if x%3==0:
			convergence=2*(x//3)
		else:
			convergence=1
		convergence_list.append(convergence)
		den=num
		num=(convergence*den)+temp #(c(n)*num(n-1))+num(n-2)

	print(f"Convergence List: {convergence_list}")	
	resultant_sum=digital_sum(num)
	print(f"Sum of Digit of the 100th Convergence Term is: {resultant_sum}")

if __name__ == '__main__':
	start=time.perf_counter()
	main()
	print(f"Time Elapsed: {time.perf_counter()-start}")