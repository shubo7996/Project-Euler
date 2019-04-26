import math
from fractions import Fraction
import decimal 

def compute_precision(x,y):
    '''
        Computes decimal precison upto 100
    '''
    with decimal.localcontext() as ctx:
        ctx.prec=100
        division= decimal.Decimal(x)/decimal.Decimal(y)
    return division
    

    
for x in range(1,101):
    #check if sq root of a number is rational or not
    if (math.sqrt(x)-int(math.sqrt(x))):
        #convert the sq root into fraction form
        fract_tup=Fraction(math.sqrt(x))
        #numerator and denominator of the above resultant fraction passed as parameters
        dec_=compute_precision(fract_tup.numerator,fract_tup.denominator)
        #converting the decimal value into an array of int and decimal
        arr=str(dec_).split('.')
        print(x,"------>",arr)

