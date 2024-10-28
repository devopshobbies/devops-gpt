from .utils import save_to_mongo
import os
import shutil
from fastapi import HTTPException

def write_basic(request,output):

    data = {
        'question':request.question,
        'output':output
    }

    save_to_mongo(data, index='question', collection = 'qa')


def write_bugfix(request,output):

    data = {
        'bug_description':request.bug_description,
        'service':request.service,
        'output':output
    }

    save_to_mongo(data, index=['bug_description','service'], collection = 'bugfix')


def write_installation(request,output):

    data = {
        'os':request.os,
        'service':request.service,
        'output':output
    }

    save_to_mongo(data, index=['os','service'], collection = 'installation')

def edit_directory_generator(gen_file,python_code):


    with open(f"app/directory_generators/{gen_file}.py", 'w') as file:
        
        file.write(python_code)

        

def execute_pythonfile(folder,gen_file):
    folder = f"app/media/{folder}"
    if os.path.isdir(folder):
        try:
            
            shutil.rmtree(folder)
            print(f"Successfully removed '{folder}' and all its contents.")
        except Exception as e:
            raise HTTPException(status_code=400, detail='please try again')

        os.system(f"python3 app/directory_generators/{gen_file}.py")
    os.system(f"python3 app/directory_generators/{gen_file}.py")
