import matplotlib.pyplot as plt
import numpy as n

x = n.random.normal(0,30,1000)
y = n.random.normal(0,50,1000)
x=[4,2,1,4]
y=[8,5,2,1]
plt.scatter(x,y)
plt.show()