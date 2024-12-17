
import os
import shutil
from fastapi import HTTPException


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
