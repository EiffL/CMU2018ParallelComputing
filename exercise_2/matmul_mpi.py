from mpi4py import MPI
import numpy as np
import h5py
import time

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

t0 = time.time()  # start time

# Open the data file
with h5py.File('/global/cscratch1/sd/flanusse/data.hdf', 'r', driver='mpio',
               comm=MPI.COMM_WORLD) as f:

    # Enables atomic operations in MPI for IO, gains in speed
    f.atomic = True
    A_dset = f['A']
    B_dset = f['B']

    # Read first matrix from HDF5 dataset
    A = np.empty(A_dset.shape, A_dset.dtype)
    A[:] = A_dset[:]

    # The following code will only extract a block of size block_size from B
    # for each process
    nx, ny = B_dset.shape
    block_size = ny // size
    start = rank * block_size
    end = (rank + 1) * block_size
    # Note the size of the matrix B we allocate here, it's only a subset of the
    # original matrix
    B = np.empty((nx, block_size), B_dset.dtype)
    with B_dset.collective:
        B[:] = B_dset[:, start:end]

# Allocate an array C to hold the result
C = np.empty((A.shape[0], ny), dtype=np.float32)

# Wait for all IO to be done
comm.Barrier()
t1 = time.time()  # start time

# At this point, A contains the full matrix, B contains a different bloc of
# colummns of the original B matrix for each process
#### Complete this section of the code to fill C with the full result of A.B ##




###############################################################################

t2 = time.time()  # end time

if rank == 0:
    print("MPI matrix multiplication took %f ms" % ((t2 - t1) * 1000.))
    print("IO took %f ms" % ((t1 - t0) * 1000.))

    # Loading result file
    with h5py.File('matmul_result.hdf', 'r') as f:
        Cref = f['C'][:]

    if np.allclose(C, Cref):
        print('Success! parallel output matches serial')
    else:
        print("max distance between matrices:", np.max(abs(C - Cref)))
