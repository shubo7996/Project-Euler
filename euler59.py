def main():
	filepath="euler59.txt"
	fline=open(filepath).readlines()
	for x in fline:
		num_array=x.split(',')
	cipher=[int(each_num) for each_num in num_array]
	print(cipher)
	from collections import Counter
	key_=[]
	for i in range(3):
		key_.append(Counter(cipher[i::3]).most_common(1)[0][0] ^ 32)
	print(key_)
	print(''.join(map(chr,key_)))
	print (sum(x^y for x, y in zip(cipher, key_*(len(cipher)//3+1))))

if __name__ == '__main__':
	main()