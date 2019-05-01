import math
import time

start=time.perf_counter()
n=20
result=math.factorial(2*n)//(math.factorial(n)**2)
print(result)
print(f"Time Elapsed: {time.perf_counter()-start}")