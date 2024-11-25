import os

project_name = "app/media/MyHelm"
charts_dir = os.path.join(project_name, "charts")
templates_dir = os.path.join(project_name, "templates")
web_dir = os.path.join(templates_dir, "web")

# Create project directories
os.makedirs(charts_dir, exist_ok=True)
os.makedirs(templates_dir, exist_ok=True)
os.makedirs(web_dir, exist_ok=True)

# Create Chart.yaml
with open(os.path.join(project_name, "Chart.yaml"), "w") as chart_file:
    chart_file.write("apiVersion: v2\n")
    chart_file.write("name: MyHelm\n")
    chart_file.write("description: A Helm chart for Kubernetes\n")
    chart_file.write("version: 0.1.0\n")

# Create values.yaml
with open(os.path.join(project_name, "values.yaml"), "w") as values_file:
    values_file.write("web:\n")
    values_file.write("  image: nginx\n")
    values_file.write("  targetPort: 80\n")
    values_file.write("  replicas: 1\n")
    values_file.write("  persistence:\n")
    values_file.write("    size: 1Gi\n")
    values_file.write("    accessModes:\n")
    values_file.write("      - ReadWriteOnce\n")
    values_file.write("  env:\n")
    values_file.write("    - name: ENV1\n")
    values_file.write("      value: Hi\n")
    values_file.write("  ingress:\n")
    values_file.write("    enabled: false\n")
    values_file.write("    host: www.example.com\n")
    values_file.write("  stateless:\n")
    values_file.write("    enabled: false\n")

# Create service.yaml
with open(os.path.join(web_dir, "service.yaml"), "w") as service_file:
    service_file.write("apiVersion: v1\n")
    service_file.write("kind: Service\n")
    service_file.write("metadata:\n")
    service_file.write("  name: web-service\n")
    service_file.write("spec:\n")
    service_file.write("  type: ClusterIP\n")
    service_file.write("  ports:\n")
    service_file.write("    - port: 80\n")
    service_file.write("      targetPort: {{ .Values.web.targetPort }}\n")
    service_file.write("  selector:\n")
    service_file.write("    app: web\n")

# Create statefulset.yaml (since stateless is false)
with open(os.path.join(web_dir, "statefulset.yaml"), "w") as statefulset_file:
    statefulset_file.write("apiVersion: apps/v1\n")
    statefulset_file.write("kind: StatefulSet\n")
    statefulset_file.write("metadata:\n")
    statefulset_file.write("  name: web\n")
    statefulset_file.write("spec:\n")
    statefulset_file.write("  serviceName: web-service\n")
    statefulset_file.write("  replicas: {{ .Values.web.replicas }}\n")
    statefulset_file.write("  selector:\n")
    statefulset_file.write("    matchLabels:\n")
    statefulset_file.write("      app: web\n")
    statefulset_file.write("  template:\n")
    statefulset_file.write("    metadata:\n")
    statefulset_file.write("      labels:\n")
    statefulset_file.write("        app: web\n")
    statefulset_file.write("    spec:\n")
    statefulset_file.write("      containers:\n")
    statefulset_file.write("        - name: web\n")
    statefulset_file.write("          image: {{ .Values.web.image }}\n")
    statefulset_file.write("          ports:\n")
    statefulset_file.write("            - containerPort: {{ .Values.web.targetPort }}\n")
    statefulset_file.write("          env:\n")
    statefulset_file.write("            - name: {{ .Values.web.env[0].name }}\n")
    statefulset_file.write("              value: {{ .Values.web.env[0].value }}\n")
    statefulset_file.write("      volumeClaimTemplates:\n")
    statefulset_file.write("        - metadata:\n")
    statefulset_file.write("            name: web-pvc\n")
    statefulset_file.write("          spec:\n")
    statefulset_file.write("            accessModes:\n")
    statefulset_file.write("              - {{ .Values.web.persistence.accessModes[0] }}\n")
    statefulset_file.write("            resources:\n")
    statefulset_file.write("              requests:\n")
    statefulset_file.write("                storage: {{ .Values.web.persistence.size }}\n")

# Create pvc.yaml
with open(os.path.join(web_dir, "pvc.yaml"), "w") as pvc_file:
    pvc_file.write("apiVersion: v1\n")
    pvc_file.write("kind: PersistentVolumeClaim\n")
    pvc_file.write("metadata:\n")
    pvc_file.write("  name: web-pvc\n")
    pvc_file.write("spec:\n")
    pvc_file.write("  accessModes:\n")
    pvc_file.write("    - {{ .Values.web.persistence.accessModes[0] }}\n")
    pvc_file.write("  resources:\n")
    pvc_file.write("    requests:\n")
    pvc_file.write("      storage: {{ .Values.web.persistence.size }}\n")

# Create secrets.yaml
with open(os.path.join(web_dir, "secrets.yaml"), "w") as secrets_file:
    secrets_file.write("apiVersion: v1\n")
    secrets_file.write("kind: Secret\n")
    secrets_file.write("metadata:\n")
    secrets_file.write("  name: web-secrets\n")
    secrets_file.write("type: Opaque\n")
    secrets_file.write("data:\n")
    secrets_file.write("  # Add your base64 encoded secrets here\n")

# Create helpers.tpl
with open(os.path.join(web_dir, "helpers.tpl"), "w") as helpers_file:
    helpers_file.write("# Define any helpers here\n")
    helpers_file.write("define \"web.fullname\"  \n")
    helpers_file.write("  {{ .Release.Name }}-{{ .Values.web.name }} \n")
    helpers_file.write("end\n")