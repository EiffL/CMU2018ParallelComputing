# Why, When, and How to write parallel code (in DESC)

This repository holds the examples and exercises for the CMU 2018 DESchool
session on parallel computing from Debbie Bard and Francois Lanusse.

During the session, use the following command to start an interactive session on Cori, with the shifter image defined in [Dockerfile](Dockerfile) preloaded (contains python, mpich, numpy, h5py, mpi4py):

```
$ salloc -N 2 -q regular --reservation=desc  -C haswell -t30 -LSCRATCH --image=docker:eiffl/nersc-python-mpi:latest
```
This will allocate 2 nodes, using the special `desc` reservation only available today. 

Docker image for the tutorial available here: https://hub.docker.com/r/eiffl/nersc-python-mpi/
