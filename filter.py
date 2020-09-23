import numpy as np
def neighbors(arr,x,y,n):
    arr=np.roll(np.roll(arr,shift=-x+n//2,axis=0),shift=-y+n//2,axis=1)
    return arr[:n,:n]
N=10 #size of image
window=5 #filtering window size
loops=5

ar = np.random.choice((0,5),(N,N))
print(ar)

newar = np.zeros((N,N)) #empty array to store a copy of the filtered array
np.set_printoptions(precision = 3) #3 decimal places
print(ar)

for loop in range(loops):
    for i in range(N):
        for j in range(N):
            newar[i][j] = np.mean(neighbors(ar, i, j, window))
    ar = np.copy(newar)
    print(ar)