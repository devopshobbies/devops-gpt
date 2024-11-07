import os

def create_helm_project_structure(base_path):
    project_path = os.path.join(base_path, 'app/media/MyHelm')
    os.makedirs(os.path.join(project_path, 'charts'), exist_ok=True)
    os.makedirs(os.path.join(project_path, 'templates', 'web'), exist_ok=True)

    chart_yaml_content = """apiVersion: v2
name: MyHelm
description: A Helm chart for Kubernetes
version: 0.1.0
"""
    
    values_yaml_content = """web:
  image: nginx
  service:
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
    enabled: false
    host: www.example.com
"""

    service_yaml_content = """apiVersion: v1
kind: Service
metadata:
  name: {{ include "MyHelm.fullname" . }}-web
spec:
  type: ClusterIP
  ports:
    - port: {{ .Values.web.service.targetPort }}
  selector:
    app: {{ include "MyHelm.name" . }}
"""

    deployment_yaml_content = """apiVersion: apps/v1
kind: Deployment
metadata:
  name: {{ include "MyHelm.fullname" . }}-web
spec:
  replicas: {{ .Values.web.replicas }}
  template:
    metadata:
      labels:
        app: {{ include "MyHelm.name" . }}
    spec:
      containers:
        - name: web
          image: {{ .Values.web.image }}
          ports:
            - containerPort: {{ .Values.web.service.targetPort }}
          env:
          {{- range .Values.web.env }}
            - name: {{ .name }}
              value: {{ .value }}
          {{- end }}
"""

    secret_yaml_content = """apiVersion: v1
kind: Secret
metadata:
  name: {{ include "MyHelm.fullname" . }}-web-env
type: Opaque
data:
  ENV1: {{ .Values.web.env | toJson | b64enc | quote }}
"""

    helpers_tpl_content = """{{/*
Expand the name of the chart.
*/}}
{{- define "MyHelm.name" -}}
{{- .Chart.Name | replace "-" "_" | lower -}}
{{- end -}}

{{/*
Create a default fully qualified domain name
*/}}
{{- define "MyHelm.fullname" -}}
{{- if .Chart.Name -}}
{{- .Release.Name | lower | replace "-" "_" | trimSuffix "-" | append (include "MyHelm.name" . | lower) | toLower -}}
{{- else -}}
{{- .Release.Name | lower -}}
{{- end -}}
{{- end -}}
"""

    with open(os.path.join(project_path, 'Chart.yaml'), 'w') as file:
        file.write(chart_yaml_content)

    with open(os.path.join(project_path, 'values.yaml'), 'w') as file:
        file.write(values_yaml_content)

    with open(os.path.join(project_path, 'templates', 'web', 'service.yaml'), 'w') as file:
        file.write(service_yaml_content)

    with open(os.path.join(project_path, 'templates', 'web', 'deployment.yaml'), 'w') as file:
        file.write(deployment_yaml_content)

    with open(os.path.join(project_path, 'templates', 'web', 'secret.yaml'), 'w') as file:
        file.write(secret_yaml_content)

    with open(os.path.join(project_path, 'templates', 'web', 'helpers.tpl'), 'w') as file:
        file.write(helpers_tpl_content)

create_helm_project_structure('.')