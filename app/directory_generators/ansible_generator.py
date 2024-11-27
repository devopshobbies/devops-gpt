import os

project_name = "app/media/MyAnsible"

# Define directory structure
ansible_dir = project_name
group_vars_dir = os.path.join(ansible_dir, "group_vars")
hosts_file = os.path.join(ansible_dir, "hosts")
host_vars_dir = os.path.join(ansible_dir, "host_vars")
nginx_playbook_file = os.path.join(ansible_dir, "nginx_playbook.yml")
roles_dir = os.path.join(ansible_dir, "roles")
install_nginx_dir = os.path.join(roles_dir, "install_nginx")
defaults_dir = os.path.join(install_nginx_dir, "defaults")
handlers_dir = os.path.join(install_nginx_dir, "handlers")
tasks_dir = os.path.join(install_nginx_dir, "tasks")
templates_dir = os.path.join(install_nginx_dir, "templates")
vars_dir = os.path.join(install_nginx_dir, "vars")

# Create project directories
os.makedirs(group_vars_dir, exist_ok=True)
os.makedirs(host_vars_dir, exist_ok=True)
os.makedirs(tasks_dir, exist_ok=True)
os.makedirs(defaults_dir, exist_ok=True)
os.makedirs(handlers_dir, exist_ok=True)
os.makedirs(templates_dir, exist_ok=True)
os.makedirs(vars_dir, exist_ok=True)
os.makedirs(roles_dir, exist_ok=True)
os.makedirs(install_nginx_dir, exist_ok=True)

# Create ansible.cfg
with open(os.path.join(ansible_dir, "ansible.cfg"), "w") as ansible_config:
    ansible_config.write("[defaults]\n")
    ansible_config.write("host_key_checking=false\n")

# Create group_vars/nginx_nodes
with open(os.path.join(group_vars_dir, "nginx_nodes"), "w") as nginx_nodes:
    nginx_nodes.write("ansible_port: 22\n")
    nginx_nodes.write("ansible_user: root\n")

# Create hosts file
with open(hosts_file, "w") as hosts:
    hosts.write("[nginx_nodes]\n")
    hosts.write("www.examppple.com\n")

# Create nginx_playbook.yml
with open(nginx_playbook_file, "w") as playbook:
    playbook.write("- hosts: all\n")
    playbook.write("  roles:\n")
    playbook.write("    - install_nginx\n")

# Create install_nginx/tasks/main.yml
with open(os.path.join(tasks_dir, "main.yml"), "w") as tasks:
    tasks.write("---\n")
    tasks.write("- name: Install CA certificates to ensure HTTPS connections work\n")
    tasks.write("  apt:\n")
    tasks.write("    name: ca-certificates\n")
    tasks.write("    state: present\n\n")
    
    tasks.write("- name: Add Nginx signing key\n")
    tasks.write("  apt_key:\n")
    tasks.write("    url: \"{ nginx_repo_key_url }\"\n")
    tasks.write("    state: present\n\n")

    tasks.write("- name: Add Nginx repository\n")
    tasks.write("  apt_repository:\n")
    tasks.write("    repo: \"deb { nginx_repo_url } { ansible_distribution_release } nginx\"\n")
    tasks.write("    state: present\n")
    tasks.write("    filename: nginx\n\n")

    tasks.write("- name: Update apt cache\n")
    tasks.write("  apt:\n")
    tasks.write("    update_cache: yes\n\n")

    tasks.write("- name: Install specific version of Nginx\n")
    tasks.write("  apt:\n")
    tasks.write("    name: \"nginx={ nginx_version }~{ ansible_distribution_release }\"\n")
    tasks.write("    state: present\n\n")

    tasks.write("- name: Ensure Nginx service is running and enabled\n")
    tasks.write("  service:\n")
    tasks.write("    name: nginx\n")
    tasks.write("    state: started\n")
    tasks.write("    enabled: yes\n")

# Create install_nginx/vars/main.yml
with open(os.path.join(vars_dir, "main.yml"), "w") as vars_file:
    vars_file.write("nginx_repo_key_url: \"https://nginx.org/keys/nginx_signing.key\"\n")
    vars_file.write("nginx_repo_url: \"http://nginx.org/packages/mainline/ubuntu/\"\n")
    vars_file.write("nginx_version: \"1.23.4-1\"\n")