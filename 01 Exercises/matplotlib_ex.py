import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(0, 5, 11)
y = x ** 2

plt.plot(x, y, 'r-')
plt.xlabel("X Label")
plt.ylabel("Y Label")
plt.title("This table")

# plt.show()

plt.subplot(1,2,1)
plt.plot(x,y,"r")

plt.subplot(1,2,2)
plt.plot(x,y,"b")

# plt.show()
plt.close()

fig = plt.figure()

axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])
axes.plot(x, y)

axes.set_xlabel("X Label")
axes.set_ylabel("Y Label")
axes.set_title("This table")

# plt.show()
plt.close()

fig = plt.figure()
                                    # LEFT, BOTTOM, WIDTH, HEIGHT.
axes1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])
axes2 = fig.add_axes([0.3, 0.3, 0.4, 0.3])

plt.show()
# axes.plot(x, y)
#
# axes.set_xlabel("X Label")
# axes.set_ylabel("Y Label")
# axes.set_title("This table")
