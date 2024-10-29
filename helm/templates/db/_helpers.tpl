{{- define "db.labels" -}}
app: {{ .Chart.Name }}
component: db-gpt
release: {{ .Release.Name }}
{{- end -}}

{{- define "db.deploymentName" -}}
{{ .Release.Name }}-db
{{- end -}}

{{- define "db.serviceName" -}}
{{ .Release.Name }}-db-service
{{- end -}}

{{- define "db.pvcName" -}}
{{ .Release.Name }}-db-pvc
{{- end -}}

{{- define "db.secretName" -}}
{{ .Release.Name }}-db-secret
{{- end -}}
