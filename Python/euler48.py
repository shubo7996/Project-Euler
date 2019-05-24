"""
	problem 48- Last 10 digit of the sequence 1^1+2^2+3^3+...1000^1000
	@author-Subhamoy Paul

"""

def power():
	summ=0
	for i in range(1,1001):
		summ+=pow(i,i)
	return summ

sum_=power()
print(sum_)
TenDig=str(sum_)[-10:]
print("Last ten digits: {}".format(TenDig))