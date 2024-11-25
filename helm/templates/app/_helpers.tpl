{{- define "app.labels" -}}
app: {{ .Chart.Name }}
component: gpt-app
release: {{ .Release.Name }}
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
