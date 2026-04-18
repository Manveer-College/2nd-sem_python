import matplotlib.pyplot as plt
import numpy as np
x = np.array([1,2,3,4,5])
y = x*x
plt.plot(x,y)
plt.title("Square of numbers")
plt.xlabel("X-axis")
plt.ylabel("X square")
plt.bar(x,y)
plt.show()