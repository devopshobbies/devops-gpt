from app.app_instance import app
from fastapi import FastAPI, HTTPException,Response
from fastapi.responses import FileResponse
import os


@app.get("/download/{filename}")
def download_file(filename: str):
    folder = "app/media/MyTerraform"  # specify your folder path here
    file_path = os.path.join(folder, filename)

    # Ensure the file exists
    if not os.path.isfile(file_path):
        raise HTTPException(status_code=404, detail="File not found.")

    # Return the file response for download
    return FileResponse(file_path, media_type='application/octet-stream', filename=filename)

@app.get("/list-directory")
def list_directory(folder: str):
    # Ensure the folder exists
    if not os.path.isdir(folder):
        raise HTTPException(status_code=404, detail=f"{folder} does not exist.")

    # List the contents of the directory
    contents = os.listdir(folder)
    return {"folder": folder, "contents": contents}
