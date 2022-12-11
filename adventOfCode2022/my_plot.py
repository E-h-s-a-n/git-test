import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

fig1, ax = plt.subplots()  # Create a figure containing a single axes.
# fig2, axs = plt.subplots(2, 2)  # a figure with a 2x2 grid of Axes

plt.xkcd()
ax.plot([1, 2, 3, 4], [1, 4, 2, 3]);  # Plot some data on the axes.
ax.scatter([0.5, 1, 1.5, 2], [1, 2, 1, 3], linewidths=2)
ax.set_title('Our Lovely ax of Fig1')
ax.grid(visible=True, axis='both', color='r', linewidth=1 )
ax.set_xlabel('x Axis Label')
ax.set_ylabel('y Axis Label')

plt.show()