#array_list=[-3,8,-2,1,-6]
#array_list=[1, 3, 3, 7, 1, 3, 3, 7, 1, 3, 3, 7]
#array_list=[-1, -2, -3, -4, -5]

def input_():
	n=int(input("Enter Length of The array: "))
	array=input()
	m=int(input("Enter Multiplying Agent: "))
	array_list=list(map(int,array.split(' ')))
	return (array_list,n,m)

def maxSubArraySum(array):
	for i in range(1,len(array)):
		if array[i-1]>0:
			array[i]+=array[i-1]
	return max(array)

array_list,length,x_=input_()
print(length,x_)
print(array_list)

max_value=0

for x in range(0,len(array_list)):
    for y in range(x,len(array_list)):
        current_array=array_list[x:y+2]
        max_val1=sum(current_array)
        new_array=list(map(lambda x: x*x_ ,current_array))
        cur_array=array_list[0:y]+new_array
        max_val2=maxSubArraySum(cur_array)+1
        maxx=max(max_val1,max_val2)
        if maxx>max_value:
        	max_value=maxx

if max_value<1:
	max_value=0
print(max_value)

