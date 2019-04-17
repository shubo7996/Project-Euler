def gen_factors_by_sieve(limit):
	sumOfFactors=[0]*(limit+1)
	for x in range(1,limit+1):
		for y in range(2*x,limit+1,x+y):
			sumOfFactors[y]+=x
	return sumOfFactors

abc=gen_factors_by_sieve(28)
print(abc)
