"""
	@author-Subhamoy Paul
"""

from collections import Counter
import time

def getTriangular():
	triList=[]
	for x in range(10000,100000):
		triList.append(x*(x+1)//2)
	return triList

def getPentagonal():
	pentList=[]
	for x in range(10000,100000):
		pentList.append(x*(3*x-1)//2)
	return pentList

def getHexagonal():
	hexList=[]
	for x in range(10000,100000):
		hexList.append(x*(2*x-1))
	return hexList

def main():

	triangle=getTriangular()
	#print("Triangular List ---> {}".format(triangle))
	#print("------------------------------------------")
	pentagon=getPentagonal()
	#print("Pentagonal List ---> {}".format(pentagon))
	#print("------------------------------------------")
	hexagon=getHexagonal()
	#print("Hexagonal List ---> {}".format(hexagon))
	#print("------------------------------------------")
	final_list=triangle+pentagon+hexagon
	count_dict=Counter(final_list)
	print(count_dict)

	for k,v in count_dict.items():
		if v==3:
			print("Answer is {}".format(k))


if __name__ == '__main__':
	start=time.clock()
	main()
	end=time.clock()
	print("Execution Time: {}".format(end-start))
