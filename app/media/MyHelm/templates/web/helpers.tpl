{{/*
Expand the name of the chart.
*/}}
{{- define "MyHelm.name" -}}
{{- .Chart.Name | replace "-" "_" | lower -}}
{{- end -}}

{{/*
Create a default fully qualified domain name
*/}}
{{- define "MyHelm.fullname" -}}
{{- if .Chart.Name -}}
{{- .Release.Name | lower | replace "-" "_" | trimSuffix "-" | append (include "MyHelm.name" . | lower) | toLower -}}
{{- else -}}
{{- .Release.Name | lower -}}
{{- end -}}
{{- end -}}
