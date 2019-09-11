python generate_throughoput_slowdown.py traces/$1.dat.$2
python compute_results.py traces/$1.dat.$2.slowdown
python compute_results.py traces/$1.dat.$2.throughput
cat traces/$1.dat.$2.slowdown.result
cat traces/$1.dat.$2.throughput.result
