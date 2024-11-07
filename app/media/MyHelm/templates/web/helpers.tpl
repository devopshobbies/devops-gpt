{{/*
Expand the name of the chart.
*/}}
{{- define "myhelm-chart.name" -}}
{{- if .Chart.Name -}}
{{ .Chart.Name | quote }}
{{- else -}}
myhelm-chart
{{- end -}}
{{- end -}}

{{/*
Return the full name of the chart.
*/}}
{{- define "myhelm-chart.fullname" -}}
{{ printf "%s-%s" .Release.Name (include "myhelm-chart.name" .) | trunc 63 | trimSuffix "-" }}
{{- end -}}
