from app.app_instance import app
from app.models import (GrafanaTerraform, Output)
from fastapi.responses import FileResponse
from app.template_generators.terraform.tfvars.grafana import grafana_tfvars
import shutil
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
                
@app.post("/api/grafana/terraform")
async def grafana_terraform_template_route(request:GrafanaTerraform) -> Output:
    
        dir = 'app/media/terraform.tfvars'
        
        file_response = grafana_tfvars(request)
        with open(dir,'w')as f:
            f.write(file_response)
        
        return FileResponse(dir, media_type='application/zip', filename=f"terraform.tfvars")
    