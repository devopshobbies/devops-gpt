def ansible_nginx_install_ubuntu(input):

    nginx_hosts = input.hosts
    nginx_inventory = (f"[nginx_nodes]\n" + "\n".join(nginx_hosts))
    nginx_version = '*' if input.version == 'latest' else input.version
    nginx_ansible_port = input.ansible_port
    nginx_ansible_user = input.ansible_user
    nginx_repo_key_in_task = "{{ nginx_repo_key_url }}"
    nginx_repo_in_task = "deb {{ nginx_repo_url }} {{ ansible_distribution_release }} nginx"
    nginx_version_in_task = "nginx={{ nginx_version }}~{{ ansible_distribution_release }}"


    prompt = f"""
              Generate a Python code to generate an Ansible project (project name is app/media/MyAnsible)
              that dynamically provisions Ansible resources ensuring a modular, flexible structure. Only provide
              Python code, no explanations or markdown formatting, without ```python entry.
              The project should be organized as follows:

              The structure of this project must be as follows:
              ```
              ├── ansible.cfg
              ├── group_vars
              │   |── nginx_nodes
              │  
              ├── hosts
              ├── host_vars
              ├── nginx_playbook.yml
              └── roles
                  └── install_nginx
                      ├── defaults
                      │   └── main.yml
                      ├── handlers
                      │   └── main.yml
                      ├── tasks
                      │   └── main.yml
                      ├── templates
                      │   └── main.yml
                      └── vars
                          └── main.yml
              ```
            - The content of ansible.cfg must be as follows:
              ```
              [defaults]
              host_key_checking=false
              ```
            - group_vars directory includes a single file called "nginx_nodes" and the content of this file must be as follows:
              ```
              ansible_port: {nginx_ansible_port}
              ansible_user: {nginx_ansible_user}
              ```
            - there is file called "hosts" which its content must be as follows:
                  ```
              {nginx_inventory}
              ```
            - There is an empty directory called "host_vars" with no files included
            - There is a file called "nginx_playbook.yml" which its content must be as follows:
              ```
              - hosts: all
                roles:
                  - install_nginx
              ```
            - There is a directory called "roles" which a sub-directory called "install_nginx" (roles/install_nginx)
              "install_nginx" has multiple sub-directories, so let's dive deeper into each its sub-directories:
                   - (install_nginx/tasks): This path has a file called "main.yml" which its content must be as follows:
                   ```
                   ---
                   - name: Install CA certificates to ensure HTTPS connections work
                     apt:
                       name: ca-certificates
                       state: present

                   - name: Add Nginx signing key
                     apt_key:
                       url: "{nginx_repo_key_in_task}"
                       state: present

                   - name: Add Nginx repository
                     apt_repository:
                       repo: "{nginx_repo_in_task}"
                       state: present
                       filename: nginx

                   - name: Update apt cache
                     apt:
                       update_cache: yes

                   - name: Install specific version of Nginx
                     apt:
                       name: "{nginx_version_in_task}"
                       state: present

                   - name: Ensure Nginx service is running and enabled
                     service:
                       name: nginx
                       state: started
                       enabled: yes
                   ```
                   - (install_nginx/vars): This path has a file called "main.yml" which its content must be as follows:
                   ```
                   nginx_repo_key_url: "https://nginx.org/keys/nginx_signing.key"
                   nginx_repo_url: "http://nginx.org/packages/mainline/ubuntu/"
                   nginx_version: "{nginx_version}"
                   ```
                   
                    finally just give me a python code without any note that can generate a project folder with the
                    given schema without ```python entry. and we dont need any base directory in the python code.
                    the final ansible template must work very well without any error!
                    
                    the python code you give me, must have structure like that:
                    
                    import os
                    project_name = "app/media/MyAnsible"
                    foo_dir = os.path.join(project_name, "bar")
                    x_dir = os.path.join(modules_dir, "y")

                    # Create project directories
                    os.makedirs(ansible_dir, exist_ok=True)

                    # Create main.tf
                    with open(os.path.join(project_name, "main.tf"), "w") as main_file:
                        # any thing you need
            """
    return prompt
     
    
def ansible_nginx_install(input):
    
    if input.os == 'ubuntu':
        return ansible_nginx_install_ubuntu(input)
