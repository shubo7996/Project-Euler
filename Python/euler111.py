from Euler_Prime import isPrime
import time,math
# # # from collections import Counter
from itertools import product,zip_longest,combinations

# # # def max_digit(number,digit):
# # #  	_dict=Counter(str(number))
# # #  	max_=max(list(_dict.values()))
# # #  	if str(digit) in list(_dict.keys()):
# # #  		try: 			
# # #  			if _dict[str(digit)]==max_:
# # #  				return number
# # #  		except:
# # #  			print("Logic is wrong !")
# # #  	else:
# # #  		return 0

# # counter_dict={0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}

# # def driver(number_):
# # 	num_,dict_=number_
# # 	high_key=_maxDigit(dict_)
# # 	return high_key

# # def _maxDigit(prime_num_dict):
# # 	high=max(list(prime_num_dict.values))
# # 	max_index=list(prime_num_dict.keys())[list(prime_num_dict.values(high)).index(high)]
# # 	if counter_dict[max_index]<=high:
# # 		counter_dict[max_index]=high

# # def extract(primeList):
# # 	finale=[]
# # 	for x in primeList:
# # 		if max(Counter(x).values()) in list(counter_dict.values()):
# # 			if list(Counter(x).key())[list(Counter(x).values()).index(max(Counter(x).values()))]==list(counter_dict.keys())[list(counter_dict.values()).index(max(counter_dict.values()))]:
# # 				finale.append()
# # 	return finale

# # def main():
# # 	start=time.process_time()
# # 	atkins_=atkins(10**9-1)
# # 	final_=[ (int(''.join(x)),int(''.join(x))) for x in combinations('1234567890',4) if int(''.join(x))[0] is not 0 and isPrime(int(''.join(x)))]
# # 	for x in final_:
# # 		driver(x)
# # 	extract_=sum(extract(final_))
# # 	print(extract_)	
# # 	print(f"Answer:{extract_}")
# # if __name__ == '__main__':
# # 	main()

# # # final_sum,sum_num=0,0
# # # for x in range(len(final_)):
# # # 	for y in range(0,9):
# # #  		sum_num+=max_digit(x,y)
# # #  		final_sum+=sum_num
# # # print(final_sum)
# # # print(f"Time taken:{time.process_time()-start}")


# def permutation(s):
# 	result=[]
# 	if len(s)==1:
# 		result.append(s)
# 	else: 
# 		if len(s)>1:
# 			last=s[-1]
# 			rest=s[0:-1]
# 			result=_merge(permutation(rest),last)
# 	return result

# def _insert(string, index,char):
#     return string[:index] + char + string[index:]

# def _merge(list_,c):
# 	res_=[]
# 	for s in list_:
# 		for i in range(0,len(s)+1):
# 			ps= _insert(s,i,c)
# 			res_.append(ps)
# 	return res_

# print(permutation('1111111112'))


#final_=set([int(''.join(x)) for x in permutations('1111111123',10) if isPrime(int(''.join(x)))])
#print(final_)


# def main():
# 	primeList=atkins(int(math.sqrt(10**10)))
# 	for digit in range(10):
# 		for rep in range(10,-1,-1):
# 			sum_=0
# 			digits=[0]*10
# 			for i  in range(9**(10-rep)):
# 				for j in range(rep):
# 					digits[j]=digit
# 				temp=i
# 				for j in range(10-rep):
# 					d=temp%9
# 					if d>=digit:
# 						d+=1
# 					if j>0 and d>digits[10-j]:
# 						break
# 					digits[-1-j]=d
# 					temp//=9


def generate_numbers(n,d,rep):

	def _filter(t):
		if t[0][0]==0 and t[1][0]==0:
			return False
		if t[0][-1]==n-1 and (t[1][-1]&1==0 or t[1][-1]==0):
			return False
		return True
		
	other_indexes=combinations(range(n),n-rep)
	other_numbers=product(*([tuple(set(range(10))-set([d]))]*(n-rep)))
	joined=filter(_filter,product(other_indexes,other_numbers))	
	for tup in joined:
		base=[d for i in range(n)]
		for ind,val in zip_longest(*tup):
			base[ind]=val
		if base[0]==0 or base[-1]&1==0 or base[-1]==5:
			continue
		yield(int(''.join(map(str,base))))

def main():
	result=0
	n=10
	for d in range(0,10):
		found_=[]
		rep=n-1
		while not found_:
			for i in generate_numbers(n,d,rep):
				if not isPrime(i):
					continue
				found_.append(i)
			rep-=1
		result+=sum(found_)
	print(result)

if __name__ == '__main__':
	start=time.perf_counter()
	main()
	end=time.perf_counter()
	print(f"Time: {end-start}")



