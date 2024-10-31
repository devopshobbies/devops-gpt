import os
import yaml

# Define the project directories and files
project_name = "app/media/MyHelm"
dirs = ["charts", "templates/web"]
files = ["Chart.yaml", "values.yaml", "templates/web/service.yaml", "templates/web/deployment.yaml", "templates/web/secret.yaml"]

# Chart.yaml content
chart_yaml_content = {
    "apiVersion": "v2",
    "name": "my-helm-chart",
    "version": "0.1.0",
    "description": "A Helm chart for Kubernetes",
    "type": "application",
}

# values.yaml content
values_yaml_content = {
    "web": {
        "image": "nginx",
        "replicaCount": 1,
        "service": {
            "port": 80,
        },
        "persistence": {
            "enabled": True,
            "size": "1Gi",
            "accessModes": ["ReadWriteOnce"],
        },
        "env": {
            "ENV1": "Hi",
        },
    }
}

# Create the project structure
for directory in dirs:
    os.makedirs(os.path.join(project_name, directory), exist_ok=True)

# Write Chart.yaml
with open(os.path.join(project_name, "Chart.yaml"), "w") as chart_file:
    yaml.dump(chart_yaml_content, chart_file)

# Write values.yaml
with open(os.path.join(project_name, "values.yaml"), "w") as values_file:
    yaml.dump(values_yaml_content, values_file)

# Write service.yaml
service_yaml_content = """
apiVersion: v1
kind: Service
metadata:
  name: {{ include "{project_name}.name" . }}
spec:
  type: ClusterIP
  ports:
    - port: {{ .Values.web.service.port }}
  selector:
    app: {{ include "{project_name}.name" . }}
"""
with open(os.path.join(project_name, "templates/web/service.yaml"), "w") as service_file:
    service_file.write(service_yaml_content)

# Write deployment.yaml
deployment_yaml_content = """
apiVersion: apps/v1
kind: Deployment
metadata:
  name: {{ include "{project_name}.name" . }}
spec:
  replicas: {{ .Values.web.replicaCount }}
  selector:
    matchLabels:
      app: {{ include "{project_name}.name" . }}
  template:
    metadata:
      labels:
        app: {{ include "{project_name}.name" . }}
    spec:
      containers:
        - name: {{ include "{project_name}.name" . }}
          image: {{ .Values.web.image }}
          ports:
            - containerPort: {{ .Values.web.service.port }}
      {{- if .Values.web.persistence.enabled }}
      volumeClaimTemplates:
      - metadata:
          name: {{ include "{project_name}.name" . }}-pvc
        spec:
          accessModes: {{ .Values.web.persistence.accessModes | toJson }}
          resources:
            requests:
              storage: {{ .Values.web.persistence.size }}
      {{- end }}
"""
with open(os.path.join(project_name, "templates/web/deployment.yaml"), "w") as deployment_file:
    deployment_file.write(deployment_yaml_content)

# Write secret.yaml
secret_yaml_content = """
apiVersion: v1
kind: Secret
metadata:
  name: {{ include "{project_name}.name" . }}-secret
type: Opaque
data:
  ENV1: {{ .Values.web.env.ENV1 | b64enc | quote }}
"""
with open(os.path.join(project_name, "templates/web/secret.yaml"), "w") as secret_file:
    secret_file.write(secret_yaml_content)