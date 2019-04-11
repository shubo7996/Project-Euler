'''
	@author-Subhamoy Paul

'''

def find_multipliers_multiplicands(number):
	rlist=[]
	end=(number//2)+1
	for divisor in range(1,end):
		q,r=divmod(number,divisor)#divmod returns tuple(p,q)
		if r is 0:
			rlist.append((divisor,q))
	return rlist

def check_if_Pandigital(tup_,num):
	p,q = tup_
	newStr=str(p)+str(q)+str(num)
	#print(newStr)
	if len(newStr)!=9:
		#print('dicarded:',tup_)
		return False
	sorted_str=[''.join(sorted(newStr))]
	if sorted_str==['123456789']:
		#print(sorted_str)
		return True
	return False 


sum_=set()
for y in range(1000,10001):
	find_=find_multipliers_multiplicands(y)
	#print(find_)
	for x in find_:
		p,q=x
		if (q,p) in find_:	
			find_.remove((q,p))
		if check_if_Pandigital(x,y):
			print(f"{p} x {q} = {p*q}")
			sum_.add(p*q)
print(f'Distinct Product List: {sum_}')
print('Answer is:',sum(sum_))
			
		
