import numpy as np

arr = np.arange(1,25) #1d array of values 1-24
print(arr)
arr = arr.reshape((3,8)) #2d array, 3x8
print(arr)
arr = arr.reshape((2,3,4)) #3d array, 2x3x4
print(arr)
arr = arr.reshape((6,4)) #2d array, 6x4
print(arr)

colsum = arr.sum(axis = 0) #sum down each column
print(colsum)
rowsum = arr.sum(axis = 1) #sum down each row
print(rowsum)
rowmax = arr.max(axis = 1) #max values from each row
print(rowmax)
colmean = arr.mean(axis = 0) #mean caluculated down each column
print(colmean)