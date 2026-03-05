# init
source ./miniconda3/bin/activate
conda init --all

# crear enviroment
conda create -n data_env-p10 python=3.10

# activar enviroment
conda activate data_env-p10

# dependencias pip
pip install ydata-profiling pyjanitor pandas

# dependencias conda
conda install -c conda-forge ydata-profiling pyjanitor

# jupyter
pip install jupyter
conda install -c conda-forge jupyter
pip install ipykernel



# ----------------
