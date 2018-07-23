#!/usr/bin/env python
from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# Only initializes an array A on the root process (rank == 0)
if rank == 0:
    # Note that the size of our array is 4x the number of processes
    A = np.arange(4 * size, dtype=np.int32)
else:
    A = None

# Allocate arrays for communication
# 4 is the size of the chunk that each process will handle
a = np.empty((4,), dtype=np.int32)

# Distributes chunks of size 4 accross all the processes
comm.Scatter(A, a, root=0)

# Perform local sum over chunk of array A and store the result in a buffer of
# size 1
buff = np.array(np.sum(a**2), dtype=np.int32)

# Sums values and shares result with all processes
result = np.array(0, dtype=np.int32)
comm.Allreduce(buff, result, op=MPI.SUM)

if rank == 0:
    print("Norm of input array %f " % np.sqrt(np.sum(A**2)))
if rank == 1:
    print("Norm computed with MPI %f" % np.sqrt(result))

# This script has computed the norm of vector A
