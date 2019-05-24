def openfile():
	list_file=[]
	filepath = 'euler13.txt'  
	fline=open(filepath).readlines()
	summ_=0
	for each_line in fline:
		each_line=int(each_line)
		summ_+=each_line
	print('Sum of all the digits: {}'.format(int(summ_)))
	#print(fline)
	#extractList(fline)

"""
def extractList(list_file):
	sumList=[]
	for each_line in list_file:
		#print(each_line)
		_summ=calculateSum(each_line)
		sumList.append(_summ)
	print("List of sum of the 50 digit number: {}".format(sumList))
	calculateFirstTenDigit(sumList)

def calculateSum(n):
	summ=0
	temp=int(n)
	#print(temp)
	while (temp>0):
		d=temp%10
		summ+=d
		temp//=10
	print('Sum of {} is {}'.format(n,summ))
	return summ

def calculateFirstTenDigit(sumList):
	_final_sum=0
	for i in sumList:
		_final_sum+=i
	print("Sum of the entire numbers: {}".format(_final_sum))
	
"""

if __name__ == '__main__':
	openfile()
