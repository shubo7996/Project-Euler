from numpy import matrix

def isValid(matrix,row,col,num):
	if not used_in_row and not used_in_col:
		return True
 
def used_in_row(matrix,row,num):
	for i in range(matrix.shape[0]):
		if matrix[row,i]==num:
			return True
		return False

def used_in_col(matrix,col,num):
	for i in range(matrix.shape[0]):
		if matrix[i,col]==num:
			return True
	return False


def isUniqueMatrix(matrix,size):
	'''Sum of elements in a row,col or 3*3 matrix is sum(1..9)=n*(n+1)/2=45'''
	sum_=0
	totalsum=size*(size+1)//2

	for x in range(size):
		sum_=0
		for y in range(size):
			if matrix[x,y]<1 or matrix[x,y]>size:
				return False
			sum_+=matrix[x,y]
		if sum_!=totalsum:
			return False

	for x in range(size):
		sum_=0
		for y in range(size):
			sum_+=matrix[y,x]
		if sum_!=totalsum:
			return False

	return True


def solve_sudoku(matrix):
	#l=[0,0]
	row,col=-1,-1
	needOperation=False
	# if not find_empty_location(matrix,l):
	# 	return True
	for x in range(matrix.shape[0]):
		for y in range(matrix.shape[0]):
			if matrix[x,y]==0:
				row,col=x,y
				needOperation=True
				break
		if(needOperation):
			break

	if not needOperation:
		if not isUniqueMatrix(matrix,matrix.shape[0]):
			return False
		return True

	for num in range(1,10):
		if isValid(matrix,row,col,num):
			matrix[row,col]=num
			if solve_sudoku(matrix):
				return True
			else:
				matrix[row,col]=0

	return False
	

def print_grid(matrix):
	for x in range(matrix.shape[0]):
		for y in range(matrix.shape[0]):
			print(matrix[x,y],end=' ')
		print('\n')

def main():
	#grid=[[0]*9]*9
	grid=matrix([[0,0,3,0,2,0,6,0,0],
		  [9,0,0,3,0,5,0,0,1],
		  [0,0,1,8,0,6,4,0,0],
		  [0,0,8,1,0,2,9,0,0],
		  [7,0,0,0,0,0,0,0,8],
		  [0,0,6,7,0,8,2,0,0],
		  [0,0,2,6,0,9,5,0,0],
		  [8,0,0,2,0,3,0,0,9],
		  [0,0,5,0,1,0,3,0,0]])
	#print(grid)
	if (solve_sudoku(grid)):
		print_grid(grid)
	else:
		print("No solution Found!")				


if __name__ == '__main__':
	main()