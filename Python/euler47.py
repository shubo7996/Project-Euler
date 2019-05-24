import sympy
import time

def getFactors(num):
	factors=sympy.factorint(num)
	return factors

def main():
	counter=0
	for x in range(100000,1000000):
		if counter==4:
			print(x-4)
			break
		else:
			factors_dict=getFactors(x)
			if len(factors_dict.keys())==4:
				print(x,"--->",list(factors_dict.keys()))
				counter+=1
			else:
				counter=0
				

if __name__ == '__main__':
	start=time.perf_counter()
	main()
	end=time.perf_counter()
	print(f'execution time: {end-start}')
