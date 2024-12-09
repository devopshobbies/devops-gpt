from app.app_instance import app
from app.models import (DockerCompose,JenkinsInstallation,Output)
from app.template_generators.jenkins.installation import select_install_jenkins
import os


    
    
@app.post("/api/jenkins/installation")
async def jenkins_installation(request:JenkinsInstallation) -> Output:
        
        select_install_jenkins(request)

        return Output(output='output')