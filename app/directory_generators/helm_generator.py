import os

# Define the project structure
project_name = "MyHelm"
base_path = f"app/media/{project_name}"

directories = [
    "charts/",
    "templates/web/"
]

files = [
    "Chart.yaml",
    "values.yaml",
    "templates/web/service.yaml",
    "templates/web/deployment.yaml",
    "templates/web/secret.yaml"  # Only if there are environment variables
]

# Create the directories
for directory in directories:
    os.makedirs(os.path.join(base_path, directory), exist_ok=True)

# Create the Chart.yaml file
chart_yaml_content = """apiVersion: v2
name: mychart
description: A Helm chart for Kubernetes
version: 0.1.0
"""
with open(os.path.join(base_path, "Chart.yaml"), "w") as chart_file:
    chart_file.write(chart_yaml_content)

# Create the values.yaml file
values_yaml_content = """web:
  image: nginx
  service:
    targetPort: 80
  replicas: 1
  persistence:
    enabled: true
    size: 1Gi
    accessModes:
      - ReadWriteOnce
  env:
    - name: ENV1
      value: Hi
  ingress:
    enabled: false
    host: www.example.com
"""
with open(os.path.join(base_path, "values.yaml"), "w") as values_file:
    values_file.write(values_yaml_content)

# Create service.yaml file
service_yaml_content = """apiVersion: v1
kind: Service
metadata:
  name: web
spec:
  type: ClusterIP
  ports:
    - port: 80
      targetPort: {{ .Values.web.service.targetPort }}
  selector:
    app: {{ .Release.Name }}
"""

with open(os.path.join(base_path, "templates/web/service.yaml"), "w") as service_file:
    service_file.write(service_yaml_content)

# Create deployment.yaml file
deployment_yaml_content = """apiVersion: apps/v1
kind: Deployment
metadata:
  name: web
spec:
  replicas: {{ .Values.web.replicas }}
  selector:
    matchLabels:
      app: {{ .Release.Name }}
  template:
    metadata:
      labels:
        app: {{ .Release.Name }}
    spec:
      containers:
        - name: web
          image: {{ .Values.web.image }}
          ports:
            - containerPort: {{ .Values.web.service.targetPort }}
          env:
            - name: ENV1
              value: {{ .Values.web.env[0].value }}
      volumeClaimTemplates:
        - metadata:
            name: web-pvc
          spec:
            accessModes: {{ .Values.web.persistence.accessModes | toYaml }}
            resources:
              requests:
                storage: {{ .Values.web.persistence.size }}
"""

with open(os.path.join(base_path, "templates/web/deployment.yaml"), "w") as deployment_file:
    deployment_file.write(deployment_yaml_content)

# Create secret.yaml file
secret_yaml_content = """apiVersion: v1
kind: Secret
metadata:
  name: web-secret
type: Opaque
data:
  ENV1: aGl
"""

with open(os.path.join(base_path, "templates/web/secret.yaml"), "w") as secret_file:
    secret_file.write(secret_yaml_content)