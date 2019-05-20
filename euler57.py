import math

def main():
	limit=1000
	result=0
	den,num=2,3

	for x in range(1,limit):
		num+=2*den
		den=num-den
		if int(math.log10(num))>int(math.log10(den)):
			result+=1

	print(result)

if __name__ == '__main__':
	main()