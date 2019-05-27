def totient(n):
	from sympy import factorint
	fact_dict=factorint(n)
	phi_=1
	for key,val in fact_dict.items():
		phi_*=key**val-key**(val-1)
	return phi_


def main():
	max_=0
	for number in range(10000,1000000):
		phi_=totient(number)
		val=number/phi_
		#print(number,"-->",phi_,"--->",val)
		if val>max_:
			max_=val
			temp_var=number
	print(temp_var)


if __name__ == '__main__':
	main()