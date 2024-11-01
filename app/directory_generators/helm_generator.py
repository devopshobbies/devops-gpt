import os

# Define project structure
project_name = "app/media/MyHelm"
directories = ["charts", "templates/web"]
files = ["Chart.yaml", "values.yaml"]
template_files = ["service.yaml", "secret.yaml"]
chart_content = """apiVersion: v2
name: my-helm-chart
description: A Helm chart for Kubernetes
version: 0.1.0
"""
values_content = """web:
  image: nginx
  replicas: 1
  service:
    port: 80
  persistence:
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

# Create project directories and files
os.makedirs(project_name, exist_ok=True)
for directory in directories:
    os.makedirs(os.path.join(project_name, directory), exist_ok=True)

for file in files:
    with open(os.path.join(project_name, file), 'w') as f:
        if file == "Chart.yaml":
            f.write(chart_content)
        elif file == "values.yaml":
            f.write(values_content)

# Create template files
for template in directories[1:]:
    for template_file in template_files:
        with open(os.path.join(project_name, template, template_file), 'w') as f:
            if template_file == "service.yaml":
                f.write("""apiVersion: v1
kind: Service
metadata:
  name: {{ include "{{ .Chart.Name }}.fullname" . }}
spec:
  type: ClusterIP
  ports:
    - port: {{ .Values.web.service.port }}
      targetPort: {{ .Values.web.service.port }}
  selector:
    app: {{ include "{{ .Chart.Name }}.fullname" . }}
""")
            elif template_file == "secret.yaml":
                f.write("""apiVersion: v1
kind: Secret
metadata:
  name: {{ include "{{ .Chart.Name }}.fullname" . }}-secret
type: Opaque
data:
  ENV1: {{ .Values.web.env | toJson | b64enc | quote }}
""")