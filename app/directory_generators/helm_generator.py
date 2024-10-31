import os
import yaml

# Project structure
project_name = "MyHelm"
base_dir = "app/media"
project_dir = os.path.join(base_dir, project_name)

# Directories to create
dirs = ["charts", "crds", "templates/web"]

# Creating the directory structure
for dir in dirs:
    os.makedirs(os.path.join(project_dir, dir), exist_ok=True)

# Chart.yaml content
chart_yaml = {
    "apiVersion": "v1",
    "name": project_name,
    "version": "0.1.0",
    "description": "A Helm chart for MyHelm",
    "maintainers": [{"name": "Your Name", "email": "youremail@example.com"}],
    "keywords": ["helm", "chart"],
    "home": "https://example.com",
    "sources": ["https://github.com/example/MyHelm"]
}

# Writing Chart.yaml
with open(os.path.join(project_dir, "Chart.yaml"), 'w') as chart_file:
    yaml.dump(chart_yaml, chart_file)

# values.yaml content based on provided information
values_yaml = {
    "web": {
        "image": "nginx",
        "service": {
            "enabled": True,
            "port": 80
        }
    }
}

# Writing values.yaml
with open(os.path.join(project_dir, "values.yaml"), 'w') as values_file:
    yaml.dump(values_yaml, values_file)

# Template files content
deployment_yaml = """apiVersion: apps/v1
kind: Deployment
metadata:
  name: web
spec:
  replicas: 1
  selector:
    matchLabels:
      app: web
  template:
    metadata:
      labels:
        app: web
    spec:
      containers:
      - name: web
        image: {{ .Values.web.image }}
        ports:
        - containerPort: {{ .Values.web.service.port }}
"""

service_yaml = """apiVersion: v1
kind: Service
metadata:
  name: web
spec:
  type: ClusterIP
  ports:
    - port: {{ .Values.web.service.port }}
  selector:
    app: web
"""

# Creating deployment.yaml and service.yaml in templates/web
with open(os.path.join(project_dir, "templates/web/deployment.yaml"), 'w') as dep_file:
    dep_file.write(deployment_yaml)

with open(os.path.join(project_dir, "templates/web/service.yaml"), 'w') as svc_file:
    svc_file.write(service_yaml)