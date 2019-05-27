import math
from itertools import product

def tupcomb(nums):
    return list(product(*((x, -x) for x in nums)))

def count_lattice_points():
	for x in range(1,radius):
		y_sq=radius*radius-x*x
		y=int(math.sqrt(y_sq))
		if y*y==y_sq:
			 make_final_list=tupcomb([x,y])
			 lattice_points.extend(make_final_list)

	return lattice_points

radius=5
origin,orthocentre=(0,0),[(5,0),(-5,0),(0,5),(0,-5)]
lattice_points=[(radius,0),(-radius,0),(0,radius),(0,-radius)]
lattice_points.extend(orthocentre)


lat_points=count_lattice_points()
print(lat_points)
print("No of lattice_points: {}".format(len(lat_points)))
#for x in range(0,len(lat_points)):


		