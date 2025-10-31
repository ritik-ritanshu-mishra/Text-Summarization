import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "textsummarizer"

list_of_files = [
    ".github/workflows/.gitkeep",               # ci cd deployment helps in automatic deployment whenever we do commit it takes the code and deploy it in the cloud .git keep will not let empty file to be deployed
    f"src/{project_name}/__init__.py",          # making of local package helps to imprt anything from any folder from textsummarizer import 
    f"src/{project_name}/components/__init__.py",   
    f"src/{project_name}/utils/__init__.py",        # utility related code(folder is created and when ever import local package it looks for thr constructor)
    f"src/{project_name}/utils/common.py",          # all utility code written 
    f"src/{project_name}/logging/__init__.py",      # logging folder created 
    f"src/{project_name}/config/__init__.py",       # config folder created 
    f"src/{project_name}/config/configuration.py",   #all configuration required for the project 
    f"src/{project_name}/pipeline/__init__.py",         #pipeline for the project 
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml", 
    "app.py",
    "main.py",      #integration docker file creating image of our source code and will do the deployment in AWS
    "Dockerfile",
    "requirements.txt",   #contains all the requiremnts of the project 
    "setup.py",
    "research/trials.ipynb",
]

for filepath in list_of_files:
    filepath = Path(filepath)   # Handle of the pathn dection of the os 
    filedir, filename = os.path.split(filepath)  #split the dir and the filename 
    
    if filedir != "":       #check whether the file dir 
        os.makedirs(filedir, exist_ok=True)         #create the folder if not present 
        logging.info(f"Creating directory:{filedir} for the file {filename}") # Creation of the folder 

    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):  #Check the file is present or not and checks the file size if the size of the file is greater then 0 then it will not replace of the code 
        with open(filepath,'w') as f:
            pass
            logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} is already exists")
