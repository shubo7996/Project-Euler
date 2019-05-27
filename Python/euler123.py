from Euler_Prime import seive

prime_list=seive(400000)
#(pn−1)^n + (pn+1)^n is divided by pn^2.
for x in range(7038,len(prime_list)+1):
 	pn=prime_list[x]
 	
 	'''Computationally Slow'''

 	#if ((pow(pn-1,x+2)+pow(pn+1,x+2))%(pow(pn,2))>=10**10): 
 	#	print(x+2)
 	#	break

 	
 	'''Computationally Fast'''

 	if 2*pn*(x)>pow(10,10): 
 	 	print(x+2)
 	 	break
	




