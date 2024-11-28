def ansible_docker_install(input):
    
    docker_hosts = input.hosts
    docker_inventory = (f"[docker_nodes]\n" + "\n".join(docker_hosts))
    docker_ansible_port = input.ansible_port
    docker_ansible_user = input.ansible_user
    docker_items_in_task = "{{ item }}"
    docker_prerequisite_packages_in_task = "{{ prerequisite_packages }}"
    ansible_architecture_in_task = "{{ ansible_architecture }}"
    ansible_distribution_release_in_task = "{{ ansible_distribution_release }}"
    docker_packages_in_task = "{{ docker_packages }}"
    docker_services_in_task = "{{ docker_services }}"



    prompt = f"""
              Generate a Python code to generate an Ansible project (project name is app/media/MyAnsible)
              that dynamically provisions Ansible resources ensuring a modular, flexible structure. Only provide
              Python code, no explanations or markdown formatting, without ```python entry.
              The project should be organized as follows:

              The structure of this project must be as follows:
              ```
              ├── ansible.cfg
              ├── group_vars
              │   |── docker_nodes
              │  
              ├── hosts
              ├── host_vars
              ├── docker_playbook.yml
              └── roles
                  └── install_docker
                      ├── defaults
                      │   └── main.yml
                      ├── files
                      │   └── sample.sh
                      ├── handlers
                      │   └── main.yml
                      ├── tasks
                      │   └── main.yml
                      ├── templates
                      │   └── sample.j2
                      └── vars
                          └── main.yml
              ```
            - The content of ansible.cfg must be as follows:
              ```
              [defaults]
              host_key_checking=false
              ```
            - group_vars directory includes a single file called "docker_nodes" and the content of this file must be as follows:
              ```
              ansible_port: {docker_ansible_port}
              ansible_user: {docker_ansible_user}
              ```
            - there is file called "hosts" which its content must be as follows:
                  ```
              {docker_inventory}
              ```
            - There is an empty directory called "host_vars" with no files included
            - There is a file called "docker_playbook.yml" which its content must be as follows:
              ```
              - hosts: all
                roles:
                  - install_docker
              ```
            - There is a directory called "roles" which a sub-directory called "install_docker" (roles/install_docker)
              "install_docker" has multiple sub-directories, so let's dive deeper into each its sub-directories:
                   - (install_docker/tasks): This path has a file called "main.yml" which its content must be as follows:
                   ```
                   ---
                   - name: Install prerequisite packages
                     apt:
                       name: "{docker_items_in_task}"
                       state: present
                     loop: "{docker_prerequisite_packages_in_task}""
                   - name: Create directory for Docker keyrings
                     file:
                       path: /etc/apt/keyrings
                       state: directory
                       mode: '0755'
                   - name: Download Docker's official GPG key
                     get_url:
                       url: https://download.docker.com/linux/ubuntu/gpg
                       dest: /etc/apt/keyrings/docker.asc
                       mode: '0644'
                   - name: Add Docker repository to apt sources
                     copy:
                       content: |
                         deb [arch={ansible_architecture_in_task} signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu {ansible_distribution_release_in_task} stable
                       dest: /etc/apt/sources.list.d/docker.list
                   - name: Update apt cache after adding Docker repo
                     apt:
                       update_cache: yes
                   - name: Install Docker packages
                     apt:
                       name: "{docker_items_in_task}"
                       state: present
                     loop: "{docker_packages_in_task}""
                   - name: Ensure Docker and containerd services are started and enabled
                     service:
                       name: "{docker_items_in_task}"
                       state: started
                       enabled: yes
                     loop: "{docker_services_in_task}""
                   ```
                   - (install_docker/vars): This path has a file called "main.yml" which its content must be as follows:
                   ```
                   prerequisite_packages:
                     - ca-certificates
                     - curl

                   docker_services:
                     - docker
                     - containerd

                   docker_packages:
                     - docker-ce
                     - docker-ce-cli
                     - containerd.io
                     - docker-buildx-plugin
                     - docker-compose-plugin
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
