def square():
	square_dict={}
	for x in range(32,100):
		if x not in square_dict.keys():
			square_dict[x]=x**2
	return square_dict

def triangle():
	triangle_dict={}
	for x in range(45,141):
		if x not in triangle_dict.keys():
			triangle_dict[x]=(x*(x+1))//2
	return triangle_dict

def pentagon():
	pentagon_dict={}
	for x in range(26,82):
		if x not in pentagon_dict.keys():
			pentagon_dict[x]=x*((3*x)-1)//2
	return pentagon_dict

def hexagon():
	hexagon_dict={}
	for x in range(23,71):
		if x not in hexagon_dict.keys():
			hexagon_dict[x]=x*((2*x)-1)
	return hexagon_dict

def heptagon():
	heptagon_dict={}
	for x in range(21,64):
		if x not in heptagon_dict.keys():
			heptagon_dict[x]=x*((5*x)-3)//2 	
	return heptagon_dict

def octagon():
	octagon_dict={}
	for x in range(19,59):
		if x not in octagon_dict.keys():
			octagon_dict[x]=x*((3*x)-2) 	
	return octagon_dict

sq=square()
print("Square ---->", sq)
print("----------------------"*15)
tri=triangle()
print("Triangle ----->", tri)
print("----------------------"*15)
pent=pentagon()
print("Pentagon----->", pent)
print("----------------------"*15)
hex=hexagon()
print("Hexagon----->", hex)
print("----------------------"*15)
hept=heptagon()
print("Heptagon---->", hept)
print("----------------------"*15)
octa=octagon()
print("Octagon---->", octa)

final_sum=0
c=1
for octa_val in octa.values():
	for hex_val in hex.values():
		if int((str(octa_val)[-2:]))==int((str(hex_val)[0:2])):
			for pent_val in pent.values():
				if int((str(hex_val)[-2:]))==int((str(pent_val)[0:2])):
					for tri_val in tri.values():
						if int((str(pent_val)[-2:]))==int((str(tri_val)[0:2])):
							for sq_val in sq.values():
								if int((str(tri_val)[-2:]))==int((str(sq_val)[0:2])):
									for hept_val in hept.values():
										if int((str(sq_val)[-2:]))==int((str(hept_val)[0:2])):
											if c==1:
												print(sq_val,tri_val,pent_val,hept_val,hex_val,octa_val)
												final_sum=sq_val+tri_val+pent_val+hept_val+hex_val+octa_val
											c-=1

							
print(final_sum)