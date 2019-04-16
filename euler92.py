import math
import time

start=time.perf_counter()
def each_square_sum(x):
	#for a,b in Counter(chain).items():
	#	if b==2:
	#		return chain[0:-1]
	#if chain.count(x)==2:
		#return set(chain) 		
	#else:
	sum_=0
	while(x>0):
		d=x%10
		sum_+=d**2
		x//=10
	#chain.append(sum_)
	return sum_


counter=0
limit=int(1E7)
cache_size=int(math.ceil(81*math.log10(limit)))+1
cache_list=[False]*(cache_size+1)
#number_list=[]

for x in range(1,cache_size):
	seq=each_square_sum(x)
	while(seq>1 and seq!=89):
		seq=each_square_sum(seq)
	if (cache_list[seq] or seq==89):
		counter+=1
		cache_list[x]=True
for y in range(cache_size,limit+1):
	if cache_list[each_square_sum(y)]:
		counter+=1

		
	'''  
	#Generates fast upto 1E5
	
	if int(str(x)[::-1]) not in number_list:
		#number_list.append(x)
		sq_chain=[x]
		final_chain=each_square_sum(x,sq_chain)
		#print(x,"--->",final_chain)
		if 89 in final_chain:
			counter+=1
			number_list.append(x)
	else:
		counter+=1
		number_list.append(x)
	
	'''
print(f"Counter is: {counter}")
print(f"Time Elapsed: {time.perf_counter()-start}")