import sys
import numpy as np

INPUT_FILE = sys.argv[1]
OUTPUT_FILE = INPUT_FILE + '.result'

input_data = np.loadtxt(INPUT_FILE)
input_data_mean = input_data.mean()
input_data_90_ptile = np.percentile(input_data,90)
input_data_99_ptile = np.percentile(input_data,99)

outfile = open(OUTPUT_FILE,'w')
outfile.write(str(input_data_mean) + '\n')
outfile.write(str(input_data_90_ptile) + '\n')
outfile.write(str(input_data_99_ptile) + '\n')
outfile.close()

