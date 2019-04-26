
#This Solution calculates precision upto just 100 decimal places 

import math
from fractions import Fraction
import decimal 

def compute_precision(x):
    '''
        Computes decimal precison upto 100
    '''
    with decimal.localcontext() as ctx:
        ctx.prec=101
        division= decimal.Decimal(x).sqrt()
    return division
    

sum_=0    
for x in range(1,101):
    #check if sq root of a number is rational or not
    if (math.sqrt(x)-int(math.sqrt(x))):
        #convert the sq root into fraction form
        #fract_tup=Fraction(math.sqrt(x))
        #numerator and denominator of the above resultant fraction passed as parameters
        #dec_=compute_precision(fract_tup.numerator,fract_tup.denominator,100)
        dec_=compute_precision(x)
        #converting the decimal value into an array of int and decimal
        arr=str(dec_).split('.')
        #print(x,"------>",len(arr[1]))
        sum_+=sum(list(map(int,list(arr[1]))))

print(sum_)


"""
    #Using Square root by Subtraction


import math

def square_root(num,prec_limit):
    limit=math.pow(100,prec_limit+1)
    a,b=5*num,5

    while(b<limit):
        if a>b:
            a-=b
            b+=10
        else:
            a*=100
            b=(b//10)*100+5

    return b//100

def main():
    sum_=0
    precision=100
    for x in range(3,101):
        if (math.sqrt(x)-int(math.sqrt(x))):
            sum_+=sum(list(map(int,list(str(square_root(x,precision))))))
    print(sum_)

if __name__=='__main__':
    main()
"""