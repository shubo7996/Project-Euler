'''@solution-Subhamoy Paul'''

import time
import math

dimension_list=[]
start=time.perf_counter()
min_diff=int(2E6)
for x in range(1,101):
	for y in range(1,101):
		#number of rectangles formed in a x*y dimension rectangle is calculated by the formula - ((x^2)+x*(y^2)+y)/4
		num_of_rect=(((x*x)+x)*((y*y)+y))//4 #where x and y are dimensions
		diff=math.fabs(num_of_rect-int(2E6))
		if diff<min_diff:
			dimension_list.append((x,y))
			area,min_diff=x*y,diff

print(dimension_list[-1])
#final_x,final_y=a,b for a,b in dimension_list[-1]]
#print(final_x,final_y)
print("Result: {}".format(area))
print("Time Elapsed: {}".format(time.perf_counter()-start))
