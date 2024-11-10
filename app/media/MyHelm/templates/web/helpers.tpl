{{/*
Common utility functions for templates
*/}}

{{- define "mychart.name" -}}
{{ .Release.Name }}-{{ .Chart.Name }}
{{- end -}}
