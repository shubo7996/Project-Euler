from numpy import *
filepath="euler8.txt"

with open(filepath,'r') as files:
	array=[]
	for each in files:
		array.append(each)

newArray=[]
for i in array:
	j=i.split(' ')
	k=[int(n) for n in j]
	newArray.append(k)
	
big=''
for x in range(0,20):
	for i in newArray[x]:
		big+=str(i)
#print(big)

def adj(big_num):
	i=0
	lists=set()
	while i+13<=len(big_num):
		prod_=1
		for x in big_num[i:i+13]:
			prod_*=int(x)
		#print(prod_)
		lists.add(prod_)
		i+=1
	print(sorted(lists))
	print("Answer is: ",list(sorted(lists))[-1])

adj(big)