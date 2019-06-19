import sys
import heapq

class Vertex(object):

	def __init__(self,node):
		self.id=node
		self.adjacent={}
		self.distance=sys.maxint #Set distance to infinity for all nodes
		self.visited=False #Marking all the  nodes invisited
		self.previous=None #Previous node

	def __str__(self):
		return str([x.id for x in self.adjacent])

	def add_neighbours(self,neighbour,weight):
		self.adjacent[neighbour]=weight

	def get_connections(self):
		return self.adjacent.keys()

	def get_id(self):
		return self.id

	def get_weight(self,neighbour):
		return self.adjacent[neighbour]

	def set_distance(self,dist):
		self.distance=dist

	def get_distance(self):
		return self.distance


class Graph(object):

	def __init__(self,graph_dict=None):
		if graph_dict==None:
			graph_dict={}
		self.__graph_dict = graph_dict
		self.num_vertices=0

	def __iter__(self):
		return iter(self.__graph_dict.values())

	def get_vertices(self):
		return list(self.__graph_dict.keys())

	def add_vertex(self,node):
		self.num_vertices+=1
		new_vertex=Vertex(node)
		#if node not in self.__graph_dict:
		#	self.__graph_dict[node]=[new_vertex]
		self.__graph_dict[node]=new_vertex
		return new_vertex

	def get_vertex(self,n):
		if n in self.__graph_dict:
			return self.__graph_dict[n]
		else:
			return None

	def add_edge(self,start,end,cost=0):
		if start not in self.__graph_dict:
			self.add_vertex(start)
		if end not in self.__graph_dict:
			self.add_vertex(end)

		self.__graph_dict[start].add_neighbours(self.__graph_dict[end],cost)
		self.__graph_dict[end].add_neighbours(self.__graph_dict[start],cost)
		# (vertex1,vertex2)=tuple(edge)
		# if vertex1 in self.__graph_dict:
		# 	self.__graph_dict[vertex1].append(vertex2)
		# else:
		# 	self.__graph_dict[vertex1]=vertex2

	def set_previous(self,current):
	 	self.previous=current

	def get_previous(self,current):
		return self.previous


def dijkstra(graph_,start_node):

	print("Dijkstra' Shortest Path: ")
	
	''' Set The Distance for the start node to be zero'''
	start_node.set_distance(0)

	'''Putting Tuple Pair into Priority Queue'''
	unvisited_queue=[(v.get_distance(),v) for v in graph_]
	heapq.heapify(unvisited_queue)










if __name__ == '__main__':
	
	graph_obj=Graph()

	Vertices = ["A","B","C","D","E","F"]
	for each_vertex in Vertices:
		graph_obj.add_vertex(each_vertex)
		
	graph_obj.add_edge("A","B",16)
	graph_obj.add_edge("A","C",12)
	graph_obj.add_edge("A","D",21)
	graph_obj.add_edge("B","D",17)
	graph_obj.add_edge("B","E",20)
	graph_obj.add_edge("C","D",28)
	graph_obj.add_edge("C","F",31)
	graph_obj.add_edge("D","E",18)
	graph_obj.add_edge("D","F",19)
	graph_obj.add_edge("D","G",23)
	graph_obj.add_edge("E","G",11)
	graph_obj.add_edge("F","G",27)


	for v in graph_obj:
		for w in v.get_connections():
			vID=v.get_id()
			wID=w.get_id()
			print(f"{vID} " + "---> " + f"{wID} " + "has weight "+ f"{v.get_weight(w)} ")


	for v in graph_obj:
		print(f"__graph_dict[{v.get_id()}]" + "= " + f"{v}")

