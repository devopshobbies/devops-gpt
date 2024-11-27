import os

project_name = "app/media/MyAnsible"
roles_dir = os.path.join(project_name, "roles")
nginx_dir = os.path.join(roles_dir, "nginx")
tasks_dir = os.path.join(nginx_dir, "tasks")
handlers_dir = os.path.join(nginx_dir, "handlers")
var_dir = os.path.join(nginx_dir, "var")
meta_dir = os.path.join(nginx_dir, "meta")

# Create project directories
os.makedirs(nginx_dir, exist_ok=True)
os.makedirs(tasks_dir, exist_ok=True)
os.makedirs(handlers_dir, exist_ok=True)
os.makedirs(var_dir, exist_ok=True)
os.makedirs(meta_dir, exist_ok=True)

# Create install_nginx.yaml
with open(os.path.join(project_name, "install_nginx.yaml"), "w") as main_file:
    main_file.write('''---
- name: install nginx service
  hosts:
    - dest
  roles:
    - nginx
''')

# Create handlers/main.yaml
with open(os.path.join(handlers_dir, "main.yaml"), "w") as handlers_file:
    handlers_file.write('''---
- name: restart nginx
  service:
    name: "{ service }"
    state: restarted

- name: restart firewall
  service:
    name: firewalld
    state: restarted
''')

# Create tasks/main.yaml
with open(os.path.join(tasks_dir, "main.yaml"), "w") as tasks_file:
    tasks_file.write('''---
# tasks file for nginx
- name: download page
  include: download_webpage.yml

- name: unzip
  include: unzip.yml

- name: install service
  include: install_service.yml

- name: open website port https
  firewalld:
    service: https
    permanent: yes
    state: enabled
  notify:
    - restart firewall

- name: open website port http
  firewalld:
    zone: public
    service: http
    permanent: yes
    state: enabled
  notify:
    - restart firewall

- name: webpage
  include: copy_files.yml
''')

# Create tasks/unzip.yaml
with open(os.path.join(tasks_dir, "unzip.yaml"), "w") as unzip_file:
    unzip_file.write('''---
- name: unarchive zip file
  ansible.builtin.unarchive:
    src: /home/ansible/ninom.zip
    dest: /home/ansible
    remote_src: yes
  register: unzip

- debug:
    var: unzip
''')

# Create tasks/download_webpage.yaml
with open(os.path.join(tasks_dir, "download_webpage.yaml"), "w") as download_file:
    download_file.write('''---
- name: download webpage
  ansible.builtin.get_url:
    url: "{ url_path }"
    dest: /home/ansible
    timeout: 20
    validate_certs: no
  register: download
  ignore_errors: True

- debug:
    var: download
''')

# Create tasks/install_service.yaml
with open(os.path.join(tasks_dir, "install_service.yaml"), "w") as install_file:
    install_file.write('''---
- name: install { service }
  register: install
  ansible.builtin.package:
    name: "{ item }"
    state: latest
  loop:
    - "{ service }"

- debug:
    var: install
''')

# Create tasks/copy_files.yaml
with open(os.path.join(tasks_dir, "copy_files.yaml"), "w") as copy_file:
    copy_file.write('''---
- name: delete before context
  shell: "rm -rf /usr/share/nginx/html/*"
  register: delete

- debug:
    var: delete

- name: copy html file on the html main dir
  register: copy_file
  copy:
    src: /home/ansible/ninom-html/
    dest: /usr/share/nginx/html/
    remote_src: yes
    directory_mode: yes
  notify:
    - restart nginx

- debug:
    var: copy_file
''')

# Create var/main.yaml
with open(os.path.join(var_dir, "main.yaml"), "w") as var_file:
    var_file.write('''---
# vars file for nginx
#url_path : https://www.free-css.com/assets/files/free-css-templates/download/page261/avalon.zip
url_path : https://www.free-css.com/assets/files/free-css-templates/download/page283/ninom.zip
service: nginx
''')

# Create meta/main.yaml
with open(os.path.join(meta_dir, "main.yaml"), "w") as meta_file:
    meta_file.write('''---
allow_duplicates: yes
dependencies:
  - { role: pre-install }
''')