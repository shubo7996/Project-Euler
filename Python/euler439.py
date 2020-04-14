import time
from sympy import factorint
from sympy.ntheory import isprime
from collections import defaultdict
from itertools import product

start=time.perf_counter()

check_dict=defaultdict(int)

def primefactorization(num):
    return factorint(num)

def sumOfDivisors(base,exp):
    total=0
    for x in range(exp+1):
        total+=base**x
    check_dict[base**exp]=total
    return total

def calcComposite(comp_num):
    if comp_num==1:
        return 1
    if comp_num in check_dict:
        return check_dict[comp_num]
    else:
        primefact=primefactorization(comp_num)
        sumofdiv=1
        for k,v in primefact.items():
            if k**v in check_dict:
                sumofdiv*=check_dict[k**v]
            else:
                sumofdiv*=sumOfDivisors(k,v)
        check_dict[comp_num]=sumofdiv
        return check_dict[comp_num]

#primeFactors=primefactorization(6)
sumoffactors=1

#for k,v in primeFactors.items():
sumoffactors*=sum([(x*y)+1 if isprime(x*y) else calcComposite(x*y) for x in range(1,int(1E3)+1) for y in range(1,int(1E3)+1)])

#print(check_dict.items())

print(sumoffactors)
print(pow(sumoffactors,1,10**9))


print(f"Time Elapsed: {time.perf_counter()-start}")