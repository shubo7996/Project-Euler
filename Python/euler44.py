def pent():
	pent_list=[]
	for x in range(1,10000):
		pent_list.append(x*(3*x-1)//2)
	return(pent_list)

pentlist=pent()
diff_list=[]
for x in range(len(pentlist)):
	for y in range(x+1,len(pentlist)):
		sum_=pentlist[x]+pentlist[y]
		diff=abs(pentlist[x]-pentlist[y])
		if sum_ in pentlist and diff in pentlist:
			print(pentlist[x],pentlist[y])
			diff_list.append(diff)
print(sorted(diff_list))