import sys

protocols = ['dcqcn']

curr_time = -1
for protocol in protocols:
    f = open(sys.argv[2]+"_debug_" + sys.argv[1], "r")
    out = open("traces/"+sys.argv[1]+"."+sys.argv[2]+".utilization", "w")
    for line in f:
        tokens = line.split()
        if (len(tokens) >= 2 and tokens[0] == "*******************************"):
            t = float(tokens[3])/1000.0
            if (t != curr_time):
		if(t<=0.0):
		    assert(float(tokens[18]) == 0)
		    util = 0.0
		else:
                    util = float(tokens[18])/(4*144) * t / (t)
                    #if (protocol == 'PERMUTATION' or protocol == 'NDP'):
                    #    util = float(tokens[18])/144
                    #elif (protocol == 'dcqcn'):
                    #    util = float(tokens[18])/(4*144)
                out.write(str(t) + " " + str(util))
                out.write("\n")
                curr_time = t
f.close()
out.close()
