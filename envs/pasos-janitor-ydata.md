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

# great_expectations
pip install great_expectations
conda install -c conda-forge great-expectations


# err
# 1. Activar el entorno
conda activate data_env-p10

# 2. Desinstalar la versión conflictiva de NumPy
pip uninstall numpy -y

# 3. Instalar la versión "Golden" compatible con Great Expectations y Python 3.10
pip install "numpy<2.0.0,>=1.22.4"

# 4. Reinstalar Great Expectations para asegurar que los entry points se reparen
pip install --upgrade great-expectations



--
pip install "ydata-profiling" "numpy<2.0.0" "pyjanitor" "great-expectations"