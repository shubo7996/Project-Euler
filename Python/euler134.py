'''
Solved using Modular Inverse and Extended Euclidean Algorithm

10**d(p1)*x+p1 == 0 (mod p2)
10**d(p1)*x == (p2-p1) (mod p2)
ax == b (mod n)

Example:

**17x == 1 (mod 43)**

x=17**-1 (mod 43)
43 = 17*2 + 9
17 = 9*1 + 8
9 = 8*1 + 1

here, GCD(43,17)=1. We can only find Inverse when GCD(x,y)=1

Since GCD(43,17) = 1, we can move forward to the Extended Euclidean Algorithm

1 = 9-8
sub 8:
    8 = 17 - 9
1 = 9 - (17-9)
1 = 2*9 - 17
sub 9:
    9 = 43 - 17*2
1 = 2*(43 - 17*2) - 17
1 = 2*43 - 17*4 - 17*1
1 = 2*43 + (-5)*17
17**-1(mod 43) == -5 == 38

17x = 1 (mod 43)
    x=38


'''



import math
import time
def generatePrime(n):
    primeList=[True]*(n+1)
    primeNumbers=[]
    p=2
    while(p*p<=n):
        if primeList[p]:
            i=p*2
            while i<=n:
                primeList[i]=False
                i+=p
        p+=1
    for x in range(2,n+1):
        if primeList[x]:
            primeNumbers.append(x)

    return primeNumbers[2:]
    #return _makeConsequetivePrime(primeNumbers)

#def _makeConsequetivePrime(PrimeList):
#    primeTuple=list(tuple())
#    for x in range(1,len(PrimeList)-1,2):
#        primeTuple.append((PrimeList[x],PrimeList[x+1]))
#    return primeTuple

def countDigits(num):
    return 10**len(str(num))

def extended_euclidean(a,b):
    x,prevX=0,1
    y,prevY=1,0
    while a!=0:
        quo_,rem_=b//a,b%a
        m,n=x-quo_*prevX,y-quo_*prevY
        b,a,x,y,prevX,prevY=a,rem_,prevX,prevY,m,n
        gcd=b
    return [x,y,gcd]


def process():
    i,sum_=0,0
    prime=generatePrime(1_000_050)
    while (prime[i]<=1_000_000):
        p1,p2=prime[i],prime[i+1]
        digitsInP1=countDigits(p1)
        rs=extended_euclidean(digitsInP1,p2)
        x=rs[0]*(p2-p1)%p2
        if x<0:
            x=p2+x
    #     lengthP1=len(str(p1))
    #     for y in range(1,11):
    #         if str((p2*y)%10)==str(p1)[-1]:
    #             num=y
    #             break
    #
    #     z=1
    #     while z>0:
    #         val=(num*p2)
    #         if str(val)[-lengthP1:]==str(p1):
    #             _sum+=val
    #             break
    #         z+=10
    #     x+=1
        sum_+=x*digitsInP1+p1
        i+=1
    print(sum_)

if __name__ == '__main__':
    start=time.perf_counter()
    process()
    #print(countDigits(23643287))
    #print(extended_euclidean(71,73))
    print(f"Time Taken:{time.perf_counter()-start}")
