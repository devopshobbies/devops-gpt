# Define any helpers here
define "web.fullname"  
  {{ .Release.Name }}-{{ .Values.web.name }} 
end
