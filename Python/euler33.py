def gcd(a, b):
  while b > 0:
    a, b = b, a % b
  return a

def soln():
 	dp,np=1,1
 	for c in range(1,10):
 		for d in range(1,c):
 			for n in range(1,d):
 				if (n*10+c)*d==(c*10+d)*n:
 					np*=n
 					dp*=d
 	return dp//gcd(np,dp)

sol_=soln()
print(sol_)