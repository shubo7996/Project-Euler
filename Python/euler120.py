sum_=0
for a in range(3,1001):
	if a%2:
		sum_+=a*(a-1)
	else:
		sum_+=a*(a-2)
print(sum_)