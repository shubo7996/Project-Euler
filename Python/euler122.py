import time
import sys

class AdditionChain(object):

	def __init__(self):
		self.limit=200
		self.cost=[sys.maxsize]*(self.limit+1)
		self.path=[0]*(self.limit+1)

	def backtrack(x,n):
		if (x>self.limit or n>self.cost[x]):
			return
		self.cost[x]=n
		self.path[n]=x
		for y in range(n,-1,-1):
			self.backtrack(x+self.path[y],n+1)
	
	def brute():
		self.backtrack(1,0)
		return sum(self.cost[1:])

if __name__ == '__main__':
	start=time.perf_counter()
	add_chain=AdditionChain().brute()
	print(add_chain)
	print(f"Time Elapsed: {time.perf_counter()-start}")
