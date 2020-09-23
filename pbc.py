import numpy as np

def neighbors(arr, x, y, n):
    arr = np.roll(np.roll(arr,shift = -x+n//2, axis = 0), shift = -y+n//2, axis = 1)
    return arr[:n, :n]

a = np.arange(0,100).reshape(10,10) #10x10 array of values 0-99
print(a)
print(neighbors(a,0,0,3)) #3x3 box of values around 0,0 - using pbc
print(neighbors(a,0,0,5)) #5x5 box of values around 0,0 - using pbc