{{/*
Helper template functions
*/}}
{{- define "myhelm.name" -}}
{{- if .Chart.Name -}}
{{ .Chart.Name | quote }}
{{- else -}}
""
{{- end -}}
{{- end -}}

{{- define "myhelm.fullname" -}}
{{- .Release.Name | replace "-" "" }}-{{ include "myhelm.name" . }}
{{- end -}}
