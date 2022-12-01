#export _VERSION_=3.9
echo [$(date)]: "START"
echo [$(date)]: "Creating conda env with python"
conda create --prefix ./env python=3.9 -y
echo [$(date)]: "Activate env"
source activate ./env
echo [$(date)]: "Installing dev requirements"
pip install -r requirements_dev.txt
echo [$(date)]: "END"