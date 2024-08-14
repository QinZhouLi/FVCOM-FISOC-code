
module purge

module load cmake
#module load gcc/9.4.0 
module load gcc/11.2.0
module load openmpi/4.1.2 openblas/0.3.18-omp
module load netcdf-c/4.8.1
module load netcdf-fortran/4.5.3
#module load netlib-scalapack/2.1.0  

# old modules prior to Mahti OS update (occurred May 2022)
#module load cmake/3.16.2 
#module load gcc/9.3.0 openmpi/4.0.3 openblas/0.3.10-omp
#module load netcdf-c/4.7.3-mpi
#module load netcdf-fortran/4.5.2

module load esmf/release
module load elmer/FISOC
#module load fvcom/fimbul
#module load fvcom/MM_test
module load fvcom/Qin
module list

python3 buildFVCOM_mahti.py

#export FC=mpiifort
#export CFLAGS=" -O3 -fPIC"
#export OPT=-O3
#export CPP= /usr/bin/cpp
#export COMPILER= -DMPIIFORT  


