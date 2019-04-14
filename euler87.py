num_list=[each_num for each_num in range(1,51)]
count=0
for x in range(2,len(num_list)):
	for y in range(x,len(num_list)):
		for z in range(y,len(num_list)):
			if x%2==1 and y%2==1 and z%2==1:
				if (x**2+y**3+z**4) or (x**3+y**4+z**2) or (x**4+y**2+z**3) in num_list:
					count+=1
print(count)