import math

def totient(n):
    from sympy import factorint
    fact_dict=factorint(n)
    phi_=1
    for key,val in fact_dict.items():
        phi_*=key**val-key**(val-1)
    return phi_

min_= 10
temp_var=0
for x in range(8000000,9000000):
    phi_=totient(x)
    set1=set(list(str(x)))
    #print(set1)
    set2=set(list(str(phi_)))
    #print(set2)
    if set1==set2:
        #print(x)
        if (x/phi_)<min_:
            min_=x/phi_
            temp_var=x
print(temp_var,"--->",min_)




