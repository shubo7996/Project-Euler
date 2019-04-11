import sympy

def getFactors(num):
	factors=sympy.factorint(num)
	return factors

def main():
	factors_=getFactors(600851475143)
	print(sorted(factors_)[-1])



if __name__ == '__main__':
	main()