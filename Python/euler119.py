# import math
# from Euler_Prime import isPrime
import time
power_list=[]
#i=11
start=time.perf_counter()
for x in range(9,100):
	val=1
	for _ in range(2,x//2):
		val*=x
		if sum(map(int,str(val)))==x:
			power_list.append(val)
	if len(power_list)==50:
		break
print(sorted(power_list)[1:][27])
end=time.perf_counter()
print(f"Time Elapsed: {end-start}")
# while True:
# 	if (isPrime(i)):
# 		i+=1
# 	else:
# 		sum_=sum(map(int, str(i)))
# 		pow_=int(math.log10(i))
# 		if (pow(sum_,(pow_+1))==i or pow(sum_,(pow_-1))==i):
# 			print(i)
# 			power_list.append(i)
# 		if len(power_list)==30:
# 			break
# 		i+=1
# print(power_list)


# '''

# 	s = sum of digits;
#     if(s*n is perfect square)
# 	print;
#     else if(s*s*n) is a perfect square:
#     	print


# '''