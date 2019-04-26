import math
from fractions import Fraction
import decimal 

def compute_precision(x,y):
    with decimal.localcontext() as ctx:
        ctx.prec=200
        division= decimal.Decimal(x)/decimal.Decimal(y)
    return division
    

    
for x in range(1,101):
    if (math.sqrt(x)-int(math.sqrt(x))):
        fract_tup=Fraction(math.sqrt(x))
        dec_=compute_precision(fract_tup.numerator,fract_tup.denominator)
        arr=str(dec_).split('.')
        print(x,"------>",arr)

