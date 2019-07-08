from sympy import factorint
import time

'''
1/x + 1/y = 1/n
x = n+i ; y = n+j
=> 1/n+i + 1/n+j = 1/n
=> (2n+i+j)/(n+i)(n+j) = 1/n
=> 2n^2 + ni + nj = n^2 + ni + nj + ij
=> 2n^2 = n^2 + ij
=> n^2 = ij

'''



start=time.perf_counter()

for x in range(int(10E7)):
	count,total_solution=1,0
	fact_dict=factorint(x)
	for val in fact_dict.values():
		count*=2*val+1
	total_solution=(count+1)//2
	if total_solution>1000:
		print(x)
		break

end=time.perf_counter()

print(f"Time Elapsed: {end-start}")

