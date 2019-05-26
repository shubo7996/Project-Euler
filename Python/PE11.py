filepath="euler18.txt"

with open(filepath,'r') as files:
	array=[]
	for each in files:
		array.append(each)
#print(array)

newArray=[]
for i in array:
	j=i.split(' ')
	k=[int(n) for n in j]
	newArray.append(k)
print(newArray)

l=len(newArray)
for i in range(l-1):
	lastArray=newArray[-1]
	secondLastArray=newArray[-2]
	for j in range(len(secondLastArray)):
		secondLastArray[j]+=max(lastArray[j],lastArray[j+1])
	newArray.pop(-1)
	newArray[-1]=secondLastArray
print(newArray[0][0])
