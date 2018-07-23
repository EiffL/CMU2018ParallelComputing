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
$ salloc -N 1 -q regular --reservation=desc -C haswell -t 00:30:00 -L SCRATCH --image=docker:eiffl/nersc-python-mpi:latest
```

Inside the job, use the `srun` command instead of `mpirun`:
```
$ srun -n 8 -c 16 shifter -- python hello_world.py
```
The "-N" option gives the number of nodes, and the "-c" option gives the number of cores assigned to each MPI task per node. From the NERSC documentation:
```
The -c option is used to assign MPI tasks to cores in a way that performs optimally  when there are fewer MPI tasks on a node than the number of hardware threads a node can support.  The "-c" value should be set as the "number of hardware threads the node can support" divided by "the number of MPI tasks per node".  For example, on Haswell, there are a total of 32 physical cores, each capable of 2 hyperthreads, so the value of "-c" should be set to 64/#MPI_tasks_per_node = 64/4 = 16 in this example.  
```
Note that if you do not want to execute this code inside the shifter image, you should
use the following:
```
$ srun -n 8 -c 16 python hello_world.py
```
