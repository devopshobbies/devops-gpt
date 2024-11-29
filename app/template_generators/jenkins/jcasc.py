def jcasc_template_generator(input) -> str:
    
    allowsSignup = 'true' if input.allowsSignup else 'false'
    allowAnonymousRead = 'true' if input.allowAnonymousRead else 'false'
    cache_size = input.cache_size
    executators = input.executators
    required_plugins = input.required_plugins


    prompt = f"""
        Generate a Python code, to generate a JCasc file (project name is app/media/MyJcasc)
        and install plugins based on the provided list, ensuring a modular, flexible structure to enable users
        to configure all essential settings at the first load. Only provide JCasc code, no explanations or
        markdown formatting. The file should be created based on these values
        - allowSignup = {allowsSignup}
        - allowAnonymousRead = {allowAnonymousRead}
        - cache_size = {cache_size}
        - executators = {executators}
        - required_plugins = {required_plugins}

        Also the file should contain ONLY these sections with following order and do not add emptylines:
        1- systemMessage
        2- create a local admin user and password, default username is admin and default password is password
        3- allowSignup
        4- allowAnonymousRead
        5- cache_size
        6- executators
        7- required_plugins
        8- views
        9- authorizationStrategy: 
            - ```
            projectMatrix:
                grantedPermissions:
                    - "Overall/Administer:admin"
                    - "Job/Read:developer"
                    - "Job/Build:developer"
            ```
        10- tools:
            - ```
                git:
                installations:
                    - name: "Default"
                    home: "/usr/bin/git"
            ```
        11- security:
            - ```
                globalJobDslSecurityConfiguration:
                    useScriptSecurity: false
            ```
        finally the python code should run without any note that can generate a project folder with the given
        schema without ```python entry. the final JCasc template must work very well without any error!

        import os
        project_name = "app/media/MyJcasc"
        jcasc_dir = os.path.join(project_name, "jcasc")

        # Create project directories
        os.makedirs(jcasc_dir, exist_ok=True)

    """
    return prompt