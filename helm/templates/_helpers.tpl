{{- define "app.labels" -}}
app: {{ .Chart.Name }}
component: gpt-app
{{- end -}}

{{- define "app.deploymentName" -}}
{{ .Release.Name }}-app-deployment
{{- end -}}

{{- define "app.serviceName" -}}
{{ .Release.Name }}-app-service
{{- end -}}

{{- define "app.secretName" -}}
{{ .Release.Name }}-app-secret
{{- end -}}

{{- define "app.ingressName" -}}
{{ .Release.Name }}-app-ingress
{{- end -}}

{{- define "web.labels" -}}
app: {{ .Chart.Name }}
component: gpt-web
{{- end -}}

{{- define "web.deploymentName" -}}
{{ .Release.Name }}-web-deployment
{{- end -}}

{{- define "web.serviceName" -}}
{{ .Release.Name }}-web-service
{{- end -}}

{{- define "web.ingressName" -}}
{{ .Release.Name }}-web-ingress
{{- end -}}
