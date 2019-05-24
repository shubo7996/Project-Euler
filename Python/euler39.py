
#euler39
import time

start=time.perf_counter()

res=0
high=0
for p in range(2,1001,2):
  counter=0
  for a in range(2,p//3):
    if ((p*p)-(2*p*a))%((2*(p-a)))==0:
      counter+=1
  if counter>high:
    high=counter
    res=p

print(res)
print(f"Time Elapsed: {time.perf_counter()-start}")
