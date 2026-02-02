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