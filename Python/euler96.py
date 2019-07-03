import time


# def isUniqueMatrix(matrix,size):

# 	'''Sum of elements in a row,col or 3*3 matrix is sum(1..9)=n*(n+1)/2=45'''

# 	sum_=0
# 	totalsum=size*(size+1)//2

# 	for x in range(size):
# 		sum_=0
# 		for y in range(size):
# 			if matrix[x,y]<1 or matrix[x,y]>size:
# 				return False
# 			sum_+=matrix[x,y]
# 		if sum_!=totalsum:
# 			return False

# 	for x in range(size):
# 		sum_=0
# 		for y in range(size):
# 			sum_+=matrix[y,x]
# 		if sum_!=totalsum:
# 			return False

# 	return True


# def isValidSudoku(matrix):

# 	for i in range(9):
# 		rowmap,colmap,gridmap={},{},{}
# 		for j in range(9):
			
# 			#row validation
# 			if matrix[i][j]==0 and matrix[i][j] in list(rowmap.keys()):
# 				if rowmap[matrix[i][j]]:
# 					return False
# 			else:
# 				rowmap[matrix[i][j]]=True
			
# 			#column validation
# 			if matrix[j][i]==0 and matrix[j][i] in list(colmap.keys()):
# 				if colmap[matrix[j][i]]:
# 					return False
# 			else:
# 				colmap[matrix[j][i]]=True
			
# 			#3*3 grid validation
# 			rowIndex=3*(i//3)
# 			colIndex=3*(i%3)
# 			rowIndex_val=rowIndex+j//3
# 			colIndex_val=colIndex+j%3
			
# 			if matrix[rowIndex_val][colIndex_val]==0 and matrix[rowIndex_val][colIndex_val] in list(gridmap.keys()):
# 				if gridmap[matrix[rowIndex_val][colIndex_val]]:
# 					return False
# 			else:
# 				gridmap[rowIndex_val][colIndex_val]=True
# 	# print(rowmap)
# 	# print(colmap)
# 	# print(gridmap)

# 	return True

	
	
def isValidRow(matrix,row,n):
	for x in range(0,9):
		if matrix[row][x]==n:
			return False
	return True

def isValidCol(matrix,col,n):
	for x in range(0,9):
		if matrix[x][col]==n:
			return False
	return True

def isValidBox(matrix,row,col,n):
	for x in range(3):
		for y in range(3):
			if matrix[x+row][y+col]==n:
				return False
	return True

def isPossible(matrix,row,col,n):
	return isValidRow(matrix,row,n) and isValidCol(matrix,col,n) and isValidBox(matrix,row-row%3,col-col%3,n)

def isSolved(matrix,l):
	for x in range(0,9):
		for y in range(0,9):
			if matrix[x][y]==0:
				l[0]=x
				l[1]=y
				return False
	return True

def solveSudoku(matrix):
	
	# row,col=-1,-1
	# needOperation=False

	# # if isSolved(matrix,l):
	# # 	return True
	
	# for x in range(9):
	# 	for y in range(0):
	# 		if matrix[x][y]==0:
	# 			row,col=x,y
	# 			needOperation=True
	# 			break
	
	# 	if(needOperation):
	# 		break

	# if not needOperation:
	# 	if not isUniqueMatrix(matrix,9):
	# 		return False
	# 	return True

	# for num in range(1,10):
	# 	if isValid(matrix,row,col,num):
	# 		matrix[row,col]=num
	
	# 		if solve_sudoku(matrix):
	# 			return True
	# 		else:
	# 			matrix[row,col]=0

	# return False
	
	l=[0,0]
	if isSolved(matrix,l):
		return True
	row,col=l[0],l[1]
	for x in range(1,10):
		if isValidSudoku(matrix):
			matrix[row][col]=x
			if solveSudoku(matrix):
				return True
			matrix[row][col]=0
	return False


def getMatrix():
	filepath='C:\\Users\\kiit1\\Documents\\Codes\\Project-Euler\\euler96.txt'
	temp_sudoku_matrix_list,perm_sudoku_matrix_list,counter=[],[],0
	with open(filepath,'r') as filehandle:
		for line in filehandle:
			if line[0]=='G':
				temp_sudoku_matrix_list=[]
			else:
				sudoku_line=list(map(int,list(line)[0:9]))
				temp_sudoku_matrix_list.append(sudoku_line)
				if len(temp_sudoku_matrix_list)==9:
					perm_sudoku_matrix_list.extend([temp_sudoku_matrix_list])
	return perm_sudoku_matrix_list

def main():
	sum_=0
	board=getMatrix()
	#print(board[1])
	for i in range(50):
		if solveSudoku(board[i]):
			sum_+=100*board[i][0][0]+10*board[i][0][1]+board[i][0][2]
	print(sum_)

	

if __name__ == '__main__':
	start=time.perf_counter()
	main()
	end=time.perf_counter()
	print(f"Time Elapsed:{end-start}")