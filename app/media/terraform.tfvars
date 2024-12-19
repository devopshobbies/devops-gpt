
# Grafana Connection Variables
grafana_connection = {
        "url"  = "http://localhost:8080",
        "auth" = ""
    }


# Grafana_Contact_Point Variables
create_contact_point = true
contact_point_name   = "My Contact Point"
use_email            = true
use_slack            = true
email_contact_point = {
  addresses               = ["one@company.org", "two@company.org"]
  message                 = "{ len .Alerts.Firing } firing."
  subject                 = "{{ template "default.title" .}}"
  single_email            = true
  disable_resolve_message = false
}

slack_contact_point = {
        url  = "https://hooks.slack.com/<YOUR_SLACK_WEBHOOK_URL>"
        text = <<EOT
        {{ len .Alerts.Firing }} alerts are firing

        Alert summaries:
        {{ range .Alerts.Firing }}
        {{ template "Alert Instance Template" . }}
        {{ end }}
        EOT
}
    
    
# Use { template "Alert Instance Template" . } or any other template if you plan # to create one. Otherwise, remove it from the text section of Slack in the above example


# Grafana_Message_Template Variables
create_message_template  = true
message_template_name    = "Alert Instance Template"
message_template_content = <<EOT
{{ define "Alert Instance Template" }}
Firing: {{ .Labels.alertname }}
Silence: {{ .SilenceURL }}
{{ end }}
EOT
    


# Grafana_Mute_Timing Variables
create_mute_timing = true
mute_timing = {
  name          = "My Mute Timing"
  start         = "04:56"
  end           = "04:57"
  weekdays      = ["monday", "tuesday:thursday"]
  days_of_month = ["1:7", "-1"]
  months        = ["1:3", "december"]
  years         = []
}

    


# Grafana_Notification_Policy Variables
create_notification_policy = true
notification_policy_config = {
  group_by        = ["..."]
  group_wait      = "45s"
  group_interval  = "6m"
  repeat_interval = "3h"
}
    
    
policies = []
/* policies = [
  {
matchers = [
      { label = "mylabel", match = "=", value = "myvalue" },
      { label = "alertname", match = "=", value = "CPU Usage" },
      { label = "Name", match = "=~", value = "host.*|host-b.*" }
    ]
    contact_point = "a_contact_point_1"
    continue      = true
    mute_timings  = ["mute_timing_1"]
    group_by      = ["group1_sub"]
  },
  {
    matchers = [
      { label = "sublabel", match = "=", value = "subvalue" }
    ]
    contact_point = "a_contact_point_1"
    continue      = false
    mute_timings  = ["mute_timing_2"]
    group_by      = ["group2_sub"]
}
    
    
] */
    
    
    