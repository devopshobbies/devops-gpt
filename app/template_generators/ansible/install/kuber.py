def ansible_kuber_install(input):
    

    kubernetes_ansible_port = input.ansible_port
    kubernetes_ansible_user = input.ansible_user
    k8s_master_nodes = input.k8s_master_nodes
    k8s_worker_nodes = input.k8s_worker_nodes
    lb_nodes = input.lb_nodes
    k8s_version = input.version
    sections = {
      "[all]": [f"{name} private_ip=x.x.x.x" for name in k8s_master_nodes + k8s_worker_nodes + lb_nodes],
      "[k8s]": k8s_master_nodes + k8s_worker_nodes,
      "[k8s_masters]": k8s_master_nodes,
      "[k8s_workers]": k8s_worker_nodes,
      "[lb]": lb_nodes,
    }
    kubernetes_inventory = "\n\n".join(f"{section}\n" + "\n".join(entries) for section, entries in sections.items())

    inventory_hostname = "{{ inventory_hostname }}"



    prompt = f"""
              Generate a Python code to generate an Ansible project (project name is app/media/MyAnsible)
              that dynamically provisions Ansible resources ensuring a modular, flexible structure. Only provide
              Python code, no explanations or markdown formatting, without ```python entry.
              The project should be organized as follows:

              The structure of this project must be as follows:
              ```
              ├── ansible.cfg
              ├── group_vars
              │   |── all
              │  
              ├── hosts
              ├── host_vars
              ├── kubernetes_playbook.yml
              └── roles
                  └── preinstall
                      ├── defaults
                      │   └── main.yml
                      ├── files
                      │   └── sample.sh
                      ├── handlers
                      │   └── main.yml
                      ├── tasks
                      │   └── basic.yml
                      │   └── main.yml
                      ├── templates
                      │   └── resolv.conf.j2
                      └── vars
                          └── main.yml
              ```
            - The content of ansible.cfg must be as follows:
              ```
              [defaults]
              host_key_checking=false
              ```
            - group_vars directory includes a single file called "all" and the content of this file must be as follows:
              ```
              # General
              install_ansible_modules: "true"
              disable_transparent_huge_pages: "true"
              setup_interface: "false"

              # Network Calico see here for more details https://github.com/projectcalico/calico/releases
              calico_operator_url: "https://raw.githubusercontent.com/projectcalico/calico/v3.29.0/manifests/tigera-operator.yaml"
              calico_crd_url: "https://raw.githubusercontent.com/projectcalico/calico/v3.29.0/manifests/custom-resources.yaml"
              pod_network_cidr: "192.168.0.0/16"

              # DNS
              resolv_nameservers: [8.8.8.8, 4.2.2.4] # 403.online

              # Sanction shekan
              use_iran: "true" # change it to "false" if you are outside of iran

              # Docker
              docker_gpg_key_url: "https://download.docker.com/linux/ubuntu/gpg"
              docker_gpg_key_path: "/etc/apt/keyrings/docker.gpg"
              docker_apt_repo: "https://download.docker.com/linux/ubuntu"

              # Kubernetes
              kubernetes_gpg_keyring_path: "/etc/apt/keyrings/kubernetes-apt-keyring.gpg"
              kubernetes_gpg_key_url: "https://pkgs.k8s.io/core:/stable:/v{k8s_version}/deb/Release.key"
              kubernetes_apt_repo: "https://pkgs.k8s.io/core:/stable:/v{k8s_version}/deb/"
              k8s_version: "{k8s_version}.2" # see here https://kubernetes.io/releases/patch-releases/ and https://github.com/kubernetes/kubernetes/releases

              # CRI
              cri_socket: unix:///var/run/containerd/containerd.sock

              # VRRP and HAProxy
              interface_name: "enp0s8"
              virtual_ip: "192.168.178.100"
              haproxy_frontend_password: "password"

              # Ansible Connection

              ansible_user: {kubernetes_ansible_user}
              ansible_port: {kubernetes_ansible_port}
              ansible_python_interpreter: "/usr/bin/python3"
              domain="devopsgpt.com"
              apiserver_url="devopsgpt.com"
              ```
            - there is file called "hosts" which its content must be as follows:
                  ```
              {kubernetes_inventory}
              ```
            - There is an empty directory called "host_vars" with no files included
            - There is a file called "kubernetes_playbook.yml" which its content must be as follows:
              ```
              - hosts: all
                roles:
                  - role: preinstall
                gather_facts: yes
                any_errors_fatal: true
                tags: [preinstall]
              ```
            - There is a directory called "roles" which a sub-directory called "preinstall" (roles/preinstall):
              "preinstall" has multiple sub-directories, so let's dive deeper into each its sub-directories:
                   - (preinstall/tasks): This path has two files called "basic.yml" and "main.yml".

                   "(preinstall/tasks/basic.yml) must be as follows:"
                   ```
                   - name: Set timezone to UTC
                     timezone:
                       name: Etc/UTC

                   - name: Set hostname
                     command: hostnamectl set-hostname {inventory_hostname}

                   - name: Remove symlink resolve.conf
                     file:
                       path: "/etc/resolv.conf"
                       state: absent
                     ignore_errors: true
                     when: use_iran == "true"

                   - name: Configure resolv.conf
                     template:
                       src: "resolv.conf.j2"
                       dest: "/etc/resolv.conf"
                       mode: "0644"
                     when: use_iran == "true"

                   - name: Add hostname
                     lineinfile:
                       path: /etc/hosts
                       regexp: '^127\.0\.0\.1'
                       line: "127.0.0.1 {inventory_hostname} localhost"
                       owner: root
                       group: root
                       mode: 0644

                   - name: Install necessary tools
                     apt:
                       update_cache: true
                       name:
                         - vim
                         - sudo
                         - wget
                         - curl
                         - telnet
                         - nload
                         - s3cmd
                         - cron
                         - ipset
                         - lvm2
                         - python3
                         - python3-setuptools
                         - python3-pip
                         - python3-apt
                         - intel-microcode
                         - htop
                         - tcpdump
                         - net-tools
                         - screen
                         - tmux
                         - byobu
                         - iftop
                         - bmon
                         - iperf
                         - sysstat
                         - ethtool
                         - plocate
                         - thin-provisioning-tools
                         - conntrack
                         - stress
                         - cpufrequtils
                         - rsync
                         - xz-utils
                         - build-essential
                         - apt-transport-https
                         - ca-certificates
                         - software-properties-common
                         - gnupg-agent
                         - iptables-persistent
                         - open-iscsi
                         - nfs-common
                         - tzdata
                         - tree
                       state: latest

                   - name: Fix broken packages
                     apt:
                       state: fixed
                   ```

                   "(preinstall/tasks/main.yml) must be as follows:"
                   ```
                   ---
                   - name: basic setup
                     include_tasks: basic.yml
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
