import os
project_name = "app/media/MyJcasc"
jcasc_dir = os.path.join(project_name, "jcasc")
os.makedirs(jcasc_dir, exist_ok=True)

jcasc_content = """
systemMessage: "Welcome to Jenkins configured via JCasC"
author:
  name: "admin"
  password: "password"
allowSignup: true
allowAnonymousRead: true
cache_size: 1
executors: 1
required_plugins:
  - "string"
views:
  - list:
      name: "All"
authorizationStrategy:
  projectMatrix:
    grantedPermissions:
      - "Overall/Administer:admin"
      - "Job/Read:developer"
      - "Job/Build:developer"
tools:
  git:
    installations:
      - name: "Default"
        home: "/usr/bin/git"
security:
  globalJobDslSecurityConfiguration:
    useScriptSecurity: false
"""

with open(os.path.join(jcasc_dir, "config.yaml"), "w") as f:
    f.write(jcasc_content.strip())