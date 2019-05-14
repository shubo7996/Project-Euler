from collections import defaultdict
from itertools import permutations
squareList=[x*x for x in range(2,32000)]
filepath="euler98.txt"
new_list=[]

def extract_data_from_file():
    fline=open(filepath).read()
    length=len(fline.strip("").split(","))
    for x in range(0,length):
    	new_list.append(fline.strip("").split(",")[x])
    final_list=list(map(lambda x: x[1:-1],new_list))
    return final_list

# def min_max(word_list):
# 	minimum_letter=min(list(map(lambda x:len(x),word_list)))
# 	maximum_letter=max(list(map(lambda x:len(x),word_list)))
# 	return minimum_letter,maximum_letter

def make_dictionary(word_list):
	my_data={}
	for x in word_list:
		my_data[''.join(sorted(x))]=x
	return my_data

def binary_search(arr,val):
	if (len(arr)==0 or (len(arr)==1 and arr[0]!=val)):
		return False

	mid= len(arr)//2
	mid_val = arr[mid]

	if val==mid_val: return True
	if val<mid_val: return binary_search(arr[:len(arr)//2],val) #recursive function which takes the first half of the array
	if val>mid_val: return binary_search(arr[len(arr)//2+1:],val) #recursive function which takes the second half of the array 


def make_square_anagram(first_word,second_word):
	max_=0
	first_word_char_list=list(first_word)
	second_word_char_list=list(second_word)
	for each_square_num in range(0,len(squareList)):
		square_length=len(str(squareList[each_square_num]))
		if (square_length<len(first_word)):
			continue
		if (square_length>len(first_word)):
			break
		match=True
		square_=squareList[each_square_num]
		mapping= defaultdict()
		for each_char in range(len(first_word_char_list)-1,-1,-1):
			each_digit=square_%10
			square_=square_//10
			if first_word_char_list[each_char] in mapping.keys():
				if mapping[first_word_char_list[each_char]]==each_digit:
					continue
				else:
					match=False
					break
			if each_digit in mapping.values():
				match=False
				break
			mapping[first_word_char_list[each_char]]=each_digit
		if not match:
			continue
		second_word_value=0
		if mapping[second_word_char_list[0]]==0:
			match=False
		else:
			for each in range(0,len(second_word_char_list)):
				second_word_value=second_word_value*10+mapping[second_word_char_list[each]]
		if not match:
			continue
		if binary_search(squareList,second_word_value) is True:
			maxpair=max(second_word_value,squareList[each_square_num])
			max_=max(max_,maxpair)
	return max_


def main():
	result=0
	word_list=extract_data_from_file()
	anagram_dict=make_dictionary(word_list)
	#print(anagram_dict)
	for ana_value in anagram_dict.values():
		#if len(ana_value)<=1:
		#	continue
		#for x in range(0,len(ana_value)):
		#	for y in range(x+1,len(ana_value)):
		temp_perm_list=[]
		perm_=permutations(ana_value,len(ana_value))
		for x in perm_:
			word=''.join(x)
			temp_perm_list.append(word.upper())
		#print(temp_perm_list)
		for y in temp_perm_list:
			if y in word_list and y!=ana_value:
				temp=y
				#print(temp)
				pairvalue=make_square_anagram(ana_value,temp)
				if pairvalue>result:
					result=pairvalue
				print(f"{ana_value} and {temp} ----> {pairvalue}")
				break
		#pairvalue=make_square_anagram(ana_value,temp)
		# if pairvalue>result:
		# 	result=pairvalue
		# print(f"{ana_value} and {temp} ----> {pairvalue}")

	print("Result is: {}".format(result))			

	# min_,max_=min_max(word_list)
	# print(min_,max_)
	# for x in word_list:
	# 	if len(x)==max_:
	# 		print(x)
	#print(word_list)
	#mega_list=[]
	#for x in word_list:
	#	my_data=(x,''.join(sorted(x)))
	#	mega_list.append(my_data)
	#print(mega_list)

if __name__ == '__main__':
	main()        