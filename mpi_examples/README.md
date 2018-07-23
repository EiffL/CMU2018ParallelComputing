# MPI examples

This folder holds a few examples of MPI commands to illustrate the basics of how
to write and execute MPI code in Python.

 - [hello_world.py](hello_world.py): MPI Communicators and rank
 - [send_recv.py](send_recv.py): MPI point-to-point communication (Send, Recv)
 - [bcast.py](bcast.py): MPI collective communication (Bcast)
 - [reduce.py](reduce.py): MPI reduce  operations (Allreduce)

To run one of these examples on your computer, use for instance:
```
$ mpirun -n 4 python hello_world.py
```
where `4` is the number of parallel processes.

To run these examples on a compute node on Cori at NERSC, you would first want
to submit an interactive job:
```
$ salloc -N 1 -q regular -C haswell -t00:30:00 -L SCRATCH --image=docker:eiffl/nersc-python-mpi:latest
```

Inside the job, use the `srun` command instead of `mpirun`:
```
$ srun -n 4 python hello_world.py
```
Note that if you want to execute this code inside the shifter image, you should
use the following:
```
$ srun -n 4 shifter -- python hello_world.py
```
