import matplotlib.pyplot as plt
import numpy as n

x = n.random.normal(0,30,1000)
y = n.random.normal(0,50,1000)

print(min(x), max(x))
print(min(y), max(y))

plt.scatter(y,x)
plt.grid()
plt.show()
