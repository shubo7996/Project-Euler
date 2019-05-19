from itertools import product

def  input_numbers():
	array=input()
	array_list=list(map(int,array.split(' ')))
	return array_list

def find_three_numbers(target_array,max_num):
	num_list=[x for x in range(1,max_num//2+1)]
	perm_list=list(product(num_list,repeat=3))
	list_=[]
	for each_perm in range(0,len(perm_list)):
		#print(each_perm)
		a,b,c=perm_list[each_perm]
		temp_arr=target_array
		if a+b in temp_arr and b+c in temp_arr and a+c in temp_arr and a+b+c==max_num:
			break
	return a,b,c

def main():
	input_=input_numbers()
	fir,sec,thr=find_three_numbers(input_,max(input_))
	print(fir,sec,thr)

if __name__ == '__main__':
	main()