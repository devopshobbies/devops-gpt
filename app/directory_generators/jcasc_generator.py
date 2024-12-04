import os
project_name = "app/media/MyJcasc"
jcasc_dir = os.path.join(project_name, "jcasc")

# Create project directories
os.makedirs(jcasc_dir, exist_ok=True)

# Define the JCasc content
jcasc_content = """
jenkins:
  numExecutors: 1
  scmCheckoutRetryCount: 2
  mode: NORMAL
  markupFormatter:
    rawHtml:
      disableSyntaxHighlighting: false
  primaryView:
    all:
      name: "all"
  crumbIssuer:
    standard:
      excludeClientIPFromCrumb: true
credentials:
  system:
    domainCredentials:
      - credentials:
          - string:
              scope: GLOBAL
              id: "gitlab-token"
              secret: "SECRET KEY"
              description: "GitLab personal access token"
unclassified:
  location:
    url: "http://localhost:8080/"
security:
  globalJobDslSecurityConfiguration:
    useScriptSecurity: false
jobs:
  - script: >
      pipelineJob('DSL Job') {
          quietPeriod(0)
          properties {
              disableConcurrentBuilds()
          }
          logRotator {
              numToKeep(10)
          }
          triggers {
              cron("H/15 * * * *")
          }
          definition {
              cps {
                  script('createJobs()')
              }
          }
      }
"""

# Write the JCasc content to a file
with open(os.path.join(jcasc_dir, "jcasc.yaml"), "w") as f:
    f.write(jcasc_content.strip())