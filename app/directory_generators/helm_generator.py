import os

project_name = "app/media/MyHelm"
chart_structure = {
    "charts": {},
    "templates": {
        "web": {}
    }
}

values_data = {
    'web': {
        'image': 'nginx',
        'targetPort': 80,
        'replicaCount': 1,
        'persistence': {
            'size': '1Gi',
            'accessModes': 'ReadWriteOnce'
        },
        'env': [
            {'name': 'ENV1', 'value': 'Hi'}
        ],
        'ingress': {
            'enabled': False,
            'host': 'www.example.com'
        },
        'stateless': True
    }
}

def create_file(path, content=""):
    with open(path, 'w') as file:
        file.write(content)

os.makedirs(os.path.join(project_name, "charts"), exist_ok=True)
os.makedirs(os.path.join(project_name, "templates", "web"), exist_ok=True)

chart_yaml_content = """apiVersion: v2
name: mychart
description: A Helm chart for Kubernetes
version: 0.1.0
"""

values_yaml_content = """web:
  image: nginx
  targetPort: 80
  replicaCount: 1
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
  stateless: true
"""

create_file(os.path.join(project_name, "Chart.yaml"), chart_yaml_content)
create_file(os.path.join(project_name, "values.yaml"), values_yaml_content)

deployment_yaml_content = """apiVersion: apps/v1
kind: Deployment
metadata:
  name: {{ .Release.Name }}-web
spec:
  replicas: {{ .Values.web.replicaCount }}
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
            {{- range .Values.web.env }}
            - name: {{ .name }}
              value: {{ .value | quote }}
            {{- end }}
"""

service_yaml_content = """apiVersion: v1
kind: Service
metadata:
  name: {{ .Release.Name }}-web
spec:
  ports:
    - port: {{ .Values.web.targetPort }}
  selector:
    app: {{ .Release.Name }}-web
"""

secrets_yaml_content = """apiVersion: v1
kind: Secret
metadata:
  name: {{ .Release.Name }}-secret
type: Opaque
data:
  example-key: {{ .Values.secret.exampleKey | b64enc | quote }}
"""

create_file(os.path.join(project_name, "templates", "web", "deployment.yaml"), deployment_yaml_content)
create_file(os.path.join(project_name, "templates", "web", "service.yaml"), service_yaml_content)
create_file(os.path.join(project_name, "templates", "web", "secrets.yaml"), secrets_yaml_content)

if values_data['web']['stateless']:
    create_file(os.path.join(project_name, "templates", "web", "statefulset.yaml"), "")
else:
    create_file(os.path.join(project_name, "templates", "web", "statefulset.yaml"), "")

if values_data['web']['ingress']['enabled']:
    ingress_yaml_content = """apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: {{ .Release.Name }}-web
spec:
  rules:
    - host: {{ .Values.web.ingress.host }}
      http:
        paths:
          - path: /
            pathType: Prefix
            backend:
              service:
                name: {{ .Release.Name }}-web
                port:
                  number: {{ .Values.web.targetPort }}
"""
    create_file(os.path.join(project_name, "templates", "web", "ingress.yaml"), ingress_yaml_content)

pvc_yaml_content = """apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: {{ .Release.Name }}-web
spec:
  accessModes:
    - {{ .Values.web.persistence.accessModes | first }}
  resources:
    requests:
      storage: {{ .Values.web.persistence.size }}
"""

create_file(os.path.join(project_name, "templates", "web", "pvc.yaml"), pvc_yaml_content)

helpers_tpl_content = """{{/*
Common utility functions for templates
*/}}

{{- define "mychart.name" -}}
{{ .Release.Name }}-{{ .Chart.Name }}
{{- end -}}
"""

create_file(os.path.join(project_name, "templates", "web", "helpers.tpl"), helpers_tpl_content)