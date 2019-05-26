from numpy import matrix
import time

start=time.time()

matrix_ = list()
filepath='euler82.txt'

with open(filepath, 'r') as filehandle:  
    for line in filehandle:  
        currentPlace = line.split('\n')
        res=list(currentPlace[0].split(','))
        final_res=list(map(int,res))
        matrix_.append(final_res)

final_matrix = matrix(matrix_)
print(f"Original Matrix:\n {final_matrix}")
print(f"Shape: {final_matrix.shape}")

matrix_size=final_matrix.shape[0]
final_matrix_solution=[0]*(matrix_size)

#Initializing Array with the val of every 80th col of each row 
for x in range(0,matrix_size):
    final_matrix_solution[x]=final_matrix[x,matrix_size-1]

for x in range(matrix_size-2,-1,-1):
	#final_matrix[matrix_size-1,x]+=final_matrix[matrix_size-1,x+1]#right
    final_matrix_solution[0]+=final_matrix[0,x]
    for y in range(1,matrix_size):
        final_matrix_solution[y]=min(final_matrix_solution[y-1]+final_matrix[y,x],final_matrix[y,x]+final_matrix_solution[y])#down
    for i in range(matrix_size-2,-1,-1):
        final_matrix_solution[i]=min(final_matrix_solution[i],final_matrix_solution[i+1]+final_matrix[i,x])    
	
    #final_matrix[x,matrix_size-1]+=final_matrix[x+1,matrix_size-1]#down

#for x in range(matrix_size-2,-1,-1):
#    for y in range(matrix_size-2,-1,-1):
#        final_matrix[x,y]+=min(final_matrix[x-1,y],final_matrix[x,y+1])
            
print(final_matrix_solution)
print(min(final_matrix_solution))
# for row in range(matrix_size-1,-1,-1):
#     c=9
#     for col in range(matrix_size-1,-1,-1):
#         #current_val=final_matrix[row,col]
#         c-=1
#         if row==matrix_size-1:
#             if c%9==0:
#                 final_matrix[row,col]+=min(final_matrix[])
#             else:    
#                 final_matrix[row,col]+=min(final_matrix[row-1,col],final_matrix[row,col+1])
#         else:
#             final_matrix[row,col]+=min(final_matrix[row+1,col],final_matrix[row,col+1],final_matrix[row-1,col])

#print(final_matrix)