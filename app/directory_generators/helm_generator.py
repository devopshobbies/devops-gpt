import os

# Define project structure
project_name = 'app/media/MyHelm'
directories = ['charts/', 'templates/']
templates_dir = 'templates/web'
files = ['Chart.yaml', 'values.yaml']
template_subdirectories = ['web']
template_files = ['service.yaml', 'helpers.tpl']

# Chart.yaml content
chart_yaml_content = """apiVersion: v2
name: my-helm-chart
description: A Helm chart for Kubernetes
version: 0.1.0
"""

# values.yaml content
values_yaml_content = """web:
  image: nginx
  replicas: 1
  service:
    targetPort: 80
  persistence:
    enabled: true
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

# Create project structure
os.makedirs(project_name, exist_ok=True)
for directory in directories:
    os.makedirs(os.path.join(project_name, directory), exist_ok=True)

# Create templates/web directory
os.makedirs(os.path.join(project_name, templates_dir), exist_ok=True)

# Create files
with open(os.path.join(project_name, 'Chart.yaml'), 'w') as chart_file:
    chart_file.write(chart_yaml_content)

with open(os.path.join(project_name, 'values.yaml'), 'w') as values_file:
    values_file.write(values_yaml_content)

# Create template files and directories
for template in template_subdirectories:
    template_path = os.path.join(project_name, 'templates', template)
    os.makedirs(template_path, exist_ok=True)
    for template_file in template_files:
        with open(os.path.join(template_path, template_file), 'w') as file:
            file.write(f"# {template_file} for {template}\n")

# Create secret.yaml if env variable is considered
with open(os.path.join(template_path, 'secret.yaml'), 'w') as secret_file:
    secret_file.write("# secret.yaml for environment variables\n")

# Create helpers.tpl
with open(os.path.join(template_path, 'helpers.tpl'), 'w') as helpers_file:
    helpers_file.write(f"""{{- define "{template}.labels" -}}
name: {{ .Release.Name }}
{{- end -}}
// Add additional helper functions if needed
""")