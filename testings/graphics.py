import matplotlib.pyplot as plt

x_array = []
y_array = []

for i in range(-50,50):
    x_array.append(i)
    y_array.append(i**2 -5*i + 6)

plt.scatter(x_array,y_array)
plt.show()