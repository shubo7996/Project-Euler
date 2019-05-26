'''
	Soulution@SubhamoyPaul
'''
import time

start=time.perf_counter()

def factorial(n):
	prod=1
	for x in range(2,n+1):
		prod*=x
	return prod

def each_fact_sum(x,chain):
	#for a,b in Counter(chain).items():
	#	if b==2:
	#		return chain[0:-1]
	if chain.count(x)==2:
		return set(chain) 
	else:
		sum_=0
		while(x>0):
			d=x%10
			sum_+=factorial(d)
			x//=10
		chain.append(sum_)
		return each_fact_sum(chain[-1],chain)

count=0
for num in range(69,int(1E6)):
	chain_list=[num]
	find_chain=each_fact_sum(num,chain_list)
	if len(find_chain)==60:
		count+=1

print(f"Result:{count}")

print(f"Time Elapsed: {time.perf_counter()-start}")