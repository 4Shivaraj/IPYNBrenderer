echo [$(date)]: "START"
echo [$(date)]: "Creating conda environment with python 3.8"
conda create --prefix ./env python=3.8 -y
echo [$(date)]: "Activate environment"
source activate ./env
echo [$(date)]: "Installing Dev Requirements"
pip install -r requirements_dev.txt
echo [$(date)]: "End"