import os
def ansible_nginx_install_ubuntu(input):

    nginx_hosts = input.hosts
    nginx_inventory = (f"[nginx_nodes]\n" + "\n".join(nginx_hosts))
    nginx_version = '*' if input.version == 'latest' else input.version
    nginx_ansible_port = input.ansible_port
    nginx_ansible_user = input.ansible_user
    nginx_repo_key_in_task = "{{ nginx_repo_key_url }}"
    nginx_repo_in_task = "deb {{ nginx_repo_url }} {{ ansible_distribution_release }} nginx"
    nginx_version_in_task = "nginx={{ nginx_version }}~{{ ansible_distribution_release }}"


    

    project_name = "app/media/MyAnsible"
    ansible_dir = project_name
    group_vars_dir = os.path.join(ansible_dir, "group_vars")
    host_vars_dir = os.path.join(ansible_dir, "host_vars")
    roles_dir = os.path.join(ansible_dir, "roles")
    install_nginx_dir = os.path.join(roles_dir, "install_nginx")
    tasks_dir = os.path.join(install_nginx_dir, "tasks")
    vars_dir = os.path.join(install_nginx_dir, "vars")
    defaults_dir = os.path.join(install_nginx_dir, "defaults")
    files_dir = os.path.join(install_nginx_dir, "files")
    handlers_dir = os.path.join(install_nginx_dir, "handlers")
    templates_dir = os.path.join(install_nginx_dir, "templates")

    # Create project directories
    os.makedirs(group_vars_dir, exist_ok=True)
    os.makedirs(host_vars_dir, exist_ok=True)
    os.makedirs(roles_dir, exist_ok=True)
    os.makedirs(install_nginx_dir, exist_ok=True)
    os.makedirs(tasks_dir, exist_ok=True)
    os.makedirs(vars_dir, exist_ok=True)
    os.makedirs(defaults_dir, exist_ok=True)
    os.makedirs(files_dir, exist_ok=True)
    os.makedirs(handlers_dir, exist_ok=True)
    os.makedirs(templates_dir, exist_ok=True)

    # Create ansible.cfg
    with open(os.path.join(ansible_dir, "ansible.cfg"), "w") as ansible_cfg:
        ansible_cfg.write("[defaults]\n")
        ansible_cfg.write("host_key_checking=false\n")

    # Create group_vars/nginx_nodes
    with open(os.path.join(group_vars_dir, "nginx_nodes"), "w") as nginx_nodes:
        nginx_nodes.write(f"ansible_port : {nginx_ansible_port}\n")
        nginx_nodes.write(f"ansible_user : {nginx_ansible_user}\n")

    # Create hosts
    with open(os.path.join(ansible_dir, "hosts"), "w") as hosts_file:
        
        hosts_file.write(f"{nginx_inventory}")
       

    # Create empty host_vars directory (already created)

    # Create nginx_playbook.yml
    with open(os.path.join(ansible_dir, "nginx_playbook.yml"), "w") as playbook:
        playbook.write("- hosts: all\n")
        playbook.write("  roles:\n")
        playbook.write("    - install_nginx\n")

    # Create install_nginx/tasks/main.yml
    with open(os.path.join(tasks_dir, "main.yml"), "w") as tasks_file:
        tasks_file.write("---\n")
        tasks_file.write("- name: Install CA certificates to ensure HTTPS connections work\n")
        tasks_file.write("  apt:\n")
        tasks_file.write("    name: ca-certificates\n")
        tasks_file.write("    state: present\n\n")
        tasks_file.write("- name: Add Nginx signing key\n")
        tasks_file.write("  apt_key:\n")
        tasks_file.write("    url: \"{ nginx_repo_key_url }\"\n")
        tasks_file.write("    state: present\n\n")
        tasks_file.write("- name: Add Nginx repository\n")
        tasks_file.write("  apt_repository:\n")
        tasks_file.write("    repo: \"deb {{ nginx_repo_url }} {{ ansible_distribution_release }} nginx\"\n")
        tasks_file.write("    state: present\n")
        tasks_file.write("    filename: nginx\n\n")
        tasks_file.write("- name: Update apt cache\n")
        tasks_file.write("  apt:\n")
        tasks_file.write("    update_cache: yes\n\n")
        tasks_file.write("- name: Install specific version of Nginx\n")
        tasks_file.write("  apt:\n")
        tasks_file.write("    name: \"nginx={{ nginx_version }}~{{ ansible_distribution_release }}\"\n")
        tasks_file.write("    state: present\n\n")
        tasks_file.write("- name: Ensure Nginx service is running and enabled\n")
        tasks_file.write("  service:\n")
        tasks_file.write("    name: nginx\n")
        tasks_file.write("    state: started\n")
        tasks_file.write("    enabled: yes\n")

        # Create install_nginx/vars/main.yml
        with open(os.path.join(vars_dir, "main.yml"), "w") as vars_file:
            vars_file.write("nginx_repo_key_url: \"https://nginx.org/keys/nginx_signing.key\"\n")
            vars_file.write("nginx_repo_url: \"http://nginx.org/packages/mainline/ubuntu/\"\n")
            vars_file.write(f"nginx_version: \"{nginx_version}\"\n")
        
    
def ansible_nginx_install(input):
    
    if input.os == 'ubuntu':
        return ansible_nginx_install_ubuntu(input)
