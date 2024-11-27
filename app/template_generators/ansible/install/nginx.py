

def ansible_nginx_install(input):
    
    prompt = f"""
    
        Generate a Python code to generate a Ansible project (project name is app/media/MyAnsible)
        with installs Nginx leatest version on the {input.os}.
        finally just give me a python code without any note that can generate a project folder with the given
        schema without ```python entry.(important)
        project's structure must be same as the structure which I write below:
        
            1. at location app/media/MyAnsible/install_nginx.yaml set:
                ```
                ---
                    - name: install nginx service
                    hosts:
                        - dest
                    roles:
                        - nginx
                
                ```
            
            2. create a file named app/media/MyAnsible/roles/nginx/handlers/main.yaml and put these contents on them:
                ```
                
                    ---
                       
                        - name: restart nginx
                        service:
                            name: "{{ service }}"
                            state: restarted

                        - name: restart firewall
                        service:
                            name: firewalld
                            state: restarted
                
                ```
                
            3. create a file named app/media/MyAnsible/roles/nginx/tasks/main.yaml and put these contents on them:
                ```
                
                    ---
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
                                    
                ```
                
            4. create a file named app/media/MyAnsible/roles/nginx/tasks/unzip.yaml and put these contents on them:
            
                ```
                ---
                - name: unarchive zip file
                ansible.builtin.unarchive:
                    src: /home/ansible/ninom.zip
                    dest: /home/ansible
                    remote_src: yes
                register: unzip

                - debug:
                    var: unzip
                
                
                
                ```
                
            5. create a file named app/media/MyAnsible/roles/nginx/tasks/download_webpage.yaml and put these contents on them:
            
                ```
                    ---
                    - name: download webpage
                    ansible.builtin.get_url:
                        url: "{{ url_path }}"
                        dest: /home/ansible
                        timeout: 20
                        validate_certs: no
                    register: download
                    ignore_errors: True

                    - debug:
                        var: download
                
                
                ```
                
            6. create a file named app/media/MyAnsible/roles/nginx/tasks/install_service.yaml and put these contents on them:

                ```
                   ---
                    - name: install {{ service }}
                    register: install
                    ansible.builtin.package:
                        name: "{{ item }}"
                        state: latest
                    loop:
                        - "{{ service }}"

                    - debug:
                    var: install
                
                
                ```
                
            7. create a file named app/media/MyAnsible/roles/nginx/tasks/copy_files.yaml and put these contents on them:

                ```
                   ---
                    - name: delete befor context
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
                
                
                ```
                
            8. create a file named app/media/MyAnsible/roles/nginx/var/main.yaml and put these contents on them:

                ```
                   ---
                    # vars file for nginx
                    #url_path : https://www.free-css.com/assets/files/free-css-templates/download/page261/avalon.zip
                    url_path : https://www.free-css.com/assets/files/free-css-templates/download/page283/ninom.zip
                    service: nginx
                
                
                ```
                
            9. create a file named app/media/MyAnsible/roles/nginx/meta/main.yaml and put these contents on them:

                ```
                    ---
                    allow_duplicates: yes
                    dependencies:
                    - {{ role: pre-install }}
                
                
                ```
                
            10. create a file named app/media/MyAnsible/roles/nginx/handlers/main.yaml and put these contents on them:

                ```
                    ---
                    # handlers file for nginx
                    - name: restart nginx
                    service:
                        name: "{{ service }}"
                        state: restarted

                    - name: restart firewall
                    service:
                        name: firewalld
                        state: restarted
                
                
                ```

            
            finally just give me a python code without any note that can generate a project folder with the given
              schema without ```python entry.(important) and we dont need any base directory in the python code. the final
              ansible template must work very well without any error!

              Python code you give me, must have structure like that:

              import os
              project_name = "app/media/MyAnsible"
              roles_dir = os.path.join(project_name, "roles")
              docker_container_dir = os.path.join(modules_dir, "docker_container")

              # Create project directories
              os.makedirs(docker_container_dir, exist_ok=True)

              # Create main.tf
              with open(os.path.join(project_name, "install_nginx.yaml"), "w") as main_file:
                  # any thing you need

         
              
    """
    return prompt