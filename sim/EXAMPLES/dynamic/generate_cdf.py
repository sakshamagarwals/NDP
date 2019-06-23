import sys
import numpy as np
import matplotlib.pyplot as plt

def find_cdf(data):

    data_size=len(data)

    # Set bins edges
    data_set=sorted(set(data))
    bins=np.append(data_set, data_set[-1]+1)

    # Use the histogram function to bin the data
    counts, bin_edges = np.histogram(data, bins=bins, density=False)

    counts=counts.astype(float)/data_size

    # Find the cdf
    cdf = np.cumsum(counts)
    return bin_edges[0:-1],cdf

inputfile = sys.argv[1]
input_data = list(np.loadtxt(inputfile))

X,Y = find_cdf(input_data)
stacked = np.column_stack((list(X),list(Y)))
np.savetxt(inputfile + '.cdf',stacked)

if(len(sys.argv) > 2):
    if(sys.argv[2] == 'P' or sys.argv[2] == 'p'): #also generate the cdf plot
        plt.plot(X,Y)
        plt.savefig(inputfile + '.cdf' + '.eps',format='eps',dpi=3000)

