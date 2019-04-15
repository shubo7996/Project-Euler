from collections import OrderedDict

start=time.perf_counter()

def isPrime(n):
    if (n <= 1):
    	return False
    if (n == 2):
    	return True
    if (n % 2 == 0):
    	return False
    if (n < 9):
    	return True
    if (n % 3 == 0):
    	return False
            
    counter = 5;            
    while((counter * counter) <= n):
        if (n % counter == 0):
        	return False
        if (n % (counter + 2) == 0):
        	return False;
        counter += 6
            

    return True
        
'''
Determine and count the primes, pn, in the series ignoring every 4th one since it will always be a square and 
therefore composite.
As soon as we reach a ratio of (primes to series length (n)), pn/n < 10% we can calculate a side length as n/2.

'''

i=0
#counter=0
prime_dict=OrderedDict()
key=('top_right','top_left','bottom_left','bottom_right')
prime_list=[]
all_numbers=[1]
ratio=1
interval=1
while ratio>0.1:
	bottom_right=i**2
	bottom_left=(i**2-i)+1
	top_left=(i**2)-(2*i)+2
	top_right=(i**2)-(3*i)+3
	#prime_dict[(key,i)]=(top_right,top_left,bottom_left,bottom_right)
	#if isPrime(i):
	#	counter+=3
	#	prime_list.extend((bottom_right,bottom_left,top_left))
	#	all_numbers.append(i)
	#	ratio=float((len(prime_list)/len(all_numbers)))
	#	if ratio<10:
	#		print(i//2)
	#		break
	#	else:
	#		continue
	#else:
	#	i+=1
	
	for x in range(4):
		i+=interval
		current_number=2*i+1
		all_numbers.append(current_number)
		if isPrime(current_number):
			prime_list.append(current_number)
			prime_dict[(key,i)]=(top_right,top_left,bottom_left,bottom_right)
	ratio=float(len(prime_list))/len(all_numbers)
	interval+=1
	

print(prime_dict)
print (f"Result:{int(((2*i+1)**0.5))}")		
print(f"Time Elapsed: {time.perf_counter()-start}")