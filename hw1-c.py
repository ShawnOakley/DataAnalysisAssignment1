# Resource: http://wiki.scipy.org/Cookbook/Matplotlib

import excelLoad as eL

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

array = (eL.total_petroleum_stocks.T['United States'].values[3:]/10000 - .12 ) / .07

matrix = array.reshape(6,5)


# QUESTION 3:
# Try to create a Hinton diagram, depicting consumption, positive or negative
# and degrees
# http://matplotlib.org/examples/specialty_plots/hinton_demo.html
# Main issue was just reformatting the dataframe into proper size/value range

def hinton(matrix, max_weight=None, ax=None):
    """Draw Hinton diagram for visualizing a weight matrix."""
    ax = ax if ax is not None else plt.gca()

    if not max_weight:
        max_weight = 2**np.ceil(np.log(np.abs(matrix).max())/np.log(2))

    ax.patch.set_facecolor('gray')
    ax.set_aspect('equal', 'box')
    ax.xaxis.set_major_locator(plt.NullLocator())
    ax.yaxis.set_major_locator(plt.NullLocator())

    for (x,y),w in np.ndenumerate(matrix):
    	if w < .4:
    		color = 'red'
    	elif w < .7:
    		color = 'orange'
    	elif w < .9:
    		color = 'blue'
    	else:
    		color = 'white'
        size = np.sqrt(np.abs(w))
        rect = plt.Rectangle([x - size / 2, y - size / 2], size, size,
                             facecolor=color, edgecolor=color)
        ax.add_patch(rect)

    ax.autoscale_view()
    ax.invert_yaxis()


if __name__ == '__main__':
# #	plt.show()
# 	print np.random.rand(20, 20) - 0.5
	hinton(matrix)
	plt.show()
# # How do you map to a shared row/column, other than the above, which takes too long