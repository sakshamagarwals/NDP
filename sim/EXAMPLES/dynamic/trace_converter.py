import sys
infile = sys.argv[1]
outfile = sys.argv[2]
PACKET_SIZE = 1500
out_file = open(outfile,'w')
id = 0
with open(infile) as f:
	num_flows = int(f.readline())
	for line in f:
		line_str = line.split()
		src = int(line_str[0])
		dst = int(line_str[1])
		num_packets = int(line_str[3])
		arrival_time = float(line_str[4])

		line_to_write = str(id) + ',' + str(src) + ',' + str(dst) + ',' + str(num_packets * PACKET_SIZE) + ',' + str(arrival_time) + '\n'
		out_file.write(line_to_write)
		id += 1

out_file.close()
		
		
