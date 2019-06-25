from numpy import matrix

def readFile(filepath):
	matrix_ = list()
	with open(filepath, 'r') as filehandle:  
		for line in filehandle:  
			currentPlace = line.split('\n')
			res=list(currentPlace[0].split(','))
			final_res=list(map(int,res))
			matrix_.append(final_res)

	return matrix(matrix_)

def find_minimal_path_using_bfs(matrix):
	minimal_sum=0
	visited={}	
	queue=[]
	row_,col_=0,0
	queue.append(matrix[0,0])
	visited[matrix[0,0]]=True
	des=matrix[79,79]

	while(queue):
		
		if col_>matrix.shape[0]-1:
			col_=0
			row_+=1
		
		element=queue.pop(0)
		minimal_sum+=element
		visited[element]=True

		if col_==0:
			queue.extend([matrix[row_,col_+1],matrix[row_+1,col_]])
			current_min=min(matrix[row_,col_+1],matrix[row_+1,col_])
			minimal_sum+=current_min
		elif col==matrix.shape[0]-1:
			queue.extend([matrix[row_,col_-1],matrix[row_+1,col_]])
			current_min=min(matrix[row_,col_-1],matrix[row_+1,col_])
			minimal_sum+=current_min
		else:
			queue.extend([matrix[row_,col_+1],matrix[row_+1,col_],matrix[row_-1,col_]])
			current_min=min(matrix[row_,col_+1],matrix[row_+1,col_],matrix[row_-1,col_])
			minimal_sum+=current_min
		current_position=[(ix,iy) for ix, row in enumerate(matrix) for iy, i in enumerate(row) if current_min]
		row_,col_=current_position[0]

		if visited[des]==True:
			break

	return minimal_sum


def main():
	file_path='C:\\Users\\kiit1\\Documents\\Codes\\Project-Euler\\euler83.txt'
	adj=readFile(file_path)
	result=find_minimal_path_using_bfs(adj)
	print(result)

if __name__ == '__main__':
	main()


