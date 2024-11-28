import os

project_name = "app/media/MyAnsible"
ansible_dir = project_name
group_vars_dir = os.path.join(ansible_dir, "group_vars")
host_vars_dir = os.path.join(ansible_dir, "host_vars")
roles_dir = os.path.join(ansible_dir, "roles")
install_docker_dir = os.path.join(roles_dir, "install_docker")
tasks_dir = os.path.join(install_docker_dir, "tasks")
vars_dir = os.path.join(install_docker_dir, "vars")
files_dir = os.path.join(install_docker_dir, "files")
handlers_dir = os.path.join(install_docker_dir, "handlers")
templates_dir = os.path.join(install_docker_dir, "templates")

# Create project directories
os.makedirs(ansible_dir, exist_ok=True)
os.makedirs(group_vars_dir, exist_ok=True)
os.makedirs(host_vars_dir, exist_ok=True)
os.makedirs(roles_dir, exist_ok=True)
os.makedirs(install_docker_dir, exist_ok=True)
os.makedirs(tasks_dir, exist_ok=True)
os.makedirs(vars_dir, exist_ok=True)
os.makedirs(files_dir, exist_ok=True)
os.makedirs(handlers_dir, exist_ok=True)
os.makedirs(templates_dir, exist_ok=True)

# Create ansible.cfg
with open(os.path.join(ansible_dir, "ansible.cfg"), "w") as cfg_file:
    cfg_file.write("[defaults]\n")
    cfg_file.write("host_key_checking=false\n")

# Create group_vars/docker_nodes
with open(os.path.join(group_vars_dir, "docker_nodes"), "w") as gv_file:
    gv_file.write("ansible_port: 28\n")
    gv_file.write("ansible_user: root\n")

# Create hosts
with open(os.path.join(ansible_dir, "hosts"), "w") as hosts_file:
    hosts_file.write("[docker_nodes]\n")
    hosts_file.write("www.example.com\n")

# Create docker_playbook.yml
with open(os.path.join(ansible_dir, "docker_playbook.yml"), "w") as playbook_file:
    playbook_file.write("- hosts: all\n")
    playbook_file.write("  roles:\n")
    playbook_file.write("    - install_docker\n")

# Create tasks/main.yml
with open(os.path.join(tasks_dir, "main.yml"), "w") as tasks_file:
    tasks_file.write("---\n")
    tasks_file.write("- name: Install prerequisite packages\n")
    tasks_file.write("  apt:\n")
    tasks_file.write("    name: \"{{ item }}\"\n")
    tasks_file.write("    state: present\n")
    tasks_file.write("  loop: \"{{ prerequisite_packages }}\"\n")
    tasks_file.write("- name: Create directory for Docker keyrings\n")
    tasks_file.write("  file:\n")
    tasks_file.write("    path: /etc/apt/keyrings\n")
    tasks_file.write("    state: directory\n")
    tasks_file.write("    mode: '0755'\n")
    tasks_file.write("- name: Download Docker's official GPG key\n")
    tasks_file.write("  get_url:\n")
    tasks_file.write("    url: https://download.docker.com/linux/ubuntu/gpg\n")
    tasks_file.write("    dest: /etc/apt/keyrings/docker.asc\n")
    tasks_file.write("    mode: '0644'\n")
    tasks_file.write("- name: Add Docker repository to apt sources\n")
    tasks_file.write("  copy:\n")
    tasks_file.write("    content: |\n")
    tasks_file.write("      deb [arch={{ ansible_architecture }} signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu {{ ansible_distribution_release }} stable\n")
    tasks_file.write("    dest: /etc/apt/sources.list.d/docker.list\n")
    tasks_file.write("- name: Update apt cache after adding Docker repo\n")
    tasks_file.write("  apt:\n")
    tasks_file.write("    update_cache: yes\n")
    tasks_file.write("- name: Install Docker packages\n")
    tasks_file.write("  apt:\n")
    tasks_file.write("    name: \"{{ item }}\"\n")
    tasks_file.write("    state: present\n")
    tasks_file.write("  loop: \"{{ docker_packages }}\"\n")
    tasks_file.write("- name: Ensure Docker and containerd services are started and enabled\n")
    tasks_file.write("  service:\n")
    tasks_file.write("    name: \"{{ item }}\"\n")
    tasks_file.write("    state: started\n")
    tasks_file.write("    enabled: yes\n")
    tasks_file.write("  loop: \"{{ docker_services }}\"\n")

# Create vars/main.yml
with open(os.path.join(vars_dir, "main.yml"), "w") as vars_file:
    vars_file.write("prerequisite_packages:\n")
    vars_file.write("  - ca-certificates\n")
    vars_file.write("  - curl\n\n")
    vars_file.write("docker_services:\n")
    vars_file.write("  - docker\n")
    vars_file.write("  - containerd\n\n")
    vars_file.write("docker_packages:\n")
    vars_file.write("  - docker-ce\n")
    vars_file.write("  - docker-ce-cli\n")
    vars_file.write("  - containerd.io\n")
    vars_file.write("  - docker-buildx-plugin\n")
    vars_file.write("  - docker-compose-plugin\n")

# Create empty host_vars directory
os.makedirs(host_vars_dir, exist_ok=True)

# Create empty files directory
os.makedirs(files_dir, exist_ok=True)

# Create empty handlers directory
os.makedirs(handlers_dir, exist_ok=True)

# Create empty templates directory
os.makedirs(templates_dir, exist_ok=True)