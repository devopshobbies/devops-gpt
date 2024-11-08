import os

# Define project structure
project_name = 'app/media/MyHelm'
directories = ['charts', 'templates/web']
files = ['Chart.yaml', 'values.yaml']
template_files = ['service.yaml', 'secrets.yaml', 'helpers.tpl']
stateless = False
persistence = True
docker_images = {'web': 'nginx'}
target_ports = {'web': 80}
replicas = {'web': 1}
pvc = {'web': {'size': '1Gi', 'accessModes': ['ReadWriteOnce']}}
environment = {'web': [{'name': 'ENV1', 'value': 'Hi'}]}
ingress = {'web': {'enabled': False, 'host': 'www.example.com'}}

# Create directories
for directory in directories:
    os.makedirs(os.path.join(project_name, directory), exist_ok=True)

# Create base files
with open(os.path.join(project_name, 'Chart.yaml'), 'w') as chart_file:
    chart_file.write("apiVersion: v2\n")

with open(os.path.join(project_name, 'values.yaml'), 'w') as values_file:
    values_content = f"web:\n  image: {docker_images['web']}\n  service:\n    port: {target_ports['web']}\n"
    values_content += f"  replicaCount: {replicas['web']}\n"
    if persistence:
        values_content += f"  persistence:\n    size: {pvc['web']['size']}\n    accessModes: {pvc['web']['accessModes'][0]}\n"
    values_content += "  env:\n"
    for env in environment['web']:
        values_content += f"    - name: {env['name']}\n      value: {env['value']}\n"
    values_content += f"  ingress:\n    enabled: {ingress['web']['enabled']}\n    host: {ingress['web']['host']}\n"
    values_content += f"  stateless: {stateless}\n"
    values_file.write(values_content)

# Create template files
for template in template_files:
    with open(os.path.join(project_name, 'templates/web', template), 'w') as temp_file:
        if template == 'service.yaml':
            temp_file.write("""
apiVersion: v1
kind: Service
metadata:
  name: {{ .Release.Name }}-web
spec:
  ports:
    - port: {{ .Values.web.service.port }}
  selector:
    app: {{ .Release.Name }}-web
""")
        elif template == 'secrets.yaml':
            temp_file.write("""
apiVersion: v1
kind: Secret
metadata:
  name: {{ .Release.Name }}-web-secrets
type: Opaque
data:
  ENV1: {{ .Values.web.env[0].value | b64enc }}
""")
        elif template == 'helpers.tpl':
            temp_file.write("""
{{- define "app.media.MyHelm.fullname" -}}
{{- .Release.Name }}-web
{{- end -}}
""")

# Create StatefulSet or Deployment based on statefulness
if stateless:
    with open(os.path.join(project_name, 'templates/web/deployment.yaml'), 'w') as deploy_file:
        deploy_file.write("""
apiVersion: apps/v1
kind: Deployment
metadata:
  name: {{ include "app.media.MyHelm.fullname" . }}
spec:
  replicas: {{ .Values.web.replicaCount }}
  selector:
    matchLabels:
      app: {{ include "app.media.MyHelm.fullname" . }}
  template:
    metadata:
      labels:
        app: {{ include "app.media.MyHelm.fullname" . }}
    spec:
      containers:
        - name: web
          image: {{ .Values.web.image }}
          ports:
            - containerPort: {{ .Values.web.service.port }}
          env:
            {{- range .Values.web.env }}
            - name: {{ .name }}
              value: {{ .value }}
            {{- end }}
""")
else:
    with open(os.path.join(project_name, 'templates/web/statefulset.yaml'), 'w') as stateful_file:
        stateful_file.write("""
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: {{ include "app.media.MyHelm.fullname" . }}
spec:
  serviceName: {{ include "app.media.MyHelm.fullname" . }}
  replicas: {{ .Values.web.replicaCount }}
  selector:
    matchLabels:
      app: {{ include "app.media.MyHelm.fullname" . }}
  template:
    metadata:
      labels:
        app: {{ include "app.media.MyHelm.fullname" . }}
    spec:
      containers:
        - name: web
          image: {{ .Values.web.image }}
          ports:
            - containerPort: {{ .Values.web.service.port }}
          env:
            {{- range .Values.web.env }}
            - name: {{ .name }}
              value: {{ .value }}
            {{- end }}
""")

# Create PVC if persistence is configured
if persistence:
    with open(os.path.join(project_name, 'templates/web/pvc.yaml'), 'w') as pvc_file:
        pvc_file.write("""
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: {{ include "app.media.MyHelm.fullname" . }}-pvc
spec:
  accessModes:
    - {{ .Values.web.persistence.accessModes }}
  resources:
    requests:
      storage: {{ .Values.web.persistence.size }}
""")