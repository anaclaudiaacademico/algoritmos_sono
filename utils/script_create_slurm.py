#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
# gerar script
import numpy as np

whereisit = "npad";
jobname = "JAN1"

callstr = "caminho_python"
procestr = " ~ /process_cluster_npad.py"
dirpos = "./input/"


numprocss = 4

for filenumber in np.arange(0,4):
    arquivo = open(dirpos + whereisit + "_%.3d" % filenumber + ".slurm", 'w')

    tosend = "#!/bin/bash\n"  
    tosend += "#SBATCH --job-name=" + jobname + "%.3d\n" % filenumber
    tosend += "#SBATCH --output=ttt/slurm_" + jobname + "%.3d.out\n" % filenumber
    tosend += "#SBATCH --error=ttt/slurm_" + jobname + "%.3d.err\n" % filenumber
    tosend += "#SBATCH --nodes=1\n"
    tosend += "#SBATCH --ntasks-per-node=32\n"
    tosend += "#SBATCH --time=12-23:59\n\n"
#    tosend += "#SBATCH -x service[1-4]\n\n"
    
    tosend += "export OMP_NUM_THREADS=%d\n\n" % int(32/numprocss)
    tosend += callstr + " " + procestr + " %d %d\n" % (filenumber,numprocss)
    
    arquivo.write(tosend)
    arquivo.close()
