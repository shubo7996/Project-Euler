import time
import math

def is_square(x):
	if x==int(math.sqrt(x))*int(math.sqrt(x)):
		return True
	else:
		return False


def continued_fraction_sqrt(n):
	
	if is_square(n):
		return [int(math.sqrt(n))]
	
	conv_list=[]

	numerator_first=0
	denominator_first=1

	while True:
		next_n=int((math.floor(math.sqrt(n))+numerator_first)/denominator_first)
		conv_list.append(int(next_n))

		numerator_second=denominator_first
		denominator_second=numerator_first-denominator_first*next_n

		denominator_third=(n - pow(denominator_second,2)) / numerator_second
		numerator_third= -denominator_second

		if denominator_third==1:
			conv_list.append(conv_list[0]*2)
			break

		numerator_first,denominator_first=numerator_third,denominator_third

	return conv_list[:-1]

def continued_fraction_simple(conv_list):
	num,den=1,conv_list.pop()
	while conv_list:
		den,num=conv_list.pop()*den+num,den
	return den,num

def main():
	largest=0,0
	for eachnum in range(1,1001):
		cont_frac=continued_fraction_sqrt(eachnum)
		if len(cont_frac)%2!=0:
			x,y=continued_fraction_simple(cont_frac)
			x,y=2*x**2+1,2*x*y
		else:
			x,y=continued_fraction_simple(cont_frac)
		if x>largest[1]:
			largest=eachnum,x
	print(f"Result: {largest[0]}")

if __name__ == '__main__':
	start_time=time.process_time()
	main()
	end_time=time.process_time()
	print("Time Elapsed: {}".format(end_time-start_time))
