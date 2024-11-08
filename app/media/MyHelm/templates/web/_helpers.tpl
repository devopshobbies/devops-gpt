{{/* Place helper variables here */}}
{{- define "<.Release.Name>.fullname" -}}
{{- printf "%s-%s" .Release.Name .Chart.Name | trunc 63 | trimSuffix "-" -}}
{{- end -}}

{{- define "<.Release.Name>.name" -}}
{{- .Chart.Name | lower -}}
{{- end -}}
