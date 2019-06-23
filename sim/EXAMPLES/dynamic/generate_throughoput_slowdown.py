import sys
import numpy as np

inputfile = sys.argv[1]
pktsize = 1500 #int(sys.argv[4]) #in bytes
propagation_delay_in_ns = 800 #int(sys.argv[5])
link_bandwidth = 40 #int(sys.argv[6])

slowdownfile = inputfile + '.slowdown'
throughputfile = inputfile + '.throughput'

NUM_HOSTS = 144
slowdowns = []
tputs = []
total_data_hosts = [0.0 for i in range(NUM_HOSTS)]
min_start_time_hosts = [1000000.00 for i in range(NUM_HOSTS)]
max_finish_times_hosts = [-1.0 for i in range(NUM_HOSTS)]

with open(inputfile) as f:
    for line in f:
        tokens = line.split(',')
        flowsize = int(tokens[3])
        src = int(tokens[1])
        dst = int(tokens[2])
        arrival_time = float(tokens[4])
        fct = float((tokens[5].split())[0])
        finish_time = arrival_time + (fct/1000000.0)
        # tput = float((tokens[6].split())[0])/float(link_bandwidth)
        if (fct != -1): #could be -1 because of the weird way in which the file logs
            #calculate slowdown
            ideal_fct = ((flowsize*8.0)/link_bandwidth)/1e3 + 3*(((pktsize*8.0)/link_bandwidth)/1e3) + (propagation_delay_in_ns * 1e-3)
            slowdown = fct/ideal_fct
            if (slowdown < 1.0):
                slowdown = 1.0
            slowdowns.append(slowdown)

            total_data_hosts[src] += flowsize
            if(arrival_time < min_start_time_hosts[src]):
                min_start_time_hosts[src] = arrival_time
            if(finish_time > max_finish_times_hosts[src]):
                max_finish_times_hosts[src] = finish_time

for i in range(NUM_HOSTS):
    tputs.append( (total_data_hosts[i] * 8.0) / (link_bandwidth * 1000000000.0 * (max_finish_times_hosts[i] - min_start_time_hosts[i])) )

np.savetxt(slowdownfile,slowdowns)
np.savetxt(throughputfile,tputs)
