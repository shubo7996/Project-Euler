'''
    Solution-@Subhamoy Paul
'''

from numpy import matrix
import time

start=time.time()

matrix_ = list()
filepath='euler81.txt'

with open(filepath, 'r') as filehandle:  
    for line in filehandle:  
        currentPlace = line.split('\n')
        #res=list(map(int,currentPlace))
        res=list(currentPlace[0].split(','))
        final_res=list(map(int,res))
        matrix_.append(final_res)


#print(len(matrix_))
#print (type(list(map(int,places[0]))[0]))
final_matrix = matrix(matrix_)
print(f"Original Matrix:\n {final_matrix}")
print(f"Shape: {final_matrix.shape}")

matrix_size=final_matrix.shape[0]
#print(matrix_size)
for i in range(matrix_size-2,-1,-1):
    final_matrix[matrix_size-1,i]+=final_matrix[matrix_size-1,i+1]
    final_matrix[i,matrix_size-1]+=final_matrix[i+1,matrix_size-1]

for row in range(matrix_size-2,-1,-1):
    for col in range(matrix_size-2,-1,-1):
        #current_val=final_matrix[row,col]
        final_matrix[row,col]+=min(final_matrix[row+1,col],final_matrix[row,col+1])

print(f"Resultant Matrix:\n {final_matrix}")
print(f"Minimal Sum Path: {final_matrix[0,0]}")

print(f"Time Elapsed: {time.time()-start}")