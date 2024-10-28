import os

# Define the project structure
project_name = "app/media/MyHelm"
directories = ["charts", "crds", "templates"]
files = ["Chart.yaml", "values.yaml"]

# Define default content for Chart.yaml and values.yaml
chart_yaml_content = """apiVersion: v2
name: myhelm
description: A Helm chart for Kubernetes
version: 0.1.0
"""
values_yaml_content = """# Default values for myhelm.
# This is a YAML-formatted file.
# Declare variables to be passed into your templates.
replicaCount: 1
image:
  repository: myimage
  pullPolicy: IfNotPresent
  tag: ""
service:
  name: myservice
  type: ClusterIP
  port: 80
"""

# Create the project structure
os.makedirs(project_name, exist_ok=True)

for directory in directories:
    os.makedirs(os.path.join(project_name, directory), exist_ok=True)

for file in files:
    file_path = os.path.join(project_name, file)
    with open(file_path, 'w') as f:
        if file == "Chart.yaml":
            f.write(chart_yaml_content)
        elif file == "values.yaml":
            f.write(values_yaml_content)

# Create a basic GitHub Actions workflow file
github_actions_dir = os.path.join(project_name, ".github/workflows")
os.makedirs(github_actions_dir, exist_ok=True)
with open(os.path.join(github_actions_dir, "ci.yml"), 'w') as f:
    f.write("""name: CI

on:
  push:
    branches:
      - main
  pull_request:
    branches:
      - main

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v2
      
      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v1
      
      - name: Cache Docker layers
        uses: actions/cache@v2
        with:
          path: /tmp/.buildx-cache
          key: ${{ runner.os }}-buildx-${{ github.sha }}
          restore-keys: |
            ${{ runner.os }}-buildx-
      
      - name: Build and push Docker image
        uses: docker/build-push-action@v2
        with:
          context: .
          file: Dockerfile
          push: true
          tags: myimage:latest
""")