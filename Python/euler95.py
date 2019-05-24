import time
# import math
#from sympy import factorint
from collections import Counter

start=time.process_time()

def gen_factors_sieve(limit):
 	sumOfFactorsList=[0]*(limit+1)
 	for x in range(1,(limit//2)+1):
 		for y in range(x*2,limit+1,x):
 			sumOfFactorsList[y]+=x
 	return sumOfFactorsList

# 	prime_factor=factorint(num)
# 	div_list=[]
# 	key_list=list(prime_factor.keys()) 
# 	limit=int(math.sqrt(num))+1
# 	for x in range(1,limit):
# 		prime_=factorint(x)
# 		if key_list==list(prime_.keys()):
# 			div_list.append(x)
# 	print(div_list)

#def recurse(num,fact_list):
#	if (Counter(list(map(str,chain)))[str(x)])==2:
#		return min(list(map(int,chain)))


chain=[]
max_val=0
set_=set()
factors_list=gen_factors_sieve(1000000)
for x in range(10000,1000000):
	temp=x
	chain=[x]
	while (Counter(list(map(str,chain)))[str(temp)])!=2:
		curr=factors_list[x]
		chain.append(curr)
		x=curr
		if  x>1000000 or len(chain)==30 or curr==0:
			break		
	#print(temp,"---->",chain)
	if (Counter(list(map(str,chain)))[str(chain[0])])==2:
		print(temp,"---->",chain)
		if len(chain)-1>=max_val:
			max_val=len(chain)-1
			set_.add(min(chain[1:len(chain)]))
print(max(set_))

end=time.process_time()
print("Time Taken: {}".format(end-start))

