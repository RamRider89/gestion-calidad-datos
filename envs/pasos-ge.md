# init
source ./miniconda3/bin/activate
conda init --all

# ENVS

# crear enviroment Python-10
conda create --name gx_env python=3.10
conda activate gx_env

# crear enviroment Python-11
conda create --name gx_env-11 python=3.11
conda activate gx_env-11


# crear enviroment Python-12
conda create --name gx_env-12 python=3.12
conda activate gx_env-12

# crear enviroment Python-13
conda create --name gx_env-13 python=3.13
conda activate gx_env-13

# ----------------------------------

# DEPS

# dependencias pip
pip install great-expectations

# dependencias conda
## conda install great-expectations
<!-- Puede romper las dependencias numpy y pandas. -->

## 

# jupyter
pip install jupyter
## conda install -c conda-forge jupyter
<!-- se puede evitar -->
pip install ipykernel
