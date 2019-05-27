"""
	a^b for 2 ≤ a ≤ 5 and 2 ≤ b ≤ 5:
	@author-Subhamoy Paul
"""
import time

start=time.time()
power_dict={}
for x in range(2,101):
	for y in range(2,101):
		power=pow(x,y)
		strg=str(x)+'^'+str(y)
		if power not in power_dict.values():
			power_dict[strg]=power
		else:
			continue
#print(power_dict)
lst=[]
for v in power_dict.values():
	lst.append(v)

print(sorted(lst))
print('Answer is:',len(lst))
print(f'Execution Time: {time.time()-start}')

