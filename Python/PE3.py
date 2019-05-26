from numpy import *
import time

start=time.perf_counter()
filepath="euler11.txt"

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
#print(newArray)

problemMatrix=matrix(newArray)
print(problemMatrix)
max_prod=1

for i in range(16):
	for j in range(16):
		prod_rows=problemMatrix[i,j]*problemMatrix[i+1,j]*problemMatrix[i+2,j]*problemMatrix[i+3,j]
		if prod_rows>max_prod:
			max_prod=prod_rows
		prod_cols=problemMatrix[i,j]*problemMatrix[i,j+1]*problemMatrix[i,j+2]*problemMatrix[i,j+3]
		if prod_cols>max_prod:
			max_prod=prod_cols
		prod_diag=problemMatrix[i,j]*problemMatrix[i+1,j+1]*problemMatrix[i+2,j+2]*problemMatrix[i+3,j+3]
		if prod_diag>max_prod:
			max_prod=prod_diag
		prod = problemMatrix[19-i,j]*problemMatrix[18-i,j+1]*problemMatrix[17-i,j+2]*problemMatrix[16-i,j+3]
		if prod>max_prod:
			max_prod=prod
print(max_prod)
print(f"Time elapsed: {time.perf_counter()-start}")

