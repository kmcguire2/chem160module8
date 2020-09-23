import numpy as np
from numpy.linalg import matrix_power

P = np.matrix([[0.25,0.40],[0.75,0.60]]) #transistion matrix
print(P)
N = np.matrix([[50],[50]]) #initial state vector
print(N)

N = P*N #state vector one hour in the future
print(N)

P10 = matrix_power(P,10) #projection matrix to the 10th power
N = P10*N #state projected 10 hours in the furture
print(N)

N = P10*N #state projected 10 hours in the furture
print(N)