def jcasc_template_generator(input) -> str:
    
    DSL_Job_Name = 'false' if input.allowsSignup else 'true'
    useScriptSecurity = 'true' if input.useScriptSecurity else 'false'
    scmCheckoutRetryCount = input.scmCheckoutRetryCount
    executators = input.executators


    prompt = f"""
        Generate a Python code, to generate a JCasc file (project name is app/media/MyJcasc)
        and install plugins based on the provided list, ensuring a modular, flexible structure to enable users
        to configure all essential settings at the first load. Only provide JCasc code, no explanations or
        markdown formatting.
        
        Also the file should contain ONLY these sections with following order and do not add emptylines:
        - jenkins:
            - numExecutors= {executators}
            - scmCheckoutRetryCount= {scmCheckoutRetryCount}
            - mode : NORMAL
            - markupFormatter:
            ```
                rawHtml:
                disableSyntaxHighlighting: false
            ```
            - primaryView:
            ```
                all:
                name: "all"
            ```
            -   crumbIssuer:
                    standard:
                    excludeClientIPFromCrumb: true
        - credentials:
            ```
            system:
                domainCredentials:
                - credentials:
                    - string:
                        scope: GLOBAL
                        id: "gitlab-token"
                        secret: "SECRET KEY"
                        description: "GitLab personal access token"
            ```
        - unclassified:
            ```
            location:
                url: "http://localhost:8080/"
            ```
        - security:
          ```
            globalJobDslSecurityConfiguration:
                useScriptSecurity: {useScriptSecurity}
          ```
        - jobs:
           ``` - script: >
                pipelineJob('{DSL_Job_Name}') {{
                    quietPeriod(0)
                    properties {{
                    disableConcurrentBuilds()
                    }}
                    logRotator {{
                    numToKeep(10)
                    }}
                    triggers {{
                    cron("H/15 * * * *")
                    }}
                    definition {{
                    cps {{
                        script('createJobs()')
                    }}
                    }}
                }}
            ```
        finally the python code should run without any note that can generate a project folder with the given
        schema without 
        python entry. the final JCasc template must work very well without any error!

        import os
        project_name = "app/media/MyJcasc"
        jcasc_dir = os.path.join(project_name, "jcasc")

        # Create project directories
        os.makedirs(jcasc_dir, exist_ok=True)

    """
    return prompt