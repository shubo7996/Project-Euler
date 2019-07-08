from sympy import factorint
import itertools
import time

'''
1/x + 1/y = 1/n ; x,y > n
x = n+i ; y = n+j

=> 1/n+i + 1/n+j = 1/n
=> (2n+i+j)/(n+i)(n+j) = 1/n
=> 2n^2 + ni + nj = n^2 + ni + nj + ij
=> 2n^2 = n^2 + ij
=> n^2 = ij

'''

start=time.perf_counter()

for x in itertools.count(4):
	count=1
	fact_dict=factorint(x)
	for val in fact_dict.values():
		count*=2*val+1
	if (count+1)//2>1000:
		print(x)
		break

end=time.perf_counter()

print(f"Time Elapsed: {end-start}")
