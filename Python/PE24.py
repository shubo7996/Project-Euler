def find_power_sum(n):
	sum_=0
	num_list=list(str(n))
	for x in num_list:
		sum_+=int(x)**5
	if sum_==n:
		return True

summ=0
for x in range(2,1000000):
	if find_power_sum(x):
		summ+=x

print(f'Sum: {summ}')