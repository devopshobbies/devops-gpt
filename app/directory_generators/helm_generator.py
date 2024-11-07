import os

class Persistence:
    def __init__(self, size, accessModes):
        self.size = size
        self.accessModes = accessModes

class Environment:
    def __init__(self, name, value):
        self.name = name
        self.value = value

class Ingress:
    def __init__(self, enabled, host):
        self.enabled = enabled
        self.host = host

def create_file_with_content(filepath, content):
    with open(filepath, 'w') as f:
        f.write(content)

def generate_helm_project_structure():
    project_name = 'app/media/MyHelm'
    
    os.makedirs(os.path.join(project_name, 'charts'), exist_ok=True)
    os.makedirs(os.path.join(project_name, 'templates', 'web'), exist_ok=True)

    chart_yaml_content = """apiVersion: v2
name: myhelm-chart
description: A Helm chart for Kubernetes
version: 0.1.0
"""
    create_file_with_content(os.path.join(project_name, 'Chart.yaml'), chart_yaml_content)

    values_yaml_content = """web:
  image: nginx
  replicas: 1
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
    create_file_with_content(os.path.join(project_name, 'values.yaml'), values_yaml_content)

    deployment_yaml_content = """apiVersion: apps/v1
kind: Deployment
metadata:
  name: {{ include "myhelm-chart.fullname" . }}
spec:
  replicas: {{ .Values.web.replicas }}
  selector:
    matchLabels:
      app: {{ include "myhelm-chart.name" . }}
  template:
    metadata:
      labels:
        app: {{ include "myhelm-chart.name" . }}
    spec:
      containers:
      - name: {{ include "myhelm-chart.name" . }}
        image: {{ .Values.web.image }}
        ports:
        - containerPort: 80
        env:
        {{- range .Values.web.env }}
        - name: {{ .name }}
          value: {{ .value }}
        {{- end }}
"""
    create_file_with_content(os.path.join(project_name, 'templates', 'web', 'deployment.yaml'), deployment_yaml_content)

    service_yaml_content = """apiVersion: v1
kind: Service
metadata:
  name: {{ include "myhelm-chart.fullname" . }}
spec:
  type: ClusterIP
  ports:
    - port: 80
      targetPort: 80
  selector:
    app: {{ include "myhelm-chart.name" . }}
"""
    create_file_with_content(os.path.join(project_name, 'templates', 'web', 'service.yaml'), service_yaml_content)

    secret_yaml_content = """apiVersion: v1
kind: Secret
metadata:
  name: {{ include "myhelm-chart.fullname" . }}-env
type: Opaque
data:
  ENV1: {{ .Values.web.env | json | b64enc | quote }}
"""
    create_file_with_content(os.path.join(project_name, 'templates', 'web', 'secret.yaml'), secret_yaml_content)

    helpers_tpl_content = """{{/*
Expand the name of the chart.
*/}}
{{- define "myhelm-chart.name" -}}
{{- if .Chart.Name -}}
{{ .Chart.Name | quote }}
{{- else -}}
myhelm-chart
{{- end -}}
{{- end -}}

{{/*
Return the full name of the chart.
*/}}
{{- define "myhelm-chart.fullname" -}}
{{ printf "%s-%s" .Release.Name (include "myhelm-chart.name" .) | trunc 63 | trimSuffix "-" }}
{{- end -}}
"""
    create_file_with_content(os.path.join(project_name, 'templates', 'web', 'helpers.tpl'), helpers_tpl_content)

generate_helm_project_structure()