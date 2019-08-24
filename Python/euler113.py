import time

'''
 //For Increasing Number
    //Eg-123 (Let A be the first number,
    //B be the second number, C be the third number)
    //A can be between 0-9
    //B can be between A-9
    //C can be between B-9
    //Thus we can choose 3 digits out of 12(10 + 2(if A=B or B=C)
    //We subtract one to exclude (0,0,0)

    //For Decreasing Number
    //Eg-741 (Let A,B,C be the digits)
    //A can be between 0-9
    //B can be between 0-A
    //C can be between 0-B
    //Thus we can choose 3 digits out of 13(10 + 2(if A=B or B=C)
    //We add one to include leading zeroes.

    //Along with Adding the Increasing and Decreasing Numbers
    //We need to Add the monotonic numbers eg-666,44
    //For every power of 10, we have 9 such numbers eg-11,22,..99,..,444,999
    //Since Googol contains 100 digits, 9*100

    //Final Equation
    //((109 100)−1)+((110 100)−101)−(9×100)(total)
'''

def combinations(n,k):
	res=1
	for i in range(1,k+1):
		res*=n-(k-i)
		res/=i
	return res

def main():
	digits=100
	result=int(((combinations(digits+9,digits)-1)+(combinations(digits+10,digits)-101)-9*100))
	print(result)

if __name__ == '__main__':
	start=time.perf_counter()
	main()
	print(f"Time elapsed: {time.perf_counter()-start}" )
