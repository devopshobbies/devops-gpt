from app.app_instance import app
from fastapi import FastAPI, HTTPException,Response
from fastapi.responses import FileResponse
import os
import zipfile


def zip_folder(folder_path: str, output_zip_path: str):
    """Zip the entire folder."""
    with zipfile.ZipFile(output_zip_path, 'w', zipfile.ZIP_DEFLATED) as zip_file:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                # Add file to the zip file
                zip_file.write(file_path, os.path.relpath(file_path, folder_path))


def add_files_to_folder(files:list,folder:str):
    
    os.makedirs(folder, exist_ok=True)

    for filename in files:
        os.path.join(folder, filename)


@app.get("/download-folder{folder_name}/{source}")
async def download_folder_MyHelm(folder_name: str,source:str):
    folder_path = f"app/media/{folder_name}"  # Adjust the path as needed
    if not os.path.exists(folder_path):
        raise HTTPException(status_code=404, detail="Folder not found")

    zip_file_path = f"app/media/{folder_name}_zip.zip"

    # Zip the folder
    zip_folder(folder_path, zip_file_path)

    # Return the zip file as a response
    return FileResponse(zip_file_path, media_type='application/zip', filename=f"{folder_name}_{source}.zip")


