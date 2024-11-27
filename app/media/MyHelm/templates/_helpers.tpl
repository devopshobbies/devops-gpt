{{/*
Common template helpers
*/}}
{{- define "my-helm.fullname" -}}
{{- printf "%s-%s" .Release.Name .Chart.Name | trunc 63 | trimSuffix "-" -}}
{{- end -}}
