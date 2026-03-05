# init
source ./miniconda3/bin/activate
conda init --all

# ENVS

# ------------------------------------------
# ------------------------------------------

# PYTHON 10

# crear enviroment Python-10
conda create -n janitor-p10 python=3.10

# activar enviroment
conda activate janitor-p10

# dependencias pip
pip install ydata-profiling pyjanitor pandas
pip install great-expectations

# dependencias conda
conda install -c conda-forge ydata-profiling pyjanitor



# ------------------------------------------ 
# ------------------------------------------
# jupyter
pip install jupyter
pip install ipykernel
