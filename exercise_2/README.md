## Exercise 2: Parallel matrix multiplication

In this second exercise, we challenge you to implement a parallel matrix
multiplication algorithm using MPI.

We provide an HDF5 file, stored here  `/global/cscratch1/sd/flanusse/data.hdf`, which contains two matrices,
`A` and `B` both of size 8192x8192.

You will find in [matmul_serial.py](matmul_serial.py) an example script that will compute `C = A . B` using serial Numpy code, output the time required to perform the computation, and save the result in a file for later comparison.
```
$ export OMP_NUM_THREADS=1
$ shifter -- python matmul_serial.py
```
Note that we disable OpenMP multi-threading to enable a fair
comparison to serial code.

Once you have computed the matrix product using serial code, have
a look at [matmul_mpi.py](matmul_mpi.py). In this file we provide
a template to allow you to load the `A` and `B` arrays using
parallel HDF5, and compare the results of your computation to the
matrix multiplication computed above.
