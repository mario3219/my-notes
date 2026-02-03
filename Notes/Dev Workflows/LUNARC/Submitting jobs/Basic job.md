Jobs are described in a job script in .sh format

Example echo_script.sh
```
#! /bin/bash
#SBATCH -t 00:05:00

echo "hello"
```

And is executed on the backend servers using:
```
sbatch echo_script.sh
```

Which outputs:
```
[fred@aurora Serial]$ sbatch echo_script.sh
Submitted batch job 7185
```
Where 7185 is the job number assigned by SLURM, and the output will be found in a file slurm-7185.out.

****

Example by Markus:

```
#!/bin/bash  
#SBATCH -t 2-16:00  
#SBATCH --ntasks-per-node=14  
#SBATCH --no-requeue  
#SBATCH -J oc_FU  
#SBATCH -o /lunarc/nobackup/projects/lu2024-17-35/mjheid/roi/oc_FU.log  
#SBATCH -e /lunarc/nobackup/projects/lu2024-17-35/mjheid/roi/oc_FU.log

module load Anaconda3  
conda activate chil

python -m run_roi
```