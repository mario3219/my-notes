| Command                                  | Output                                             |
| ---------------------------------------- | -------------------------------------------------- |
| conda create -n myenv python=3.11        | Create env                                         |
| conda activate myenv<br>conda deactivate | Activate/deactivate env                            |
| conda env list                           | Lists environments                                 |
| conda remove -n ENV_NAME --all           | Remove env                                         |
| conda rename -n old_name new_name        | Rename environment                                 |
| conda env export > environment.yml       | Export required packages                           |
| conda env create -f environment.yml      | Create environment using required packages in .yml |
| conda create -n myenv --clone base       | Copy packages from base                            |
