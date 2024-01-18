import os
from pathlib import Path

project_name = 'src/automation'

list_of_files = [
    ".github/workflows/.gitkeep",
    f"{project_name}/__init__.py",
    f"{project_name}/constant/__init__.py",
    f"{project_name}/constant/constants/__init__.py",
    f"{project_name}/entity/config_entity/__init__.py",
    f"{project_name}/entity/artifact_entity/__init__.py",
    f"{project_name}/model_factory/__init__.py"
    f"{project_name}/components/__init__.py",
    f"{project_name}/pipeline/__init__.py",
    f"{project_name}/pipeline/data_pipeline/__init__.py",
    f"{project_name}/pipeline/model_pipeline/__init.py",
    f"{project_name}/logging.py",
    f"{project_name}/exception.py",
    "config/config.yaml",
    "params/params.yaml",
    "dvc.yaml",
    "requirements.txt",
    "research/testing.py",
    "setup.py",
    "model/.gitkeep",
    "templates/index.html",
    "init_setup.sh",
]


for filepath in list_of_files:
    filepath=Path(filepath)
    filedir,filename=os.path.split(filepath)
    
    if filedir !="":
        os.makedirs(filedir,exist_ok=True)
        
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,"w") as f:
            pass
    else:
        print(f"{filepath} already exists")