#!/usr/bin/env python
from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# Create an array A, initialized with different data depending on the rank of
# the process
if rank == 0:
    A = np.array([0, 1])
else:
    A = np.array([2, 3])

# Compute the sum over the local array elements
result = np.array(0)
for i in range(2):
    result += A[i]

if rank == 0:
    # For process 0, wait for the result of the sum computed by process 1
    buffer = np.array(0)
    comm.Recv(buffer, source=1)
    result += buffer
    print("The result is %d" % result)

if rank == 1:
    # For process 1, send the partial sum to process 0
    comm.Send(result, dest=0)

# This script has computed the sum of vector A despite A being stored over
# different processes.
