Compare how long it takes to run this simple Gaussian fitting example looping over the dataset, and using multiprocessing to map the fitting into a pool of processes. 
Try different sizes of datasets, specified by the command line input, e.g. 

> time python loop-fitG.py  10000
loop Model: Gaussian1D
Inputs: (u'x',)
Outputs: (u'y',)
Model set size: 1
Parameters:
      amplitude        mean         stddev    
    ------------- ------------- --------------
    3.05037167379 1.27749879998 0.809572903661

real    0m41.657s
user    0m40.358s
sys     0m0.542s



> time python poolmap-gFit.py 10000
I have 4 cores here
pool.map: Model: Gaussian1D
Inputs: (u'x',)
Outputs: (u'y',)
Model set size: 1
Parameters:
      amplitude        mean         stddev    
    ------------- ------------- --------------
    3.04340606599 1.29109752995 0.798482260075

real    0m23.750s
user    1m21.012s
sys     0m1.363s


These examples were run on a 2015 macbook air with 2 physical cores, 4 hyprthreads. Note in the poolmap example the difference between the "user" time and the "real" time - this indicates how much time was taken by the CPUs, in this case about 3.5x more than user time (indicating the 4 threads available). 
Also note that the multiprocessing example was only twice as fast as the regular loop, despite there being 4 threads available. This demonstrates the overhead inherent in setting up the pools and processes. 