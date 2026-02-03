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

**Project allocation**
If member of more than one project, need to specify which project to charge

```
#SBATCH -A lu2025-x-xxx
```

**GPU and CPU allocation**

NVIDIA A100 with Intel CPU
```
#SBATCH -p gpua100i
#SBATCH -N 1
#SBATCH --ntasks-per-node=16
#SBATCH --gres=gpu:1
#SBATCH --mem-per-cpu=11800
```
Using 1 node, 16 tasks per node, 1 gpu, 11800MB per CPU core.