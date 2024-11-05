{{/*
Helper Template
*/}}
{{- define "my-helm.name" -}}
{{- .Chart.Name | replace "-" "_" | quote -}}
{{- end -}}

{{- define "my-helm.fullname" -}}
{{- if .Chart.Name -}}
{{- .Release.Name | default "my-release" | lower | quote }}-{{ .Chart.Name | lower | quote }}
{{- else -}}
{{- .Release.Name | default "my-release" | lower | quote }}
{{- end -}}
{{- end -}}
