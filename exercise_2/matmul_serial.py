#!/usr/bin/env python
import numpy as np
import h5py
import time

t0 = time.time()  # start time

# Open the data file
with h5py.File('/global/cscratch1/sd/flanusse/data.hdf', 'r') as f:
    A = f['A'][:]
    B = f['B'][:]

t1 = time.time()

C = np.dot(A, B)

t2 = time.time()  # end time

print("MPI matrix multiplication took %f ms" % ((t2 - t1) * 1000.))
print("IO took %f ms" % ((t1 - t0) * 1000.))

# Saving result for later comparison
with h5py.File('matmul_result.hdf', 'w') as f:
    f['C'] = C
print("output saved in 'matmul_result.hdf'")
