import time
from collections import Counter

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
            if len(str(x))-len(set(str(x)))>=3:
                primeNumbers.append(x)
    
    return primeNumbers

primes=generatePrime(1_000_000)
check_list=list()

def findRepeatAndReplace(num):
    num_string=str(num)
    final=list()
    for x in (Counter(num_string)-Counter(set(num_string))):
        num_list=['0','1','2','3','4','5','6','7','8','9']
        nested=[int(num_string.replace(x,each)) for each in num_list]
        final.append(nested)
    return final

def remove_composite(comb_list):
    for x in comb_list:
        check_list.append(x)
        if x not in primes:
            comb_list.remove(x)
    return comb_list

x=0
flag=True
while flag:
    if primes[x] not in check_list:
        find_replacement=findRepeatAndReplace(primes[x])
        for y in find_replacement:
            if len(remove_composite(y))==8:
                print(y[0])
                flag=False
                break
    x+=1



    