import os

# Define the project structure
project_name = "MyHelm"
base_path = "app/media/"
project_path = os.path.join(base_path, project_name)

directories = [
    "charts",
    "templates/web"
]

files_and_contents = {
    "Chart.yaml": """apiVersion: v2
name: MyHelm
description: A Helm chart for Kubernetes
version: 0.1.0
""",
    "values.yaml": """web:
  image: nginx
  targetPort: 80
  replicas: 1
  persistence:
    size: 1Gi
    accessModes:
      - ReadWriteOnce
  env:
    - name: ENV1
      value: Hi
  ingress:
    enabled: true
  stateless: true
""",
    "templates/web/service.yaml": """apiVersion: v1
kind: Service
metadata:
  name: {{ .Release.Name }}-web
spec:
  type: ClusterIP
  ports:
    - port: 80
      targetPort: {{ .Values.web.targetPort }}
  selector:
    app: {{ .Release.Name }}-web
""",
    "templates/web/deployment.yaml": """apiVersion: apps/v1
kind: Deployment
metadata:
  name: {{ .Release.Name }}-web
spec:
  replicas: {{ .Values.web.replicas }}
  selector:
    matchLabels:
      app: {{ .Release.Name }}-web
  template:
    metadata:
      labels:
        app: {{ .Release.Name }}-web
    spec:
      containers:
        - name: web
          image: {{ .Values.web.image }}
          ports:
            - containerPort: {{ .Values.web.targetPort }}
          env:
            - name: {{ .Values.web.env[0].name }}
              value: {{ .Values.web.env[0].value }}
""",
    "templates/web/secret.yaml": """apiVersion: v1
kind: Secret
metadata:
  name: {{ .Release.Name }}-web-secret
type: Opaque
data:
  ENV1: {{ .Values.web.env[0].value | b64enc | quote }}
"""
}

# Create directories and files
os.makedirs(project_path, exist_ok=True)
for directory in directories:
    os.makedirs(os.path.join(project_path, directory), exist_ok=True)

for file_path, content in files_and_contents.items():
    with open(os.path.join(project_path, file_path), 'w') as f:
        f.write(content)