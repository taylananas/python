import matplotlib.pyplot as plt
#[(4, -6), (6, -14), (14, -12), (8, -10)]
x = [4,14,14,8]
x.append(x[0])
y = [-6,-14,-12,10]
y.append(y[0])

plt.plot(x,y,"o-")
plt.grid()
plt.show()