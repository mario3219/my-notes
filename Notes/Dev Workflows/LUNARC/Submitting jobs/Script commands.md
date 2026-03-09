```
The COSMOS system has 256 GB of memory installed on a normal compute node. To allow memory for the operating system, only 254000 MB are available for jobs and the default memory request per core is 5300 MB of memory (48 cores per node).
```

Things to put into .sh file and their effects

| Command                                  | Output                                                              |
| ---------------------------------------- | ------------------------------------------------------------------- |
| `#SBATCH -T 00:10:00`                    | Time for the job                                                    |
| `#SBATCH -J name`                        | Naming a job                                                        |
| `#SBATCH --mem-per-cpu=10600`            | Default memory is 5300 MB, if more is needed, needs to be specified |
| `#SBATCH -o name_%j.out`                 | Specify output file                                                 |
| `#SBATCH -e name_%j.err`                 | Specify error file                                                  |
| `#SBATCH --mail-user=jonte@institute.se` | Specify notification mail                                           |
| `#SBATCH --mail-type=END`                | What type of notification                                           |
| `BEGIN,END,FAIL,REQUEUE,ALL`             | What types exist                                                    |
| `#SBATCH --mem=256G`                     | RAM requirement                                                     |

**Project allocation**
If member of more than one project, need to specify which project to charge

```
#SBATCH -A lu2025-x-xxx
```

**GPUs**

| Command               | Output                     |
| --------------------- | -------------------------- |
| `#SBATCH -p gpua100`  | NVIDIA A100 GPU with AMD   |
| `#SBATCH -p gpua100i` | NVIDIA A100 GPU with Intel |
