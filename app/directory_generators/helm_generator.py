import os
import yaml

# Define directory and file structure
project_name = 'MyHelm'
base_path = os.path.join('app', 'media', project_name)

directories = [
    os.path.join(base_path, 'charts'),
    os.path.join(base_path, 'templates', 'web')
]

files = {
    'Chart.yaml': {
        'apiVersion': 'v2',
        'name': project_name,
        'description': 'A Helm chart for Kubernetes',
        'version': '0.1.0',
        'appVersion': '1.0.0'
    },
    'values.yaml': {
        'web': {
            'image': {
                'repository': 'nginx',
                'tag': 'latest'
            },
            'service': {
                'enabled': True,
                'port': 80
            },
            'replicaCount': 1,
            'persistence': {
                'enabled': True,
                'size': '1Gi',
                'accessModes': ['ReadWriteOnce']
            },
            'env': [{
                'name': 'ENV1',
                'value': 'Hi'
            }],
            'ingress': {
                'enabled': False,
                'host': 'www.example.com'
            }
        }
    }
}

# Create directories
for directory in directories:
    os.makedirs(directory, exist_ok=True)

# Create files with initial content
for filename, content in files.items():
    with open(os.path.join(base_path, filename), 'w') as file:
        yaml.dump(content, file)

# Create service.yaml template
service_yaml_content = """apiVersion: v1
kind: Service
metadata:
  name: {{ include "{project_name}.fullname" . }}
spec:
  type: ClusterIP
  ports:
    - port: {{ .Values.web.service.port }}
  selector:
    app: {{ include "{project_name}.name" . }}
"""

with open(os.path.join(base_path, 'templates', 'web', 'service.yaml'), 'w') as service_file:
    service_file.write(service_yaml_content.format(project_name=project_name))

# Create secret.yaml template if environment variables exist
if files['values.yaml']['web'].get('env'):
    secret_yaml_content = """apiVersion: v1
kind: Secret
metadata:
  name: {{ include "{project_name}.fullname" . }}-env
type: Opaque
data:
  ENV1: {{ .Values.web.env[0].value | b64enc | quote }}
"""

    with open(os.path.join(base_path, 'templates', 'web', 'secret.yaml'), 'w') as secret_file:
        secret_file.write(secret_yaml_content.format(project_name=project_name))