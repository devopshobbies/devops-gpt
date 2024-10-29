{{- define "web.labels" -}}
app: {{ .Chart.Name }}
component: web-gpt
release: {{ .Release.Name }}
{{- end -}}

{{- define "web.deploymentName" -}}
{{ .Release.Name }}-web
{{- end -}}

{{- define "web.serviceName" -}}
{{ .Release.Name }}-web-service
{{- end -}}

{{- define "web.secretName" -}}
{{ .Release.Name }}-web-secret
{{- end -}}
