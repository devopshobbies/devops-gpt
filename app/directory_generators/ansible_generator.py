import os

project_name = "app/media/MyAnsible"

# Create project directories
os.makedirs(os.path.join(project_name, "group_vars"), exist_ok=True)
os.makedirs(os.path.join(project_name, "host_vars"), exist_ok=True)
os.makedirs(os.path.join(project_name, "roles", "install_docker", "defaults"), exist_ok=True)
os.makedirs(os.path.join(project_name, "roles", "install_docker", "files"), exist_ok=True)
os.makedirs(os.path.join(project_name, "roles", "install_docker", "handlers"), exist_ok=True)
os.makedirs(os.path.join(project_name, "roles", "install_docker", "tasks"), exist_ok=True)
os.makedirs(os.path.join(project_name, "roles", "install_docker", "templates"), exist_ok=True)
os.makedirs(os.path.join(project_name, "roles", "install_docker", "vars"), exist_ok=True)

# Create ansible.cfg
with open(os.path.join(project_name, "ansible.cfg"), "w") as ansible_cfg:
    ansible_cfg.write("[defaults]\n")
    ansible_cfg.write("host_key_checking=false\n")

# Create group_vars/docker_nodes
with open(os.path.join(project_name, "group_vars", "docker_nodes"), "w") as docker_nodes:
    docker_nodes.write("ansible_port: 22\n")
    docker_nodes.write("ansible_user: root\n")

# Create hosts
with open(os.path.join(project_name, "hosts"), "w") as hosts_file:
    hosts_file.write("[docker_nodes]\n")
    hosts_file.write("www.example.com\n")

# Create docker_playbook.yml
with open(os.path.join(project_name, "docker_playbook.yml"), "w") as playbook:
    playbook.write("- hosts: all\n")
    playbook.write("  roles:\n")
    playbook.write("    - install_docker\n")

# Create install_docker/tasks/main.yml
with open(os.path.join(project_name, "roles", "install_docker", "tasks", "main.yml"), "w") as tasks_file:
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

# Create install_docker/vars/main.yml
with open(os.path.join(project_name, "roles", "install_docker", "vars", "main.yml"), "w") as vars_file:
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