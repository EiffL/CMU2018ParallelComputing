#!/usr/bin/env python
import numpy as np
import h5py
import time

t0 = time.time()  # start time

# Open the data file
with h5py.File('/global/cscratch1/sd/flanusse/data.hdf', 'r') as f:
    A = f['A'][:]
    B = f['B'][:]

C = np.dot(A, B)

t1 = time.time()  # end time

print("IO and numpy matrix multiplication took: %f ms" % ((t1 - t0) * 1000))
