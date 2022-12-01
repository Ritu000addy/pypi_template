import os
from pathlib import Path
import logging

logging.basicConfig(
    level=logging.INFO,
    format= '[%(asctime)s: %(levelname)s]: %(message)s'
)

while True:
    project_name = input("Enter the Project Name: ")
    if project_name != '':
        break

logging.info(f"Creating project by name: {project_name}")

#list of files
list_of_files = [
    ".github/workflows/.gitkeep",   #action files # dummy files
    f"src/{project_name}/__init__.py",  #scripts
    f"tests/__init__.py", 
    f"tests/unit/__init__.py", 
    f"tests/integration/__init__.py", 
    "init_setup.sh",     #repo for env set up and install requirements
    "requirements.txt",
    "requirements_dev.txt",     #testing
    "setup.py",     #basic setup
    "pyproject.toml",
    "setup.cfg",
    "tox.ini",      #test package on diff env
]

for filepath in list_of_files:

    filepath = Path(filepath)       #will use whenever call filepath

    filedir, filename = os.path.split(Path(filepath))

    if filedir != "":       #to check if dir is empty, if not then make directory
        os.makedirs(filedir, exist_ok=True)     #exist_ok wont throw error if its true
        logging.info(f"Creating directory at: {filedir} for file: {filename}")
    
    #rerun code will erase the files

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating a new file {filename} at path: {filepath}")
    else:
        logging.info(f"File is already present at: {filepath}")
