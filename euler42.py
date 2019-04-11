def produceTriangle():
	triList=[]
	for x in range(1,1001):
		triList.append(int(0.5*x*(x+1)))
	return triList


f=open("euler42.txt",'r')
namesList=sorted(f.read().replace('"','').split(','),key=str)
#print (namesList)
char_num_dict={"A":1,"B":2,"C":3,"D":4,"E":5,"F":6,"G":7,"H":8,"I":9,"J":10,"K":11,"L":12,"M":13,"N":14,"O":15,"P":16,"Q":17,"R":18,"S":19,"T":20,"U":21,"V":22,"W":23,"X":24,"Y":25,"Z":26}

tri_=produceTriangle()
#print(tri_)
counter=0
for each_name in namesList:
	sum_=0
	for each_word in list(each_name):
		try:
			sum_+=char_num_dict[each_word]
		except:
			print("Key not Found!")
	if sum_ in tri_:
		print(each_name)
		counter+=1
print("Answer is: %i"%counter)