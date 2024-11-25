def IaC_template_generator_argocd(input) -> str:
    
    argocd = ['argocd_repository', 'argocd_application']

    argocd_create_repository = 'true' if input.argocd_repository else 'false'
    if input.argocd_application != None:
      argocd_create_application = 'true'
      argocd_application_auto_prune = 'true' if input.argocd_application.sync_policy.auto_prune else 'false'
      argocd_application_selfheal = 'true' if input.argocd_application.sync_policy.self_heal else 'false'
    else:
      argocd_create_application = 'false'
      argocd_application_auto_prune = ""
      argocd_application_selfheal = ""
    
    depends_on = 'depends_on = []'
    if input.application_depends_repository == True:
        depends_on = 'depends_on = [argocd_repository.repository]'

    prompt = f"""
              Generate a Python code to generate a Terraform project (project name is app/media/MyTerraform)
              that dynamically provisions {argocd} resources ensuring a modular, flexible structure to enable users
              to configure all essential settings at the root level. Only provide Python code, no explanations or
              markdown formatting. The project should be organized as follows:
              1. Root Directory Structure:
                  - main.tf:
                      - Define the provider block as follows:
                            ```
                            provider "argocd" {{
                              server_addr = var.argocd_instance_info["server_addr"]
                              username    = var.argocd_instance_info["username"]
                              password    = var.argocd_instance_info["password"]
                              insecure    = var.argocd_instance_info["insecure "]
                            }}
                            ```
                      - Defines a module block that references "argocd" from a subdirectory within modules.
                        This module block should expose all variables that {argocd} resources require, allowing
                        configuration at the root level rather than directly within the module.
                      - Every variable defined in {argocd} resources should be passed through the module block,
                        ensuring that users can adjust all critical parameters of {argocd} resources by modifying
                        root main.tf. Avoid using any other parameters. just use the parameters of {argocd} resources with the same keys
                  - variables.tf:
                      - Sets this variable name for argocd provider:
                          argocd_instance_info(object()) as follows:
                              ```
                              type         = object({{
                              server_addr  = string
                              username     = string
                              password     = string
                              insecure     = bool
                             }})
                              ```
                      - Sets these variables names for argocd_repository resource:
                          repository_create(bool), argocd_repository_info(map(string))
                      - Sets these variables names for argocd_application resource:
                          application_create(bool), argocd_application(map(string)), argocd_sync_options(list(string))
                  - terraform.tfvars:
                      - Structure as follows:
                          argocd_instance_info = {{
                            server_addr = "ARGOCD_DOMAIN"
                            username = "admin"
                            password = "ARGOCD_ADMIN_PASS"
                            insecure = true
                          }}

                          repository_create = {argocd_create_repository}
                          argocd_repository_info = {{
                            repo  = "https://YOUR_REPO.git"
                            username = "USERNAME"
                            password = "CHANGE_ME_WITH_TOKEN"
                          }}

                          application_create = {argocd_create_application}
                          argocd_application = {{
                            name = "APPLICATION_NAME"
                            destination_server = "https://kubernetes.default.svc"
                            destination_namespace = "DESTINATION_NAMESPACE"
                            source_repo_url = "https://YOUR_REPO.git"
                            source_path = "SOURCE_PATH"
                            source_target_revision = "SOURCE_TARGET_REVISION"
                          }}

                          argocd_sync_options = ["CreateNamespace=true", "ApplyOutOfSyncOnly=true", "FailOnSharedResource=true"]
                  - versions.tf:
                      - Structure as follows:
                            terraform {{
                              required_version = ">= 1.0"

                              required_providers {{
                                argocd = {{
                                  source  = "oboukili/argocd"
                                  version = ">= 6.0.2"
                               }}
                              }}
                            }}
              2. Module Directory Structure (modules/argocd):
                  - main.tf:
                      - Set the following parameters for argocd_repository resource (name its terraform resource to "repository") and avoid using any other parameters:
                           - 1. count (type: number): follow the below syntax for count:
                               ```
                               count = var.repository_create ? 1 : 0
                               ```
                           - 2. repo (type: string): follow the below syntax for repo parameter:
                               ```
                               repo  = var.argocd_repository_info["repo"]
                               ```
                           - 3. username (type: string): follow the below syntax for username parameter:
                               ```
                               username  = var.argocd_repository_info["username"]
                               ```
                           - 4. password (type: string): follow the below syntax for password parameter:
                               ```
                               password  = var.argocd_repository_info["password"]
                               ```
                      - Set the following parameters for argocd_application resource (name its terraform resource to "application") and avoid using any other parameters:
                           - 1. count (type: number): follow the below syntax for count:
                               ```
                               count = var.application_create ? 1 : 0
                               ```
                           - 2. add depends_on block following :
                                ```
                                {depends_on}
                                
                                ```
                                
                           - 3. metadata (A block): Define a metadata block as follows:
                               ```
                               metadata {{
                                 name      = var.argocd_application["name"]
                                 namespace = argocd
                                 labels = {{
                                   using_sync_policy_options = "true"
                                 }}
                               }}
                               ```
                           - 4. spec (A block): Define a spec block as follows:
                               ```
                               spec {{
                                 destination {{
                                   server    = var.argocd_application["destination_server"]
                                   namespace = var.argocd_application["destination_namespace"]
                                 }}
                                 source {{
                                   repo_url = var.argocd_application["source_repo_url"]
                                   path  = var.argocd_application["source_path"]
                                   target_revision = var.argocd_application["source_target_revision"]
                                 }}
                                 sync_policy {{
                                   automated {{
                                   prune     = {argocd_application_auto_prune}
                                   self_heal = {argocd_application_selfheal}
                                   }}
                                   sync_options = var.argocd_sync_options
                                 }}
                               }}
                               ```
                  - variables.tf:
                      - Sets these variables names for argocd_repository resource:
                          repository_create(bool), argocd_repository_info(map(string))
                      - Sets these variables names for argocd_application resource:
                          application_create(bool), argocd_application(map(string)), argocd_sync_options(list(string))
                  - terraform.tfvars:
                      - Structure as follows:
                          repository_create = {argocd_create_repository}
                          argocd_repository_info = {{
                            repo  = "https://YOUR_REPO.git"
                            username = "USERNAME"
                            password = "CHANGE_ME_WITH_TOKEN"
                          }}

                          application_create = {argocd_create_application}
                          argocd_application = {{
                            name = "APPLICATION_NAME"
                            destination_server = "https://kubernetes.default.svc"
                            destination_namespace = "DESTINATION_NAMESPACE"
                            source_repo_url = "https://YOUR_REPO.git"
                            source_path = "SOURCE_PATH"
                            source_target_revision = "SOURCE_TARGET_REVISION"
                          }}

                          argocd_sync_options = ["CreateNamespace=true", "ApplyOutOfSyncOnly=true", "FailOnSharedResource=true"]
                  - versions.tf:
                      - Structure as follows:
                            terraform {{
                              required_version = ">= 1.0"

                              required_providers {{
                                argocd = {{
                                  source  = "oboukili/argocd"
                                  version = ">= 6.0.2"
                               }}
                              }}
                            }}
              Ensure this project structure supports {argocd}’s configurability, extensibility, and
              reusability across diverse Terraform providers, empowering users to manage their resources through a
              single, customizable root configuration while keeping module internals robustly modular.

              finally just give me a python code without any note that can generate a project folder with the given
              schema without ```python entry. and we dont need any base directory in the python code. the final
              terraform template must work very well without any error!

              Python code you give me, must have structure like that:

              import os
              project_name = "app/media/MyTerraform"
              modules_dir = os.path.join(project_name, "modules")
              argocd_dir = os.path.join(modules_dir, "argocd")

              # Create project directories
              os.makedirs(argocd_dir, exist_ok=True)

              # Create main.tf
              with open(os.path.join(project_name, "main.tf"), "w") as main_file:
                  # any thing you need

            """
    return prompt
