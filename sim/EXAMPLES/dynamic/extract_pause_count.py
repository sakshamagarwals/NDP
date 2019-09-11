import sys
pause_count = 0
with open(sys.argv[1]) as f1:
	for line in f1:
		line_str = line.split()
		if(line_str[0]=='Ingress' and line_str[3]=='PAUSE' and line_str[4]=='1000'):
			pause_count += 1
print pause_count	
