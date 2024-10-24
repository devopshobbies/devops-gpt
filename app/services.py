from .utils import save_to_mongo
import os
import shutil

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

def edit_directory_generator(python_code):


    with open('app/directory_generator.py', 'w') as file:
        
        file.write(python_code)

        

def execute_pythonfile():
    folder = 'app/media/MyTerraform'
    if os.path.isdir(folder):
        try:
            
            shutil.rmtree(folder)
            print(f"Successfully removed '{folder}' and all its contents.")
        except Exception as e:
            print(f"Failed to remove '{folder}'. Reason: {e}")

        os.system('python3 app/directory_generator.py')
    os.system('python3 app/directory_generator.py')
