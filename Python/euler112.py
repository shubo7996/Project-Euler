import time

start=time.perf_counter()

num=101
numList=[]
while num>100:
	asc,dec=0,0
	str_num=str(num)
	for x in range(0,len(str_num)-1):
		if str_num[x]<str_num[x+1]:
			asc+=1
		else:
			if str_num[x]>str_num[x+1]:
				dec+=1

	if asc>=1 and dec>=1:
		#print(num)
		numList.append(num)

	
	percent=len(numList)/num * 100
	if (percent==99):
		print(num)
		break

	num+=1

print(f"Time elapsed: {time.perf_counter()-start}" )

	