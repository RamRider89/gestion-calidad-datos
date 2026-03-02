# init
source ./miniconda3/bin/activate
conda init --all

# crear enviroment
conda create --name gx_env python=3.10 # Choose a supported Python version
conda activate gx_env

# dependencias pip
pip install great-expectations

# dependencias conda
conda install great-expectations


great_expectations --version
