import numpy as np


def minum(x):
    if len(x) == 1:
        return x[0]
    
    next = minum(x[1:])

    if next < x[0]: return next
    else: return x[0]

liste = np.random.uniform(0,1000,995)

print(minum(liste))