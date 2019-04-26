'''
#This Solution calculates precision upto just 100 decimal places

Solution- @Subhamoy Paul 

'''
import math
import decimal 
import time

start=time.perf_counter()

def compute_precision(x):
    '''
        Computes decimal precison upto 100
    '''
    with decimal.localcontext() as ctx:
        ctx.prec=102
        division= decimal.Decimal(x).sqrt()
    return division
    

sum_=0    
for x in range(1,101):
    #check if sq root of a number is rational or not
    if (math.sqrt(x)-int(math.sqrt(x))):
        dec_=compute_precision(x)
        arr=str(dec_).split('.')
        #new_arr2_sum=arr[1][1:99]
        #print(x,"---->",sum(map(int,list(new_arr2_sum))))
        #print(x,"------>",sum(list(map(int,list(arr[0]+arr[1])))))
        sum_+=sum(list(map(int,list(arr[0]+arr[1][0:99]))))

print("Result is:",sum_)
print(f"Time Elapsed: {time.perf_counter()-start}")