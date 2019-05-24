def  input_numbers():
	array=input()
	array_list=list(map(int,array.split(' ')))
	return array_list

def find_three_numbers(target_array,max_num):
	target_array.remove(max_num)
	a,b,c=tuple(target_array)
	return abs(max_num-a),abs(max_num-b),abs(max_num-c)

def main():
	input_=input_numbers()
	fir,sec,thr=find_three_numbers(input_,max(input_))
	print(fir,sec,thr)

if __name__ == '__main__':
	main()