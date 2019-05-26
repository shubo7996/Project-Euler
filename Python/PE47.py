def countable(x):
	twice_x = set(list(str(x*2)))
	thrice_x = set(list(str(x*3)))
	four_x= set(list(str(x*4)))
	five_x= set(list(str(x*5)))
	six_x= set(list(str(x*6)))
	if twice_x==thrice_x and thrice_x==four_x and four_x==five_x and five_x==six_x and six_x==twice_x:
		return True

min_=10000000
for num in range(100000,1000000):
	if countable(num):
		if num<min_:
			min_=num
print(min_)
