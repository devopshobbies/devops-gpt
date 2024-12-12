import os
def ansible_kuber_install(input):
  
    kubernetes_ansible_port = input.ansible_port
    kubernetes_ansible_user = input.ansible_user
    k8s_master_nodes = input.k8s_master_nodes
    k8s_worker_nodes = input.k8s_worker_nodes
    k8s_version = input.version
    sections = {
      "[all]": [f"{name} private_ip=x.x.x.x" for name in k8s_master_nodes + k8s_worker_nodes],
      "[k8s]": k8s_master_nodes + k8s_worker_nodes,
      "[k8s_masters]": k8s_master_nodes,
      "[k8s_workers]": k8s_worker_nodes,
    }
    kubernetes_inventory = "\n\n".join(f"{section}\n" + "\n".join(entries) for section, entries in sections.items())



    project_name = "app/media/MyAnsible"
    ansible_dir = project_name
    group_vars_dir = os.path.join(ansible_dir, "group_vars")
    host_vars_dir = os.path.join(ansible_dir, "host_vars")
    roles_dir = os.path.join(ansible_dir, "roles")

    # Create project directories
    os.makedirs(group_vars_dir, exist_ok=True)
    os.makedirs(host_vars_dir, exist_ok=True)
    os.makedirs(roles_dir, exist_ok=True)

    preinstall_dir = os.path.join(roles_dir, "preinstall")
    k8s_dir = os.path.join(roles_dir, "k8s")
    init_k8s_dir = os.path.join(roles_dir, "init_k8s")
    join_master_dir = os.path.join(roles_dir, "join_master")
    join_worker_dir = os.path.join(roles_dir, "join_worker")

    os.makedirs(preinstall_dir, exist_ok=True)
    os.makedirs(k8s_dir, exist_ok=True)
    os.makedirs(init_k8s_dir, exist_ok=True)
    os.makedirs(join_master_dir, exist_ok=True)
    os.makedirs(join_worker_dir, exist_ok=True)

    # Create ansible.cfg
    with open(os.path.join(ansible_dir, "ansible.cfg"), "w") as ansible_cfg_file:
        ansible_cfg_file.write("[defaults]\nhost_key_checking=false\n")

    # Create group_vars/all
    with open(os.path.join(group_vars_dir, "all"), "w") as group_vars_file:
        group_vars_file.write(f"""# General
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
    kubernetes_gpg_key_url: "https://pkgs.k8s.io/core:/stable:/v1.31/deb/Release.key"
    kubernetes_apt_repo: "https://pkgs.k8s.io/core:/stable:/v1.31/deb/"
    k8s_version: {k8s_version} # see here https://kubernetes.io/releases/patch-releases/ and https://github.com/kubernetes/kubernetes/releases

    # CRI
    cri_socket: unix:///var/run/containerd/containerd.sock

    # Ansible Connection
    ansible_user: {kubernetes_ansible_user}
    ansible_port: {kubernetes_ansible_port}
    ansible_python_interpreter: "/usr/bin/python3"
    domain: "devopsgpt.com"
    apiserver_url: "devopsgpt.com"
    """)

    # Create hosts
    with open(os.path.join(ansible_dir, "hosts"), "w") as hosts_file:
        hosts_file.write(f"""{kubernetes_inventory}""")

    # Create kubernetes_playbook.yml
    with open(os.path.join(ansible_dir, "kubernetes_playbook.yml"), "w") as playbook_file:
        playbook_file.write("""- hosts: all
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

    - hosts: k8s_masters
      roles:
        - role: preinstall
        - role: k8s
        - role: join_master
      gather_facts: yes
      any_errors_fatal: true
      tags: [join_master]

    - hosts: k8s_workers
      roles:
        - role: preinstall
        - role: k8s
        - role: join_worker
      gather_facts: yes
      any_errors_fatal: true
      tags: [join_worker]
    """)

    # Create preinstall files
    preinstall_defaults_dir = os.path.join(preinstall_dir, "defaults")
    preinstall_files_dir = os.path.join(preinstall_dir, "files")
    preinstall_handlers_dir = os.path.join(preinstall_dir, "handlers")
    preinstall_tasks_dir = os.path.join(preinstall_dir, "tasks")
    preinstall_templates_dir = os.path.join(preinstall_dir, "templates")
    preinstall_vars_dir = os.path.join(preinstall_dir, "vars")

    os.makedirs(preinstall_defaults_dir, exist_ok=True)
    os.makedirs(preinstall_files_dir, exist_ok=True)
    os.makedirs(preinstall_handlers_dir, exist_ok=True)
    os.makedirs(preinstall_tasks_dir, exist_ok=True)
    os.makedirs(preinstall_templates_dir, exist_ok=True)
    os.makedirs(preinstall_vars_dir, exist_ok=True)

    with open(os.path.join(preinstall_defaults_dir, "main.yml"), "w") as defaults_file:
        defaults_file.write("")

    with open(os.path.join(preinstall_files_dir, "sample.sh"), "w") as files_file:
        files_file.write("")

    with open(os.path.join(preinstall_handlers_dir, "main.yml"), "w") as handlers_file:
        handlers_file.write("")

    with open(os.path.join(preinstall_tasks_dir, "basic.yml"), "w") as basic_tasks_file:
        basic_tasks_file.write("""- name: Set timezone to UTC
      timezone:
        name: Etc/UTC

    - name: Set hostname
      command: hostnamectl set-hostname {{ inventory_hostname }}

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
        regexp: '^127\\.0\\.0\\.1'
        line: "127.0.0.1 {{ inventory_hostname }} localhost"
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
    """)

    with open(os.path.join(preinstall_tasks_dir, "main.yml"), "w") as tasks_main_file:
        tasks_main_file.write("""---
    - name: basic setup
      include_tasks: basic.yml
    """)

    # Create k8s files
    k8s_defaults_dir = os.path.join(k8s_dir, "defaults")
    k8s_files_dir = os.path.join(k8s_dir, "files")
    k8s_handlers_dir = os.path.join(k8s_dir, "handlers")
    k8s_tasks_dir = os.path.join(k8s_dir, "tasks")
    k8s_templates_dir = os.path.join(k8s_dir, "templates")
    k8s_vars_dir = os.path.join(k8s_dir, "vars")

    os.makedirs(k8s_defaults_dir, exist_ok=True)
    os.makedirs(k8s_files_dir, exist_ok=True)
    os.makedirs(k8s_handlers_dir, exist_ok=True)
    os.makedirs(k8s_tasks_dir, exist_ok=True)
    os.makedirs(k8s_templates_dir, exist_ok=True)
    os.makedirs(k8s_vars_dir, exist_ok=True)

    with open(os.path.join(k8s_defaults_dir, "main.yml"), "w") as k8s_defaults_file:
        k8s_defaults_file.write("")

    with open(os.path.join(k8s_files_dir, "sample.sh"), "w") as k8s_files_file:
        k8s_files_file.write("")

    with open(os.path.join(k8s_handlers_dir, "main.yml"), "w") as k8s_handlers_file:
        k8s_handlers_file.write("""---
    # handlers file for k8s

    - name: Remove temporary GPG key file
      file:
        path: "/tmp/docker.list"
        state: absent

    - name: Restart kubelet
      service:
        name: kubelet
        state: restarted
    """)

    with open(os.path.join(k8s_tasks_dir, "k8s.yml"), "w") as k8s_tasks_k8s_file:
        k8s_tasks_k8s_file.write("""- name: Disable SWAP since kubernetes can't work with swap enabled
      shell: |
        swapoff -a

    - name: Disable SWAP in fstab since kubernetes can't work with swap enabled
      replace:
        path: /etc/fstab
        regexp: '^([^#].*?\\sswap\\s+sw\\s+.*)$'
        replace: '# \\1'

    - name: Check if ufw is installed
      package_facts:
        manager: "auto"

    - name: Disable ufw # just in Ubuntu
      ufw:
        state: disabled
      when: "'ufw' in ansible_facts.packages"

    - name: Ensure kernel modules for containerd are enabled
      lineinfile:
        path: /etc/modules-load.d/containerd.conf
        line: "{{ item }}"
        create: yes
        state: present
      loop:
        - overlay
        - br_netfilter

    - name: Load kernel modules
      command:
        cmd: "modprobe {{ item }}"
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
        marker: "# {mark} ANSIBLE MANAGED BLOCK"
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
        path: '{{ docker_gpg_key_path }}'
        state: absent

    - name: Download Docker GPG key
      shell: |
        curl -fsSL {{ docker_gpg_key_url }} | gpg --dearmor -o {{ docker_gpg_key_path }}

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
        line: "deb [arch={{ architecture.stdout }} signed-by={{ docker_gpg_key_path }}] {{ docker_apt_repo }} {{ distribution_codename.stdout }} stable"
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
        path: '{{ kubernetes_gpg_keyring_path }}'
        state: absent

    - name: Download Kubernetes GPG key
      shell: |
        curl -fsSL '{{ kubernetes_gpg_key_url }}' | gpg --dearmor -o '{{ kubernetes_gpg_keyring_path }}'

    - name: Add Kubernetes repo
      apt_repository:
        repo: "deb [signed-by={{ kubernetes_gpg_keyring_path }}] {{ kubernetes_apt_repo }} /"
        state: present
        filename: kubernetes.list

    - name: Update apt cache
      apt:
        update_cache: yes

    - name: Install Kubernetes packages
      apt:
        name: "{{ item }}"
        state: present
      loop:
        - kubeadm=1.31.2-1.1
        - kubelet=1.31.2-1.1
        - kubectl=1.31.2-1.1

    - name: Hold Kubernetes packages
      dpkg_selections:
        name: "{{ item }}"
        selection: hold
      loop:
        - kubeadm
        - kubelet
        - kubectl
        - containerd.io

    - name: Configure node ip
      lineinfile:
        path: /etc/default/kubelet
        line: KUBELET_EXTRA_ARGS=--node-ip={{ private_ip }}
        create: yes
        state: present
      notify: Restart kubelet

    - name: Add hosts to /etc/hosts
      lineinfile:
        path: /etc/hosts
        line: "{{ hostvars[item].private_ip }} {{ item }} {{ item }}.{{ domain }}"
        state: present
        create: no
      loop: "{{ groups['all'] }}"
      when: hostvars[item].private_ip is defined

    - name: Add apiserver_url to point to the masters temporary
      lineinfile:
        dest: /etc/hosts
        line: "{{ hostvars[groups['k8s_masters'][0]].private_ip }} {{ apiserver_url }}"
        state: present

    - name: Pull Kubernetes images | If you got error check your dns and sanction
      command:
        cmd: kubeadm config images pull
    """)

    with open(os.path.join(k8s_tasks_dir, "main.yml"), "w") as k8s_tasks_main_file:
        k8s_tasks_main_file.write("""---
    - name: Install kubernetes packages
      include_tasks: k8s.yml
    """)

    # Create init_k8s files
    init_k8s_defaults_dir = os.path.join(init_k8s_dir, "defaults")
    init_k8s_files_dir = os.path.join(init_k8s_dir, "files")
    init_k8s_handlers_dir = os.path.join(init_k8s_dir, "handlers")
    init_k8s_tasks_dir = os.path.join(init_k8s_dir, "tasks")
    init_k8s_templates_dir = os.path.join(init_k8s_dir, "templates")
    init_k8s_vars_dir = os.path.join(init_k8s_dir, "vars")

    os.makedirs(init_k8s_defaults_dir, exist_ok=True)
    os.makedirs(init_k8s_files_dir, exist_ok=True)
    os.makedirs(init_k8s_handlers_dir, exist_ok=True)
    os.makedirs(init_k8s_tasks_dir, exist_ok=True)
    os.makedirs(init_k8s_templates_dir, exist_ok=True)
    os.makedirs(init_k8s_vars_dir, exist_ok=True)

    with open(os.path.join(init_k8s_defaults_dir, "main.yml"), "w") as init_k8s_defaults_file:
        init_k8s_defaults_file.write("")

    with open(os.path.join(init_k8s_files_dir, "sample.sh"), "w") as init_k8s_files_file:
        init_k8s_files_file.write("")

    with open(os.path.join(init_k8s_handlers_dir, "main.yml"), "w") as init_k8s_handlers_file:
        init_k8s_handlers_file.write("")

    with open(os.path.join(init_k8s_tasks_dir, "cni.yml"), "w") as init_k8s_tasks_cni_file:
        init_k8s_tasks_cni_file.write("""- block:
        - name: Check if Calico CRDs exist
          command: kubectl get crd felixconfigurations.crd.projectcalico.org
          register: calico_crd_check
          ignore_errors: true
      delegate_to: "{{ groups['k8s_masters'][0] }}"

    - block:
        - name: Apply CNI plugin (Calico)
          command: kubectl create -f {{ calico_operator_url }}
          retries: 3
          delay: 3

        - name: Apply CNI plugin (Calico)
          command: kubectl create -f {{ calico_crd_url }}
          retries: 3
          delay: 3
      delegate_to: "{{ groups['k8s_masters'][0] }}"
      when: calico_crd_check.rc != 0
      run_once: true
    """)

    with open(os.path.join(init_k8s_tasks_dir, "initk8s.yml"), "w") as init_k8s_tasks_initk8s_file:
        init_k8s_tasks_initk8s_file.write("""- name: Init cluster | Check if kubeadm has already run
      stat:
        path: "/var/lib/kubelet/config.yaml"
      register: kubeadm_already_run
      when: inventory_hostname == groups['k8s_masters'][0]
      delegate_to: "{{ groups['k8s_masters'][0] }}"

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
      delegate_to: "{{ groups['k8s_masters'][0] }}"

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
      delegate_to: "{{ groups['k8s_masters'][0] }}"

    - name: Sleep for 300 seconds and reboot the Master1 server
      wait_for:
        timeout: 300
      delegate_to: localhost

    - name: Reboot the servers
      command: reboot
      async: 1
      poll: 0
      # ignore_errors: yes
      delegate_to: "{{ groups['k8s_masters'][0] }}"

    - name: Sleep for 300 seconds to Master1 up and running
      wait_for:
        timeout: 300
      delegate_to: localhost
      # when: use_iran == "true"

    - name: Example Task After Reboot
      debug:
        msg: "Server back online and ready for tasks."
    """)

    with open(os.path.join(init_k8s_tasks_dir, "main.yml"), "w") as init_k8s_tasks_main_file:
        init_k8s_tasks_main_file.write("""---
    # tasks file for init_k8s

    - name: Initialize kubernetes cluster
      include_tasks: initk8s.yml

    - name: Initialize Calico CNI
      include_tasks: cni.yml
    """)

    # Create join_master files
    join_master_defaults_dir = os.path.join(join_master_dir, "defaults")
    join_master_files_dir = os.path.join(join_master_dir, "files")
    join_master_handlers_dir = os.path.join(join_master_dir, "handlers")
    join_master_tasks_dir = os.path.join(join_master_dir, "tasks")
    join_master_templates_dir = os.path.join(join_master_dir, "templates")
    join_master_vars_dir = os.path.join(join_master_dir, "vars")

    os.makedirs(join_master_defaults_dir, exist_ok=True)
    os.makedirs(join_master_files_dir, exist_ok=True)
    os.makedirs(join_master_handlers_dir, exist_ok=True)
    os.makedirs(join_master_tasks_dir, exist_ok=True)
    os.makedirs(join_master_templates_dir, exist_ok=True)
    os.makedirs(join_master_vars_dir, exist_ok=True)

    with open(os.path.join(join_master_defaults_dir, "main.yml"), "w") as join_master_defaults_file:
        join_master_defaults_file.write("")

    with open(os.path.join(join_master_files_dir, "join-command"), "w") as join_master_files_file:
        join_master_files_file.write("")

    with open(os.path.join(join_master_handlers_dir, "main.yml"), "w") as join_master_handlers_file:
        join_master_handlers_file.write("")

    with open(os.path.join(join_master_tasks_dir, "join_master.yml"), "w") as join_master_tasks_join_master_file:
        join_master_tasks_join_master_file.write("""- name: Init cluster | Check if kubeadm has already run
      stat:
        path: "/var/lib/kubelet/config.yaml"
      register: kubeadm_already_run

    - block:
        - name: Generate join command
          command: kubeadm token create --print-join-command
          register: join_command

        - name: Print join command
          debug:
            msg: "{{ join_command.stdout_lines[0] }}"

        - name: Copy join command to local file
          become: false
          local_action: copy content="{{ join_command.stdout_lines[0] }} $@" dest="roles/join_master/files/join-command"

        - name: copy kubeadmcnf.yaml
          template:
            src: kubeadmcnf-join.yml.j2
            dest: /root/kubeadm-config.yaml

      when:
        - inventory_hostname == groups['k8s_masters'][0]
      delegate_to: "{{ groups['k8s_masters'][0] }}"

    - block:
        - name: Copy the join command to server location
          copy:
            src: roles/join_master/files/join-command
            dest: /root/join-command.sh
            mode: "0777"

      when:
        - inventory_hostname != groups['k8s_masters'][0]
        - inventory_hostname in groups['k8s_masters']
        - not kubeadm_already_run.stat.exists

    - block:
        - name: get certificate key
          shell: kubeadm init phase upload-certs --upload-certs --config=/root/kubeadm-config.yaml
          register: kubeadm_cert_key

        - name: Print certificate key
          debug:
            msg: "{{ kubeadm_cert_key.stdout_lines[2] }}"

        - name: register the cert key
          set_fact:
            control_plane_certkey: "{{ kubeadm_cert_key.stdout_lines[2] }}"

      when:
        - inventory_hostname  in groups['k8s_masters'][0]
      delegate_to: "{{ groups['k8s_masters'][0] }}"
      run_once: false
      delegate_facts: true

    - name: Join | Join control-plane to cluster
      command: "sh /root/join-command.sh --control-plane --certificate-key={{ hostvars[groups['k8s_masters'][0]].control_plane_certkey }}  --cri-socket={{ cri_socket }}"
      when:
        - inventory_hostname != groups['k8s_masters'][0]
        - inventory_hostname in groups['k8s_masters']
        - not kubeadm_already_run.stat.exists

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
      when:
        - inventory_hostname != groups['k8s_masters'][0]
        - inventory_hostname in groups['k8s_masters']
        - not kubeadm_already_run.stat.exists

    - name: remove apiserver_url to point to the masters temporary
      lineinfile:
        dest: /etc/hosts
        line: "{{ hostvars[groups['k8s_masters'][0]].private_ip }} {{ apiserver_url }}"
        state: absent

    - name: Add apiserver_url to point to the masters
      lineinfile:
        dest: /etc/hosts
        line: "{{ private_ip }} {{ apiserver_url }}"
        state: present
      when:
        - inventory_hostname in groups['k8s_masters']
    """)

    with open(os.path.join(join_master_tasks_dir, "main.yml"), "w") as join_master_tasks_main_file:
        join_master_tasks_main_file.write("""---
    # tasks file for join_master

    - name: Join master(s) node to cluster
      include_tasks: join_master.yml
    """)

    # Create join_worker files
    join_worker_defaults_dir = os.path.join(join_worker_dir, "defaults")
    join_worker_files_dir = os.path.join(join_worker_dir, "files")
    join_worker_handlers_dir = os.path.join(join_worker_dir, "handlers")
    join_worker_tasks_dir = os.path.join(join_worker_dir, "tasks")
    join_worker_templates_dir = os.path.join(join_worker_dir, "templates")
    join_worker_vars_dir = os.path.join(join_worker_dir, "vars")

    os.makedirs(join_worker_defaults_dir, exist_ok=True)
    os.makedirs(join_worker_files_dir, exist_ok=True)
    os.makedirs(join_worker_handlers_dir, exist_ok=True)
    os.makedirs(join_worker_tasks_dir, exist_ok=True)
    os.makedirs(join_worker_templates_dir, exist_ok=True)
    os.makedirs(join_worker_vars_dir, exist_ok=True)

    with open(os.path.join(join_worker_defaults_dir, "main.yml"), "w") as join_worker_defaults_file:
        join_worker_defaults_file.write("")

    with open(os.path.join(join_worker_files_dir, "join-command"), "w") as join_worker_files_file:
        join_worker_files_file.write("")

    with open(os.path.join(join_worker_handlers_dir, "main.yml"), "w") as join_worker_handlers_file:
        join_worker_handlers_file.write("")

    with open(os.path.join(join_worker_tasks_dir, "join_worker.yml"), "w") as join_worker_tasks_join_worker_file:
        join_worker_tasks_join_worker_file.write("""- name: Init cluster | Check if kubeadm has already run
      stat:
        path: "/var/lib/kubelet/config.yaml"
      register: kubeadm_already_run

    - block:
        - name: Generate join command
          command: kubeadm token create --print-join-command
          register: join_command

        - name: Print join command
          debug:
            msg: "{{ join_command.stdout_lines[0] }}"

        - name: Copy join command to local file
          become: false
          local_action: copy content="{{ join_command.stdout_lines[0] }} $@" dest="roles/join_worker/files/join-command"

      when:
        - inventory_hostname not in groups['k8s_masters'][0]
      delegate_to: "{{ groups['k8s_masters'][0] }}"

    - block:
        - name: Copy the join command to server location
          copy:
            src: roles/join_worker/files/join-command
            dest: /root/join-command.sh
            mode: "0777"

      when:
        - inventory_hostname not in groups['k8s_masters']
        - not kubeadm_already_run.stat.exists

    - name: Join | Join worker nodes to the cluster
      command: sh /root/join-command.sh
      when:
        - inventory_hostname not in groups['k8s_masters']
        - not kubeadm_already_run.stat.exists
    """)

    with open(os.path.join(join_worker_tasks_dir, "main.yml"), "w") as join_worker_tasks_main_file:
        join_worker_tasks_main_file.write("""---
    # tasks file for join_worker

    - name: Join worker(s) node to cluster
      include_tasks: join_worker.yml
    """)