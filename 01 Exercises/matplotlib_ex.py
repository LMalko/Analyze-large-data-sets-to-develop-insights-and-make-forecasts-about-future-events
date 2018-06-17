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


# OOP - Create canvas
fig = plt.figure()

                                    # LEFT, BOTTOM, WIDTH, HEIGHT.
axes1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])
axes2 = fig.add_axes([0.2, 0.5, 0.4, 0.3])

# plt.show()
axes1.plot(x, y)
axes2.plot(y,x)

axes1.set_xlabel("X Label")
axes1.set_ylabel("Y Label")

axes2.set_xlabel("X Label")
axes2.set_ylabel("Y Label")

axes1.set_title("This table")
axes2.set_title("That table")

# plt.show()
plt.close()

fig, axes = plt.subplots(nrows=3, ncols=3)
plt.tight_layout()

# plt.show()
plt.close()

fig, axes = plt.subplots(nrows=1, ncols=2)

for current_ax in axes:
    current_ax.plot(x, y)

axes[0].set_title("First axes")
axes[1].set_title("Second axes")

plt.show()




