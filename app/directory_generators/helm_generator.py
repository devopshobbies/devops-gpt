import os

class Persistance:
    def __init__(self, size, accessModes):
        self.size = size
        self.accessModes = accessModes

class Environment:
    def __init__(self, name, value):
        self.name = name
        self.value = value

def create_helm_structure(base_path):
    os.makedirs(os.path.join(base_path, "charts"), exist_ok=True)
    os.makedirs(os.path.join(base_path, "templates/web"), exist_ok=True)

    chart_yaml_content = """apiVersion: v2
name: MyHelm
description: A Helm chart for Kubernetes
version: 0.1.0
"""
    with open(os.path.join(base_path, "Chart.yaml"), "w") as f:
        f.write(chart_yaml_content)

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
    with open(os.path.join(base_path, "values.yaml"), "w") as f:
        f.write(values_yaml_content)

    service_yaml_content = """apiVersion: v1
kind: Service
metadata:
  name: {{ include "<.Release.Name>.fullname" . }}
spec:
  type: ClusterIP
  ports:
    - port: 80
      targetPort: {{ .Values.web.service.targetPort }}
  selector:
    app: {{ include "<.Release.Name>.name" . }}
"""
    with open(os.path.join(base_path, "templates/web/service.yaml"), "w") as f:
        f.write(service_yaml_content)

    deployment_yaml_content = """apiVersion: apps/v1
kind: Deployment
metadata:
  name: {{ include "<.Release.Name>.fullname" . }}
spec:
  replicas: {{ .Values.web.replicas }}
  selector:
    matchLabels:
      app: {{ include "<.Release.Name>.name" . }}
  template:
    metadata:
      labels:
        app: {{ include "<.Release.Name>.name" . }}
    spec:
      containers:
        - name: {{ include "<.Release.Name>.name" . }}
          image: {{ .Values.web.image }}
          ports:
            - containerPort: {{ .Values.web.service.targetPort }}
          env:
            - name: ENV1
              value: Hi
"""
    with open(os.path.join(base_path, "templates/web/deployment.yaml"), "w") as f:
        f.write(deployment_yaml_content)

    if True:  # Ingress enabled condition
        ingress_yaml_content = """apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: {{ include "<.Release.Name>.fullname" . }}
spec:
  rules:
    - host: {{ .Values.web.ingress.host }}
      http:
        paths:
          - path: /
            pathType: Prefix
            backend:
              service:
                name: {{ include "<.Release.Name>.fullname" . }}
                port:
                  number: 80
"""
        with open(os.path.join(base_path, "templates/web/ingress.yaml"), "w") as f:
            f.write(ingress_yaml_content)

    secret_yaml_content = """apiVersion: v1
kind: Secret
metadata:
  name: {{ include "<.Release.Name>.fullname" . }}-secret
type: Opaque
data:
  ENV1: {{ .Values.web.env[0].value | b64enc | quote }}
"""
    with open(os.path.join(base_path, "templates/web/secret.yaml"), "w") as f:
        f.write(secret_yaml_content)

    helpers_tpl_content = """{{/* Place helper variables here */}}
{{- define "<.Release.Name>.fullname" -}}
{{- printf "%s-%s" .Release.Name .Chart.Name | trunc 63 | trimSuffix "-" -}}
{{- end -}}

{{- define "<.Release.Name>.name" -}}
{{- .Chart.Name | lower -}}
{{- end -}}
"""
    with open(os.path.join(base_path, "templates/web/_helpers.tpl"), "w") as f:
        f.write(helpers_tpl_content)

create_helm_structure("app/media/MyHelm")