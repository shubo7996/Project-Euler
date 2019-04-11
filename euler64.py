import math
import time

start_time= time.perf_counter() 

def recurse(a,conv_list):
  if len(conv_list)==100:
    return conv_list
  else:
    a=(1/(a-int(a)))
    conv_list.append(int(a))
    return recurse(a,conv_list)

counter=0
for x in range(1,10001):
  if math.sqrt(x)-int(math.sqrt(x)):
    num=math.sqrt(x)
    a0=int(num)
    converge_list=[a0]
    final_list=recurse(num,converge_list)
    #print(f"{x}---->{final_list}")
    if a0*2 in final_list:
      period=final_list.index(a0*2)
    if period%2!=0:
      counter+=1

print(f"Counter for Odd Periods: {counter}")

print(f"Time Elapsed: {time.perf_counter()-start_time}")