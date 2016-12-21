# Matrix Algebra
import numpy as np
A = np.matrix('1,2,3;2,7,4')
B = np.matrix('1,-1;0,1')
C = np.matrix('5,-1;9,1;6,0')
D = np.matrix('3,-2,-1;1,2,3')
u = np.matrix('6,2,-3,5')
v = np.matrix('3,5,-1,4')
w = np.matrix('1;8;0;5')
A.shape
B.shape
C.shape
D.shape
u.shape
v.shape
w.shape
u+v
u-v
alpha = 6
alpha * u 
np.dot(u,v)
np.linalg.norm(u)
A + C
CT = C.transpose()
A - CT
CT + (3 * D)
np.dot(B, A)
AT = A.transpose()
np.dot(B, AT)
np.dot(B,C)
np.dot(C,B)
np.dot(A,AT)
DT = D.transpose()
np.dot(DT,D)
B**4
