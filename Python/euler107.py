import time
import sys

def readFile(filepath):
	matrix_ = list()
	with open(filepath, 'r') as filehandle:  
		for line in filehandle:  
			currentPlace = line.split('\n')
			res=list(currentPlace[0].split(','))
			final_res=list(map(str,res))
			final_list=[int(0) if x=='-' else int(x) for x in final_res]
			matrix_.append(final_list)

	return matrix_

class Graph():

	def __init__(self,vertices):
		self.Vertices=vertices

	def minKey(self,key,mstSet):
		min_=sys.maxsize
		for v in range(self.Vertices):
			if key[v]< min_ and mstSet[v]==False:
				min_=key[v]
				min_index=v
		return min_index

	def primMst(self):
		key=[sys.maxsize]*self.Vertices
		parent=[None]*self.Vertices
		key[0]=0
		mstSet=[False]*self.Vertices
		parent[0]=-1

		for c_out in range(self.Vertices):
			u=self.minKey(key,mstSet)
			mstSet[u]=True
			for v in range(self.Vertices):
				if self.graph[u][v]>0 and mstSet[v]==False and key[v]>self.graph[u][v]:
					key[v]=self.graph[u][v]
					parent[v]=u

		return key

if __name__ == '__main__':
	filepath='C:\\Users\\kiit1\\Documents\\Codes\\Project-Euler\\euler107.txt'
	adj_matrix=readFile(filepath)
	graph_obj=Graph(40)
	graph_obj.graph=adj_matrix
	keys=graph_obj.primMst()
	min_weight,total_weight=0,0
	for key in keys:
		min_weight+=key
	for x in range(0,len(adj_matrix)):
		for y in range(x+1,len(adj_matrix[x])):
			total_weight+=adj_matrix[x][y]
	print(total_weight-min_weight)
