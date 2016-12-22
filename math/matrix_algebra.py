# Matrix Algebra
import numpy as np
A = np.matrix('1,2,3;2,7,4')
"""matrix([[1, 2, 3],
        [2, 7, 4]])"""
 
B = np.matrix('1,-1;0,1')
"""matrix([[ 1, -1],
        [ 0,  1]])"""
C = np.matrix('5,-1;9,1;6,0')
"""matrix([[ 5, -1],
        [ 9,  1],
        [ 6,  0]])"""
D = np.matrix('3,-2,-1;1,2,3')
"""matrix([[ 3, -2, -1],
        [ 1,  2,  3]])"""
u = np.matrix('6,2,-3,5')
"""matrix([[ 6,  2, -3,  5]])"""
v = np.matrix('3,5,-1,4')
"""matrix([[ 3,  5, -1,  4]])"""
w = np.matrix('1;8;0;5')
"""matrix([[1],
        [8],
        [0],
        [5]])"""
A.shape
"""(2, 3)"""
B.shape
"""(2, 2)"""
C.shape
"""(3, 2)"""
D.shape
"""(2, 3)"""
u.shape
"""(1, 4)"""
v.shape
"""(1, 4)"""
w.shape
"""(4, 1)"""
u+v
"""matrix([[ 9,  7, -4,  9]])"""
u-v
"""matrix([[ 3, -3, -2,  1]])"""
alpha = 6
alpha * u 
"""matrix([[ 36,  12, -18,  30]])"""
np.dot(u,v)
"""ValueError: shapes (1,4) and (1,4) not aligned: 4 (dim 1) != 1 (dim 0)
"""
np.linalg.norm(u)
"""8.6023252670426267"""
A + C
"""ValueError: operands could not be broadcast together with shapes (2,3) (3,2) 
"""
CT = C.transpose()
"""matrix([[ 5,  9,  6],
        [-1,  1,  0]])"""
A - CT
"""matrix([[-4, -7, -3],
        [ 3,  6,  4]])"""
CT + (3 * D)
"""matrix([[14,  3,  3],
        [ 2,  7,  9]])"""
np.dot(B, A)
"""matrix([[-1, -5, -1],
        [ 2,  7,  4]])"""
AT = A.transpose()
"""matrix([[1, 2],
        [2, 7],
        [3, 4]])"""
np.dot(B, AT)
"""ValueError: shapes (2,2) and (3,2) not aligned: 2 (dim 1) != 3 (dim 0)
"""
np.dot(B,C)
"""ValueError: shapes (2,2) and (3,2) not aligned: 2 (dim 1) != 3 (dim 0)
"""
np.dot(C,B)
"""matrix([[ 5, -6],
        [ 9, -8],
        [ 6, -6]])"""
np.dot(A,AT)
"""matrix([[14, 28],
        [28, 69]])"""
DT = D.transpose()
"""matrix([[ 3,  1],
        [-2,  2],
        [-1,  3]])"""
np.dot(DT,D)
"""matrix([[10, -4,  0],
        [-4,  8,  8],
        [ 0,  8, 10]])"""
B**4
"""matrix([[ 1, -4],
        [ 0,  1]])"""
