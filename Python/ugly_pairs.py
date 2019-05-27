from itertools import permutations

def check_consequetive(word):
	counter=0
	temp=word
	ascii_list=list(map(lambda x: ord(x), list(word)))
	for eachnum in range(0,len(ascii_list)-1):
		first_=ascii_list[eachnum]
		next_=ascii_list[eachnum+1]
		if first_==(next_+1) or (first_+1)==next_ :
			counter+=1
	if counter<1:
		return True



def main():
	userinput=input("Enter a Word: ")
	perm=permutations(userinput,len(userinput))
	
	for x in perm:
		string=''.join(x)
		if (check_consequetive(string)):
			print(string)
			break

if __name__ == '__main__':
	main()