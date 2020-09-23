import time
import math
import numpy as np

trials = int(input("Enter the number of trials: "))
t = time.process_time()

x = np.square(np.random.random(trials)) #returns nd arrary with set of random values, squared
y = np.square(np.random.random(trials))
total = x + y #adds arrays together
inside = (total < 1.).sum() #returns the number of values that are
pi = 4.*inside/trials
et = time.process_time() - t
print("pi est =%9.6f error=%9.6f time=%f"%(pi, pi-math.pi, et))