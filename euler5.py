import time

start=time.perf_counter()
def gcd(a, b):
  while b > 0:
    a, b = b, a % b
  return a

def lcm(a, b):
  return (a * b) / gcd(a, b)

llcm = lcm(11, 12)
for n in range(12, 20):
  llcm = lcm(n, llcm)

print (llcm)


i = 1
for k in (range(1, 21)): 
  if i % k > 0: 
    for j in range(1, 21): 
      if (i*j) % k == 0: 
        i *= j 
        break 

print (i)
print(f"Time Elapsed: {time.perf_counter()-start}")