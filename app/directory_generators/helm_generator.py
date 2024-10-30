import os

project_name = "MyHelm"
base_dir = "app/media"
project_path = os.path.join(base_dir, project_name)

# Define directories and files
dirs = [
    os.path.join(project_path, "charts"),
    os.path.join(project_path, "crds"),
    os.path.join(project_path, "templates", "web"),
]

files = {
    "Chart.yaml": """apiVersion: v1
name: MyHelm
description: A Helm chart for Kubernetes
version: 0.1.0
""",
    "values.yaml": """image:
  repository: rembg
  tag: latest
  pullPolicy: IfNotPresent
""",
}

# Create project structure
os.makedirs(project_path, exist_ok=True)
for d in dirs:
    os.makedirs(d, exist_ok=True)

# Create files with default content
for file_name, content in files.items():
    with open(os.path.join(project_path, file_name), 'w') as f:
        f.write(content)