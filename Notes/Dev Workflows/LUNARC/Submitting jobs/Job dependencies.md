If the result of one jub is dependent on another, can be specified

```
sbatch run_mesh.sh
>> Submitted batch job 8042
```

Now we can make a script dependent on this to be finished

```
sbatch -d afterok:8042 run_sim.sh
>> Submitted batch job 8043
```

**jobinfo** or **squeue** can be used to see status