"""
	Program to find out the longet Collitz Sequence in range of 1 million.
	@author- Subhamoy Paul
	Solution to the #12 problem of the Euler's Project!\

"""
import time


def collatz():
	dict={}
	for i in range(100000,1000001):
		list=[]
		if i%2==0:
			list.append(i)
			calc_for_even(i,list,dict)
		else:
			list.append(i)
			calc_for_odd(i,list,dict)

def calc_for_even(n,list,dict):
	next=n//2
	if next==1:
		list.append(next)
		makeDict(list,dict)
		#print('Length of the List is: {}'.format(len(list)))
		return

	if next%2==0:
		list.append(next)
		calc_for_even(next,list,dict)
	else:
		list.append(next)
		calc_for_odd(next,list,dict)
	
def calc_for_odd(n,list,dict):
	next=(3*n)+1
	if next==1:
		list.append(next)
		makeDict(list,dict)
		#print('Length of the List is: {}'.format(len(list)))
		return
	if next%2==0:
		list.append(next)
		calc_for_even(next,list,dict)
	else:
		list.append(next)
		calc_for_odd(next,list,dict)

def makeDict(list,dict):
	key=list[0]
	dict[key]=list
	if key==1000000:
		#print(dict)
		findMax(dict)

def findMax(dict):
	lengthList=[]
	for k in dict.values():
		maxLength=len(k)
		
		"""
		if You Print out the sorted List, You shall find 525 is largest number in the list.
		Now accordingly, map 525 to the length of the values list and find its corresponding key
		
		"""
		if maxLength==525:
			val=k
			key=list(dict.keys())[list(dict.values()).index(val)]
	print('Key with the Longest Sequence is {}'.format(key))
	#print('List: {}'.format(sorted(lengthList)))

if __name__=='__main__':
    start=time.time()
    collatz()
    print(f"Time Elapsed: {time.time()-start}")