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

    year = 1983
    plt.title('U.S. Oil Reserves: 1983-2012', color='w', weight='bold')

    # Subtitles in a graph
    # http://stackoverflow.com/questions/1388450/giving-graphs-a-subtitle-in-matplotlib

    plt.figtext(.5,.04,'Oil Reserves as measured in terms of Millions of Barrels ',fontsize=10,ha='center')
    plt.figtext(.5,.01,'Red  < 40% of max capacity, Orange  < 70% of max capacity, Blue  < 90% of max capacity',fontsize=10,ha='center')

    # Adding text to a rectangle
    # http://stackoverflow.com/questions/14531346/how-to-add-a-text-into-a-rectangle

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
        # Plotting as rectangles
        rect = plt.Rectangle([x - size / 2.5, y - size / 2], size, size,
                             facecolor=color, edgecolor=color, label = "X")
        ax.add_patch(rect)

        rx, ry = rect.get_xy()
        cx = rx + rect.get_width()/2.0
        cy = ry = rect.get_height()/2.0

        ax.annotate(year, (x  - size/4, y + size/3), color='w', weight='bold')
        year += 1
        # Plotting as circles
        # circle1=plt.Circle((w,w),.2,color=color)
        # fig = plt.gcf()
        # print fig
        # print fig.gca()
        # fig.gca().add_artist(circle1)

    ax.autoscale_view()
    ax.invert_yaxis()
    ax.plot(label = "U.S. Oil Reserves")


if __name__ == '__main__':
# #	plt.show()
# 	print np.random.rand(20, 20) - 0.5
	hinton(matrix)
	plt.show()
# # How do you map to a shared row/column, other than the above, which takes too long