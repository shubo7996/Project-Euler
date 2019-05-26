import time

start= time.perf_counter()

'''
	--> a/b=3/7 such that p/q <= a/b
	--> p*b <= q*a
	--> p = (q*a-1)/b [-1 so that eq doesnt become equal]
	--> r/s < p/q

'''

a,b,r,s=3,7,0,1

for q in range(2,int(1E6)):
	p=(a*q-1)//b
	if((p*s)>(r*q)):
		s=q
		r=p

print(f"{r}/{s}")

print(f"Time Elapsed: {time.perf_counter()-start}")