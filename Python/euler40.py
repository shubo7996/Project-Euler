"""
	d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
"""

strg=''
prod_=1
for x in range(1,1000000):
	strg+=str(x)
#print(strg)
#print(len(strg))
prod_=int(strg[0])*int(strg[9])*int(strg[99])*int(strg[999])*int(strg[9999])*int(strg[99999])*int(strg[999999])
print(prod_)