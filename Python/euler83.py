import numpy as np

'''
	Read File into a 2D Matrix
'''
filepath='C:\\Users\\kiit1\\Documents\\Codes\\Project-Euler\\euler83.txt'
matrix_ = list()
with open(filepath, 'r') as filehandle:  
	for line in filehandle:  
		currentPlace = line.split('\n')
		res=list(currentPlace[0].split(','))
		final_res=list(map(int,res))
		matrix_.append(final_res)


matrix=np.matrix(matrix_)

''' Global Variables '''

ROW,COL=matrix.shape[0],matrix.shape[1]
visited=np.matrix([[False]*COL]*ROW)	
row_queue,col_queue=[],[]
row_,col_=0,0
reached_dest=False
#minimal_sum=matrix[row_,col_]
#move_count=0
#nodes_left_in_layer, nodes_in_next_layer=1,0

direction_row=[-1,+1,0,0]
direction_col=[0,0,+1,-1]
	

def find_minimal_path_using_bfs():	
	nodes_left_in_layer, nodes_in_next_layer=1,0
	move_count=0
	row_queue.append(row_)
	col_queue.append(col_)
	visited[row_,col_]=True
	while len(row_queue)>0:
		r=row_queue.pop(0)
		c=col_queue.pop(0)
		if matrix[r,c]==matrix[ROW-1,COL-1]:
			reached_dest=True
			break
		explore_neighbours(r,c)
		nodes_left_in_layer-=1
		if nodes_left_in_layer==0:
			nodes_left_in_layer=nodes_in_next_layer
			nodes_in_next_layer=0
			move_count+=1
	if reached_dest:
		return move_count
	return-1

def explore_neighbours(r,c):
	nodes_in_next_layer=0
	for x in range(0,4):
		rr=r+direction_row[x]
		cc=c+direction_col[x]

		#skipping out of bound location
		if rr<0 or cc<0:
			continue
		if rr>=ROW or cc>=COL:
			continue
		#Skipping visited location
		if visited[rr,cc]:
			continue

		row_queue.append(rr)
		col_queue.append(cc)
		visited[rr,cc]=True
		#print(matrix[rr,cc])
		nodes_in_next_layer+=1


def solve():
	count_=find_minimal_path_using_bfs()
	print(count_)

if __name__ == '__main__':
	solve()

