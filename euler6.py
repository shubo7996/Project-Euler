def main():
	sum_of_num=0
	pow_of_num=0
	square_of_sum=0
	for x in range(1,101):
		sum_of_num+=x
		pow_of_num+=pow(x,2)
	square_of_sum=pow(sum_of_num,2)
	print("Difference of {}-{} is {}".format(square_of_sum,pow_of_num,square_of_sum-pow_of_num))

if __name__ == '__main__':
	main()