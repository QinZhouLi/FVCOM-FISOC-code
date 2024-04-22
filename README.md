
Compiling FVCOM for FISOC on CSC machines.

Has been built on Puhti (approx. 2019), Mahti (approx. 2022) and LUMI (in progress as of Feb 2024).

Scripts like this just load the right modules and call the python build script:
buildFVCOM_MachineName.sh

I think the ones with "MM" and "FX4" instead of MachineName were used on Puhti and only differ from each other in terms of which make.inc to use and where to install.  This is because FVCOM was installed multiple times on Puhti with slightly different options. Only one build was used on Mahti.  Probably one build is fine for LUMI...


Python scripts look like this:
buildFVCOM_MachineName.py
These scripts set some paths and environment variables and call make.





Old notes:

To build on virtual machine / elemeruser prepare code by:
- copying FVCOM_source/make.inc.elmeruser to FVCOM_source/make.inc
- copying FVCOM_source/libs/makefile.vm_elemeruser to FVCOM_source/libs/makefile
- and execute it to build local libraries

Then build FVCOM via cmake following the instructions given in the readme.elmeruser of the uk-fvcom-iceshelf-vm-elmeruser branch of the fvcom-cmake repository
