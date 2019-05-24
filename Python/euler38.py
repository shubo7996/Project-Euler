s=set(['1','2','3','4','5','6','7','8','9'])
lists=[]
strg=''
for x in range(1000,10000):
	strg=''
	for i in range(1,10):
		strg+=str(x*i)
		if len(strg)==9:
			if set(strg)==s:
				lists.append(int(strg))
				break
		elif len(strg)>9:
			break
		else:
			continue
		
print(sorted(lists))
print('Answer is:',sorted(lists)[-1])