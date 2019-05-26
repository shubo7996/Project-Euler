import math
import time

start=time.perf_counter()

def gcd(m,n):
	x,y=0,0
	if(m>n):
		x,y=m,n
	else:
		x,y=n,m
	while (x%y!=0):
		temp=x
		x=y
		y=temp%x

	return y

limit=1500000
triangles=[0]*(limit+1)

result=0
p=0
m_limit=int(math.sqrt(limit//2))

for x in range(2,m_limit):
	for y in range(1,x):
		if ((x+y)%2)==1 and gcd(y,x)==1:
			a=(x*x)+(y*y)
			b=(x*x)-(y*y)
			c=2*x*y
			p=a+b+c
			while(p<=limit):
				triangles[p]+=1
				if triangles[p]==1:
					result+=1
				if triangles[p]==2:
					result-=1
				p+=a+b+c


print(f"Result: {result}")

print(f"Time Elapsed:{time.perf_counter()-start}")