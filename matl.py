#encoding:utf-8
import matplotlib.pyplot as plt
x = [1, 10, 50]
y = [8.34, 74.26, 367.23]
z = [5.82, 28.75 ,129.44]

plt.plot(x, y, label='without result', color="red",linewidth=2)
plt.plot(x, z, label='with result')
plt.xlabel('Tasks(w)')
plt.ylabel('Mem(m)')
plt.show()

