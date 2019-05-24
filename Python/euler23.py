import math

def divisors(n):
	yield 1
	largest=int(math.sqrt(n))

	if largest*largest==n:
		yield largest
	else:
		largest+=1

	for x in range(2,largest):
		if n%x==0:
			yield x
			yield n//x

def is_abundant(n):
	if n<12:
		return False
	return sum(divisors(n))>n

def is_abundant_sum(n):
	abundants_set = set(abundants_list)
	for i in abundants_list:
		if i>n:
			return False
		if (n-i) in abundants_set:
			return True
	return False

abundants_list = [x for x in range(1, 28123+1) if is_abundant(x)]
sum_of_non_abundants = sum(x for x in range(1, 28123 + 1) if not is_abundant_sum(x))
#abundants_set = set(abundants_list)
#print(abundants_list)
print(sum_of_non_abundants)
