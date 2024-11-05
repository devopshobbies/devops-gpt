import os

project_name = "app/media/MyHelm"

# Define the directory structure and file content
directories = [
    "charts",
    "templates/web"
]

files = {
    "Chart.yaml": """apiVersion: v2
name: my-helm
description: A Helm chart for Kubernetes
version: 0.1.0
appVersion: "1.0"
""",
    "values.yaml": """web:
  image: nginx
  service:
    port: 80
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
""",
    "templates/web/service.yaml": """apiVersion: v1
kind: Service
metadata:
  name: {{ include \"my-helm.fullname\" . }}
spec:
  type: ClusterIP
  ports:
    - port: {{ .Values.web.service.port }}
  selector:
    app: {{ include \"my-helm.name\" . }}
""",
    "templates/web/deployment.yaml": """apiVersion: apps/v1
kind: Deployment
metadata:
  name: {{ include \"my-helm.fullname\" . }}
spec:
  replicas: {{ .Values.web.replicas }}
  selector:
    matchLabels:
      app: {{ include \"my-helm.name\" . }}
  template:
    metadata:
      labels:
        app: {{ include \"my-helm.name\" . }}
    spec:
      containers:
        - name: {{ include \"my-helm.name\" . }}
          image: {{ .Values.web.image }}
          ports:
            - containerPort: {{ .Values.web.service.port }}
          env:
            - name: ENV1
              value: Hi
""",
    "templates/web/secret.yaml": """apiVersion: v1
kind: Secret
metadata:
  name: {{ include \"my-helm.fullname\" . }}-secret
type: Opaque
data:
  ENV1: {{ .Values.web.env[0].value | b64enc | quote }}
""",
    "templates/web/helpers.tpl": """{{/*
Helper Template
*/}}
{{- define "my-helm.name" -}}
{{- .Chart.Name | replace \"-\" \"_\" | quote -}}
{{- end -}}

{{- define "my-helm.fullname" -}}
{{- if .Chart.Name -}}
{{- .Release.Name | default \"my-release\" | lower | quote }}-{{ .Chart.Name | lower | quote }}
{{- else -}}
{{- .Release.Name | default \"my-release\" | lower | quote }}
{{- end -}}
{{- end -}}
"""
}

# Create directories
for directory in directories:
    os.makedirs(os.path.join(project_name, directory), exist_ok=True)

# Create files
for file_path, content in files.items():
    with open(os.path.join(project_name, file_path), 'w') as f:
        f.write(content)