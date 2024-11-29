import os

project_name = "app/media/MyHelm"
directories = ["charts", "templates", "templates/web"]
files = ["Chart.yaml", "values.yaml"]
template_files = ["service.yaml", "deployment.yaml", "secrets.yaml", "helpers.tpl"]
ingress_enabled = False
stateless_enabled = True
persistence = True

os.makedirs(project_name, exist_ok=True)

for directory in directories:
    os.makedirs(os.path.join(project_name, directory), exist_ok=True)

with open(os.path.join(project_name, "Chart.yaml"), "w") as chart_file:
    chart_file.write("apiVersion: v2\n")
    chart_file.write("name: MyHelm\n")
    chart_file.write("description: A Helm chart for Kubernetes\n")
    chart_file.write("version: 0.1.0\n")

with open(os.path.join(project_name, "values.yaml"), "w") as values_file:
    values_file.write("web:\n")
    values_file.write("  image: nginx\n")
    values_file.write("  targetPort: 80\n")
    values_file.write("  replicas: 1\n")
    if persistence:
        values_file.write("  persistence:\n")
        values_file.write("    size: 1Gi\n")
        values_file.write("    accessModes: \n")
        values_file.write("      - ReadWriteOnce\n")
    if ingress_enabled:
        values_file.write("  ingress:\n")
        values_file.write("    enabled: true\n")
        values_file.write("    host: www.example.com\n")
    values_file.write("  stateless:\n")
    values_file.write("    enabled: true\n")
    values_file.write("  env:\n")
    values_file.write("    - name: ENV1\n")
    values_file.write("      value: Hi\n")

for template in template_files:
    with open(os.path.join(project_name, "templates", template), "w") as template_file:
        if template == "service.yaml":
            template_file.write("apiVersion: v1\n")
            template_file.write("kind: Service\n")
            template_file.write("metadata:\n")
            template_file.write("  name: {{ .Release.Name }}-web\n")
            template_file.write("spec:\n")
            template_file.write("  ports:\n")
            template_file.write("    - port: 80\n")
            template_file.write("      targetPort: {{ .Values.web.targetPort }}\n")
            template_file.write("  selector:\n")
            template_file.write("    app: {{ .Release.Name }}-web\n")

        if stateless_enabled and template == "deployment.yaml":
            template_file.write("apiVersion: apps/v1\n")
            template_file.write("kind: Deployment\n")
            template_file.write("metadata:\n")
            template_file.write("  name: {{ .Release.Name }}-web\n")
            template_file.write("spec:\n")
            template_file.write("  replicas: {{ .Values.web.replicas }}\n")
            template_file.write("  selector:\n")
            template_file.write("    matchLabels:\n")
            template_file.write("      app: {{ .Release.Name }}-web\n")
            template_file.write("  template:\n")
            template_file.write("    metadata:\n")
            template_file.write("      labels:\n")
            template_file.write("        app: {{ .Release.Name }}-web\n")
            template_file.write("    spec:\n")
            template_file.write("      containers:\n")
            template_file.write("        - name: web\n")
            template_file.write("          image: {{ .Values.web.image }}\n")
            template_file.write("          ports:\n")
            template_file.write("            - containerPort: {{ .Values.web.targetPort }}\n")
            template_file.write("          env:\n")
            template_file.write("            - name: {{ .Values.env[0].name }}\n")
            template_file.write("              value: {{ .Values.env[0].value }}\n")

        if template == "secrets.yaml":
            template_file.write("apiVersion: v1\n")
            template_file.write("kind: Secret\n")
            template_file.write("metadata:\n")
            template_file.write("  name: {{ .Release.Name }}-secret\n")
            template_file.write("type: Opaque\n")
            template_file.write("data:\n")
            template_file.write("  # Insert your base64 encoded secrets here\n")

        if template == "helpers.tpl":
            template_file.write("{{/* Add your helper functions here */}}\n")

if persistence:
    with open(os.path.join(project_name, "templates", "pvc.yaml"), "w") as pvc_file:
        pvc_file.write("apiVersion: v1\n")
        pvc_file.write("kind: PersistentVolumeClaim\n")
        pvc_file.write("metadata:\n")
        pvc_file.write("  name: {{ .Release.Name }}-web-pvc\n")
        pvc_file.write("spec:\n")
        pvc_file.write("  accessModes:\n")
        pvc_file.write("    - {{ .Values.web.persistence.accessModes | first }}\n")
        pvc_file.write("  resources:\n")
        pvc_file.write("    requests:\n")
        pvc_file.write("      storage: {{ .Values.web.persistence.size }}\n")

if ingress_enabled:
    with open(os.path.join(project_name, "templates", "ingress.yaml"), "w") as ingress_file:
        ingress_file.write("apiVersion: networking.k8s.io/v1\n")
        ingress_file.write("kind: Ingress\n")
        ingress_file.write("metadata:\n")
        ingress_file.write("  name: {{ .Release.Name }}-web-ingress\n")
        ingress_file.write("spec:\n")
        ingress_file.write("  rules:\n")
        ingress_file.write("    - host: {{ .Values.web.ingress.host }}\n")
        ingress_file.write("      http:\n")
        ingress_file.write("        paths:\n")
        ingress_file.write("          - path: /\n")
        ingress_file.write("            pathType: Prefix\n")
        ingress_file.write("            backend:\n")
        ingress_file.write("              service:\n")
        ingress_file.write("                name: {{ .Release.Name }}-web\n")
        ingress_file.write("                port:\n")
        ingress_file.write("                  number: 80\n")