
module purge

module load cmake/3.16.2 
module load gcc/9.3.0 openmpi/4.0.3 openblas/0.3.10-omp
module load netcdf-c/4.7.3-mpi
module load netcdf-fortran/4.5.2
module load esmf/release
module load elmer/FISOC
module load fvcom/fimbul
module list

python buildFVCOM_mahti.py

#export FC=mpiifort
#export CFLAGS=" -O3 -fPIC"
#export OPT=-O3
#export CPP= /usr/bin/cpp
#export COMPILER= -DMPIIFORT  


