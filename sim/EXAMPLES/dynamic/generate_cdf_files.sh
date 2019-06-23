python generate_throughoput_slowdown.py dcqcn-traces/${1}.dat.dcqcn
python generate_cdf.py dcqcn-traces/${1}.dat.dcqcn.slowdown
python generate_cdf.py dcqcn-traces/${1}.dat.dcqcn.throughput
python generate_throughoput_slowdown.py dcqcn-traces/${1}.dat.dcqcn-params
python generate_cdf.py dcqcn-traces/${1}.dat.dcqcn-params.slowdown
python generate_cdf.py dcqcn-traces/${1}.dat.dcqcn-params.throughput
