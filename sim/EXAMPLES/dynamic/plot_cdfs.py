import sys
import numpy as np 
import matplotlib.pyplot as plt 

NUM_FILES = (len(sys.argv) - 1)/2
assert(NUM_FILES >= 1)

FILES = []
LABELS = []
COLORS = ['red','green','blue','pink','purple','black']

for i in range(NUM_FILES):
    FILES.append(sys.argv[2*i + 1])
    LABELS.append(sys.argv[2*i + 2])

XLABEL = raw_input("\nEnter xbabel:\n")
YLABEL = raw_input("\nEnter ylabel:\n")
TITLE = raw_input("\nEnter title:\n")
PLOT_NAME = raw_input("\nEnter plot file name (wrt current dir):\n")

for i in range(NUM_FILES):
    stacked = np.loadtxt(FILES[i])
    X = stacked[:,0]
    Y = stacked[:,1]
    plt.plot(X,Y, color=COLORS[i], label=LABELS[i], linewidth=2)
    #plt.xscale('log')
    plt.xlim(0.1,1)
    plt.grid(True)
    plt.xlabel(XLABEL)
    plt.ylabel(YLABEL)
    plt.title(TITLE)
    plt.legend(loc='lower right')
plt.savefig(PLOT_NAME, format = 'eps', dpi = 1000)
