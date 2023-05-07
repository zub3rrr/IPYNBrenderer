import os
from pathlib import Path
import logging 

logging.basicConfig(
  level=logging.INFO,
  format="[%(asctime)s:%(levelname)s]: %(message)s"
  )


while True:
  project_name = input("Enter project name: ")
  if project_name != '':
    break 
  
  
logging.info(f"Creating project by name {project_name}")

#list of files we want in our project

list_of_files = [
  ".github/workflow/.gitkeep",   #this is keep our project structure intact in github repository i.e. empty files and folder specially
  f"src/{project_name}/__init__.py",
  f"tests/__init__.py",
  f"tests/unit/__init__.py",
  f"tests/integration/__init__.py", 
  "init_setup.sh", #basic environment setup like conda and all
  "requirements.txt",
  "requirements_dev.txt",
   "setup.py",
   "pyproject.toml",
   "setup.cfg",
   "tox.ini"      #to test python packages in various environments
   
]
  
  
for filepath in list_of_files:
  filepath = Path(filepath)
  filedir , filename = os.path.split(filepath)
  if filedir != '':
    os.makedirs(filedir,exist_ok=True)
    logging.info(f"Creating a directory at : {filedir} for file : {filename}")
  if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0 ) :
    with open(filepath,"w") as f:
      pass
      logging.info(f"Creating a new file :{filename} at path:{filepath}")
      
  else:
    logging.info(f"File is already present at path:{filepath}")
    
    
  
  