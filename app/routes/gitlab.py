from app.app_instance import app
from app.models import (GitLabInstallation,Output)
from app.template_generators.gitlab.installation import select_install_gitlab
import os


    
    
@app.post("/api/gitlab/installation")
async def gitlab_installation(request:GitLabInstallation) -> Output:
        
        select_install_gitlab(request)

        return Output(output='output')