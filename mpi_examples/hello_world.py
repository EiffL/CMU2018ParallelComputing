#!/usr/bin/env python
from mpi4py import MPI

# Use the default WORLD communicator and extract process rank and total number
# of processes
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

if rank == 0:
    print("I am the master")
else:
    print("I'm worker number %d" % rank)
