import sys
import numpy as np

inputfile = sys.argv[1]
pktsize = 1500 #int(sys.argv[4]) #in bytes
propagation_delay_in_ns = 200 #int(sys.argv[5])
link_bandwidth = 40 #int(sys.argv[6])

slowdownfile = inputfile + '.slowdown'
throughputfile = inputfile + '.throughput'

NUM_HOSTS = 144
slowdowns = []
tputs = []
inloads = []
total_data_hosts = [0.0 for i in range(NUM_HOSTS)]
min_start_time_hosts = [1000000.00 for i in range(NUM_HOSTS)]
max_finish_times_hosts = [-1.0 for i in range(NUM_HOSTS)]
max_start_times_hosts = [-1.0 for i in range(NUM_HOSTS)]

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
	    if(src/16 == dst/16):
                ideal_data_time = ((flowsize*8.0)/link_bandwidth)/1e3 + 1*(((pktsize*8.0)/link_bandwidth)/1e3) + (2 * propagation_delay_in_ns * 1e-3)
	        ideal_header_time = 2.0 * (8.0 * 40 / link_bandwidth)/1e3 + (2 * propagation_delay_in_ns * 1e-3)
	    else:
                ideal_data_time = ((flowsize*8.0)/link_bandwidth)/1e3 + 1*(((pktsize*8.0)/link_bandwidth)/1e3) + 2*(((pktsize*8.0)/(4*link_bandwidth))/1e3) + (4 * propagation_delay_in_ns * 1e-3)
	        ideal_header_time = 2.0 * (8.0 * 40 / link_bandwidth)/1e3 + 2.0 * (8.0 * 40 / (4 * link_bandwidth))/1e3  + (4 * propagation_delay_in_ns * 1e-3)
            
            ideal_fct = ideal_header_time + ideal_data_time	    
	    slowdown = fct/ideal_fct
	    
            if (slowdown < 1.0):
                slowdown = 1.0
		assert(false)
            slowdowns.append(slowdown)

            total_data_hosts[src] += flowsize
            if(arrival_time < min_start_time_hosts[src]):
                min_start_time_hosts[src] = arrival_time
            if(finish_time > max_finish_times_hosts[src]):
                max_finish_times_hosts[src] = finish_time
            if(arrival_time > max_start_times_hosts[src]):
                max_start_times_hosts[src] = arrival_time

for i in range(NUM_HOSTS):
    tputs.append( (total_data_hosts[i] * 8.0) / (link_bandwidth * 1000000000.0 * (max_finish_times_hosts[i] - min_start_time_hosts[i])) )
    inloads.append( (total_data_hosts[i] * 8.0) / (link_bandwidth * 1000000000.0 * (max_start_times_hosts[i] - min_start_time_hosts[i])) )

np.savetxt(slowdownfile,slowdowns)
np.savetxt(throughputfile,tputs)
print "Avg input load: ", sum(inloads)/len(inloads)
print "Avg util: ", (sum(tputs)/len(tputs))/(sum(inloads)/len(inloads))
