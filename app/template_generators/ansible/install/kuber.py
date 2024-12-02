def ansible_kuber_install(input):
   
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
    item_in_task = "{{ item }}"
    ufw_in_task = "'ufw'"
    docker_gpg_key_path_in_task = "{{ docker_gpg_key_path }}"
    docker_gpg_key_url_in_task = "{{ docker_gpg_key_url }}"
    architecture_stdout_in_task = "{{ architecture.stdout }}"
    docker_apt_repo_in_task = "{{ docker_apt_repo }}"
    distribution_codename_stdout_in_task = "{{ distribution_codename.stdout }}"
    kubernetes_gpg_keyring_path_in_task = "{{ kubernetes_gpg_keyring_path }}"
    kubernetes_gpg_key_url_in_task = "{{ kubernetes_gpg_key_url }}"
    kubernetes_apt_repo_in_task = "{{ kubernetes_apt_repo }}"
    private_ip_in_task = "{{ private_ip }}"
    hostvars_private_ip_in_task = "{{ hostvars[item].private_ip }}"
    domain_in_task = "{{ domain }}"
    groups_all_in_task = "{{ groups['all'] }}"
    hostvars_groups_k8s_masters_private_ip_in_task = "{{ hostvars[groups['k8s_masters'][0]].private_ip }}"
    apiserver_url_in_task = "{{ apiserver_url }}"
    groups_k8s_masters_in_task = "{{ groups['k8s_masters'][0] }}"
    calico_operator_url_in_task = "{{ calico_operator_url }}"
    calico_crd_url_in_task = "{{ calico_crd_url }}"



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
                      |    └── main.yml
                      k8s
                      ├── defaults
                      │   └── main.yml
                      ├── files
                      │   └── sample.sh
                      ├── handlers
                      │   └── main.yml
                      ├── tasks
                      │   └── k8s.yml
                      │   └── main.yml
                      ├── templates
                      │   └── sample.j2
                      └── vars
                      |    └── main.yml
                      init_k8s
                      ├── defaults
                      │   └── main.yml
                      ├── files
                      │   └── sample.sh
                      ├── handlers
                      │   └── main.yml
                      ├── tasks
                      │   └── cni.yml
                      │   └── initk8s.yml
                      │   └── main.yml
                      ├── templates
                      │   └── kubeadmcnf.yml.j2
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
              domain: "devopsgpt.com"
              apiserver_url: "devopsgpt.com"
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

              - hosts: k8s
                roles:
                  - role: k8s
                gather_facts: yes
                any_errors_fatal: true
                tags: [k8s]

              - hosts: k8s
                roles:
                  - role: init_k8s
                gather_facts: yes
                any_errors_fatal: true
                tags: [init_k8s]
              ```
            - There is a directory called "roles" which a sub-directory called "preinstall" (roles/preinstall):
              "preinstall" has multiple sub-directories, so let's dive deeper into each its sub-directories:
                 - (preinstall/tasks): This path has two files called "basic.yml" and "main.yml".

                   1. Create "preinstall/tasks/basic.yml" and it must be as follows:"
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
                       state: latest
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

                   - name: Fix broken packages
                     apt:
                       state: fixed
                   ```

                   2. Create preinstall/tasks/main.yml and it must be as follows:"
                   ```
                   ---
                   - name: basic setup
                     include_tasks: basic.yml
                   ```
            - There is a directory called "roles" which a sub-directory called "k8s" (roles/k8s):
              "k8s" has multiple sub-directories, so let's dive deeper into each its sub-directories:
                - (k8s/tasks): This path has two files called "k8s.yml" and "main.yml".

                   1. Create k8s/tasks/k8s.yml and it must be as follows:"
                   ```
                   - name: Disable SWAP since kubernetes can't work with swap enabled
                     shell: |
                       swapoff -a

                   - name: Disable SWAP in fstab since kubernetes can't work with swap enabled
                     replace:
                       path: /etc/fstab
                       regexp: '^([^#].*?\sswap\s+sw\s+.*)$'
                       replace: '# \\1'

                   - name: Check if ufw is installed
                     package_facts:
                       manager: "auto"

                   - name: Disable ufw # just in Ubuntu
                     ufw:
                       state: disabled
                     when: "{ufw_in_task} in ansible_facts.packages"

                   - name: Ensure kernel modules for containerd are enabled
                     lineinfile:
                       path: /etc/modules-load.d/containerd.conf
                       line: "{item_in_task}"
                       create: yes
                       state: present
                     loop:
                       - overlay
                       - br_netfilter

                   - name: Load kernel modules
                     command:
                       cmd: "modprobe {item_in_task}"
                     loop:
                       - overlay
                       - br_netfilter

                   - name: Ensure sysctl settings for Kubernetes are present
                     blockinfile:
                       path: /etc/sysctl.d/kubernetes.conf
                       block: |
                         net.bridge.bridge-nf-call-ip6tables = 1
                         net.bridge.bridge-nf-call-iptables = 1
                         net.ipv4.ip_forward = 1
                       create: yes
                       marker: "# {{mark}} ANSIBLE MANAGED BLOCK"
                       owner: root
                       group: root
                       mode: '0644'

                   - name: Reload sysctl settings
                     command:
                       cmd: sysctl --system

                   - name: Update apt cache
                     apt:
                       update_cache: yes

                   - name: Install required packages
                     apt:
                       pkg:
                         - ca-certificates
                         - curl
                         - gnupg
                         - lsb-release
                         - gpg

                       state: present
                       update_cache: yes

                   - name: Ensure the /etc/apt/keyrings directory exists
                     file:
                       path: /etc/apt/keyrings
                       state: directory
                       mode: '0755'  # Adjust the permissions as necessary
                       owner: root   # Set the owner, if required
                       group: root

                   - name: Remove existing Docker GPG key if it exists
                     file:
                       path: '{docker_gpg_key_path_in_task}'
                       state: absent

                   - name: Download Docker GPG key
                     shell: |
                       curl -fsSL {docker_gpg_key_url_in_task} | gpg --dearmor -o {docker_gpg_key_path_in_task}

                   - name: Determine the architecture
                     command: dpkg --print-architecture
                     register: architecture

                   - name: Determine the distribution codename
                     command: lsb_release -cs
                     register: distribution_codename

                   - name: Add Docker APT repository
                     lineinfile:
                       path: /etc/apt/sources.list.d/docker.list
                       create: yes
                       line: "deb [arch={architecture_stdout_in_task} signed-by={docker_gpg_key_path_in_task}] {docker_apt_repo_in_task} {distribution_codename_stdout_in_task} stable"
                       state: present

                   - name: Update apt cache
                     apt:
                       update_cache: yes

                   - name: Install required packages (containerd)
                     apt:
                       pkg:
                         - containerd.io
                       state: present

                   - name: Generate default containerd configuration
                     shell:
                       cmd: containerd config default > /etc/containerd/config.toml

                   - name: Replace SystemdCgroup from false to true in containerd config
                     replace:
                       path: /etc/containerd/config.toml
                       regexp: 'SystemdCgroup = false'
                       replace: 'SystemdCgroup = true'

                   - name: Restart containerd service
                     systemd:
                       name: containerd
                       state: restarted
                       daemon_reload: yes

                   - name: Enable containerd service
                     systemd:
                       name: containerd
                       enabled: yes
                   - name: Delete the existing Kubernetes APT keyring file if it exists
                     file:
                       path: '{kubernetes_gpg_keyring_path_in_task}'
                       state: absent

                   - name: Download Kubernetes GPG key
                     shell: |
                       curl -fsSL '{kubernetes_gpg_key_url_in_task}' | gpg --dearmor -o '{kubernetes_gpg_keyring_path_in_task}'

                   - name: Add Kubernetes repo
                     apt_repository:
                       repo: "deb [signed-by={kubernetes_gpg_keyring_path_in_task}] {kubernetes_apt_repo_in_task} /"
                       state: present
                       filename: kubernetes.list

                   - name: Update apt cache
                     apt:
                       update_cache: yes

                   - name: Install Kubernetes packages
                     apt:
                       name: "{item_in_task}"
                       state: present
                     loop:
                       - kubeadm={k8s_version}.2-1.1
                       - kubelet={k8s_version}.2-1.1
                       - kubectl={k8s_version}.2-1.1

                   - name: Hold Kubernetes packages
                     dpkg_selections:
                       name: "{item_in_task}"
                       selection: hold
                     loop:
                       - kubeadm
                       - kubelet
                       - kubectl
                       - containerd.io

                   - name: Configure node ip
                     lineinfile:
                       path: /etc/default/kubelet
                       line: KUBELET_EXTRA_ARGS=--node-ip={private_ip_in_task}
                       create: yes
                       state: present
                     notify: Restart kubelet

                   - name: Add hosts to /etc/hosts
                     lineinfile:
                       path: /etc/hosts
                       line: "{hostvars_private_ip_in_task} {item_in_task} {item_in_task}.{domain_in_task}"
                       state: present
                       create: no
                     loop: "{groups_all_in_task}"
                     when: hostvars[item].private_ip is defined

                   - name: Add apiserver_url to point to the masters temporary"
                     lineinfile:
                       dest: /etc/hosts
                       line: "{hostvars_groups_k8s_masters_private_ip_in_task} {apiserver_url_in_task}"
                       state: present

                   - name: Pull Kubernetes images | If you got error check your dns and sanction
                     command:
                       cmd: kubeadm config images pull
                   ```
                   2. Create k8s/tasks/main.yml and it must be as follows:"
                   ```
                   ---
                   - name: Install kubernetes packages
                     include_tasks: k8s.yml
                   ```
                   - (k8s/handlers): This path has a file called "main.yml".

                   3. Create k8s/handlers/main.yml and it must be as follows:"
                   ```
                   ---
                   # handlers file for k8s

                   - name: Remove temporary GPG key file
                     file:
                       path: "/tmp/docker.list"
                       state: absent

                   - name: Restart kubelet
                     service:
                       name: kubelet
                       state: restarted
                   ```
            - There is a directory called "roles" which a sub-directory called "init_k8s" (roles/init_k8s):
              "init_k8s" has multiple sub-directories, so let's dive deeper into each its sub-directories:
                - (init_k8s/tasks): This path has three files called "cni.yml", "initk8s.yml" and "main.yml".

                   1. Create init_k8s/tasks/cni.yml and it must be as follows:"
                   ```
                   - block:
                       - name: Check if Calico CRDs exist
                         command: kubectl get crd felixconfigurations.crd.projectcalico.org
                         register: calico_crd_check
                         ignore_errors: true
                     delegate_to: "{groups_k8s_masters_in_task}"

                   - block:
                       - name: Apply CNI plugin (Calico)
                         command: kubectl create -f {calico_operator_url_in_task}
                         retries: 3
                         delay: 3

                       - name: Apply CNI plugin (Calico)
                         command: kubectl create -f {calico_crd_url_in_task}
                         retries: 3
                         delay: 3
                     delegate_to: "{groups_k8s_masters_in_task}"
                     when: calico_crd_check.rc != 0
                     run_once: true
                   ```
                   2. Create init_k8s/tasks/initk8s.yml and it must be as follows:"
                   ```
                   - name: Init cluster | Check if kubeadm has already run
                     stat:
                       path: "/var/lib/kubelet/config.yaml"
                     register: kubeadm_already_run
                     when: inventory_hostname == groups['k8s_masters'][0]
                     delegate_to: "{groups_k8s_masters_in_task}"

                   - block:
                       - name: Init cluster | Copy kubeadmcnf.yaml
                         template:
                           src: kubeadmcnf.yml.j2
                           dest: /root/kubeadmcnf.yaml

                       - name: Init cluster | Initiate cluster on node groups['kube_master'][0]
                         shell: kubeadm init --config=/root/kubeadmcnf.yaml
                         register: kubeadm_init
                         # Retry is because upload config sometimes fails
                         until: kubeadm_init is succeeded or "field is immutable" in kubeadm_init.stderr
                         notify: Restart kubelet

                     when: inventory_hostname == groups['k8s_masters'][0] and not kubeadm_already_run.stat.exists
                     delegate_to: "{groups_k8s_masters_in_task}"

                   - block:
                       - name: Create kubectl directory
                         file:
                           path: /root/.kube
                           state: directory

                       - name: Configure kubectl
                         copy:
                           src: /etc/kubernetes/admin.conf
                           dest: /root/.kube/config
                           remote_src: yes

                       - name: Fetch kubeconfig
                         fetch:
                           src: /etc/kubernetes/admin.conf
                           dest: kubeconfig/
                           flat: yes
                     when: inventory_hostname == groups['k8s_masters'][0]
                     delegate_to: "{groups_k8s_masters_in_task}"

                   - name: Sleep for 300 seconds and reboot the Master1 server
                     wait_for:
                       timeout: 300
                     delegate_to: localhost

                   - name: Reboot the servers
                     command: reboot
                     async: 1
                     poll: 0
                     # ignore_errors: yes
                     delegate_to: "{groups_k8s_masters_in_task}"

                   - name: Sleep for 300 seconds to Master1 up and running
                     wait_for:
                       timeout: 300
                     delegate_to: localhost
                     # when: use_iran == "true"

                   - name: Example Task After Reboot
                     debug:
                       msg: "Server back online and ready for tasks."
                   ```
                   3. Create init_k8s/tasks/main.yml and it must be as follows:"
                   ```
                   ---
                   # tasks file for init_k8s

                   - name: Initialize kubernetes cluster
                     include_tasks: initk8s.yml

                   - name: Initialize Calico CNI
                     include_tasks: cni.yml
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
