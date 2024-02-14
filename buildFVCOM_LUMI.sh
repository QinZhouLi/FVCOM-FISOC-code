
#module purge

export COMPILER="gcc/11.2.0"
export MPI="cray-mpich/8.1.23"
module load $COMPILER $MPI PrgEnv-gnu/8.3.3 cray-libsci/22.12.1.1 cray-hdf5/1.12.2.3 cray-netcdf/4.9.0.3 cray-parallel-netcdf/1.12.3.1

#module load craype

module load cmake
#module load netcdf-c

#module load openmpi/4.1.2 openblas/0.3.18-omp
#module load netcdf-c/4.8.1
#module load netcdf-fortran/4.5.3

#module load esmf/release
#module load elmer/FISOC
#module load fvcom/fimbul
#module list

python3 buildFVCOM_LUMI.py

#export FC=mpiifort
#export CFLAGS=" -O3 -fPIC"
#export OPT=-O3
#export CPP= /usr/bin/cpp
#export COMPILER= -DMPIIFORT  


