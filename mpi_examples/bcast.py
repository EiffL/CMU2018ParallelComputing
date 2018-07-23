#!/usr/bin/env python
from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# Allocate an array of size 5, but only process 0 holds the data at first
if rank == 0:
    A = np.array([0, 1, 2, 3, 4], dtype=np.int32)
else:
    A = np.empty(5, dtype=np.int32)

# Broadcast the content of A from process 0 to all other processes
comm.Bcast(A, root=0)

print("I am process %d:" % rank, A)
