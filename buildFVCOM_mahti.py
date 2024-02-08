
import os
from shutil import copyfile
import subprocess

#clean = True
clean = False

#BuildPreReq = True
BuildPreReq = False

BuildFVCOM = True
#BuildFVCOM = False

install_dir =  "/projappl/project_2002875/installs/FVCOM_Fimbul/"
make_inc_name = "make.inc.mahti"
#install_dir =  "/projappl/project_2002875/installs/FVCOM_MM/"
#make_inc_name = "make.inc.mahti.MM"

#make_inc_name = "make.inc.puhti"

prereq_install_dir =  "/projappl/project_2002875/installs/FVCOM_external/"
prereq_dir =  "/projappl/project_2002875/source/fvcom4_fisoc/FVCOM_source/libs/"
source_dir =  "/projappl/project_2002875/source/fvcom4_fisoc/FVCOM_source/"

#prereq_makefile_name = "makefile.puhti"
prereq_makefile_name = "makefile.mahti"
makefile_name = "makefile.api"
makedep_name = "makedepends.api"

# environment variables set here will be used over vars set with ?= in the makefile
#os.environ["IOLIBS"] = "-L/appl/spack/v014/install-tree/gcc-9.3.0/netcdf-fortran-4.5.2-n7l5qr/lib -lnetcdff -lnetcdf"
#os.environ["IOINCS"] = "-I/appl/spack/v014/install-tree/gcc-9.3.0/netcdf-fortran-4.5.2-n7l5qr/include"

#os.environ["IOLIBS"] = "-L/appl/spack/v017/install-tree/gcc-11.2.0/netcdf-c-4.8.1-k66cgq/lib"
os.environ["IOLIBS"] = "-L/appl/spack/v017/install-tree/gcc-11.2.0/netcdf-fortran-4.5.3-y5m33p/lib -lnetcdff -lnetcdf"
os.environ["IOINCS"] = "/appl/spack/v017/install-tree/gcc-11.2.0/netcdf-fortran-4.5.3-y5m33p/include"

#os.environ["IOLIBS"] = "-L/appl/spack/v017/install-tree/gcc-9.4.0/netcdf-c-4.8.1-ewvkdv/lib"
#os.environ["IOLIBS"] = "-L/appl/spack/v017/install-tree/gcc-9.4.0/netcdf-fortran-4.5.3-yxu75d/lib -lnetcdff -lnetcdf"
#os.environ["IOINCS"] = "/appl/spack/v017/install-tree/gcc-9.4.0/netcdf-fortran-4.5.3-yxu75d/include"

os.environ["INSTALLDIR"] = prereq_install_dir
os.environ["TOPDIR"] = source_dir

#os.environ["INCLUDEPATH"] = "/appl/spack/v014/install-tree/gcc-9.3.0/openmpi-4.0.3-ddb3ro/lib"
#os.environ["INCLUDEPATH"] = "/appl/spack/v017/install-tree/gcc-8.5.0/gcc-11.2.0-zshp2k/lib"
#os.environ["INCLUDEPATH"] = "/appl/spack/v017/install-tree/gcc-11.2.0/openmpi-4.1.2-h6c3ze/lib"

os.environ["COMPILER"] = "-DGFORTRAN"
           
if clean:
    make_args = "clean"
else:
    make_args = ""


try:
    os.chdir(source_dir)
    copyfile(make_inc_name, "make.inc")
    copyfile(makefile_name, "makefile")
    copyfile(makedep_name, "makedepends")
    os.chdir(prereq_dir)
    copyfile(prereq_makefile_name, "makefile")
except:
    raise NameError("ERROR: Failed to replace makefiles\n")

if BuildPreReq:
    print("\nBuilding FVCOM pre-requisites\n")
    if clean:
        print ("cleaning")
        ret = subprocess.call(["make","clean"])
    else:
        ret = subprocess.call(["make"])

    if (ret != 0):
        raise NameError("ERROR: Failed to build FVCOM pre-requisites\n")
    

if BuildFVCOM:

    print("\nBuilding FVCOM \n")

    os.chdir(source_dir)

    if clean:
        print ("cleaning")
        ret = subprocess.call(["make", "clean"])
        if (ret != 0):
            raise NameError("ERROR: Failed to clean FVCOM\n")
    else:
        ret = subprocess.call(["make"])
        if (ret != 0):
            raise NameError("ERROR: Failed to build FVCOM\n")

        print ("copy to ",install_dir)

        try:
            copyfile("fvcom_driver", install_dir+"/fvcom_driver")
            copyfile("libfvcom_api.so", install_dir+"/libfvcom_api.so")
        except:
            raise NameError("ERROR: Failed to copy lib and exe to install_dir\n")

print("\nFVCOM build complete (maybe it even works...) \n")

