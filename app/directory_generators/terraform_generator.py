import os
project_name = "app/media/MyTerraform"
modules_dir = os.path.join(project_name, "modules")
argocd_dir = os.path.join(modules_dir, "argocd")

# Create project directories
os.makedirs(argocd_dir, exist_ok=True)

# Create main.tf
with open(os.path.join(project_name, "main.tf"), "w") as main_file:
    main_file.write('''
provider "argocd" {
  server_addr = var.argocd_instance_info["server_addr"]
  username    = var.argocd_instance_info["username"]
  password    = var.argocd_instance_info["password"]
  insecure    = var.argocd_instance_info["insecure"]
}

module "argocd" {
  source = "./modules/argocd"
  
  repository_create      = var.repository_create
  argocd_repository_info  = var.argocd_repository_info
  application_create      = var.application_create
  argocd_application      = var.argocd_application
  argocd_sync_options     = var.argocd_sync_options
}
''')

# Create variables.tf
with open(os.path.join(project_name, "variables.tf"), "w") as vars_file:
    vars_file.write('''
variable "argocd_instance_info" {
  type = object({
    server_addr = string
    username    = string
    password    = string
    insecure    = bool
  })
}

variable "repository_create" {
  type = bool
}

variable "argocd_repository_info" {
  type = map(string)
}

variable "application_create" {
  type = bool
}

variable "argocd_application" {
  type = map(string)
}

variable "argocd_sync_options" {
  type = list(string)
}
''')

# Create terraform.tfvars
with open(os.path.join(project_name, "terraform.tfvars"), "w") as tfvars_file:
    tfvars_file.write('''
argocd_instance_info = {
  server_addr = "ARGOCD_DOMAIN"
  username    = "admin"
  password    = "ARGOCD_ADMIN_PASS"
  insecure    = true
}

repository_create = false
argocd_repository_info = {
  repo     = "https://YOUR_REPO.git"
  username = "USERNAME"
  password = "CHANGE_ME_WITH_TOKEN"
}

application_create = true
argocd_application = {
  name                   = "APPLICATION_NAME"
  destination_server     = "https://kubernetes.default.svc"
  destination_namespace  = "DESTINATION_NAMESPACE"
  source_repo_url       = "https://YOUR_REPO.git"
  source_path           = "SOURCE_PATH"
  source_target_revision = "SOURCE_TARGET_REVISION"
}

argocd_sync_options = ["CreateNamespace=true", "ApplyOutOfSyncOnly=true", "FailOnSharedResource=true"]
''')

# Create versions.tf
with open(os.path.join(project_name, "versions.tf"), "w") as versions_file:
    versions_file.write('''
terraform {
  required_version = ">= 1.0"

  required_providers {
    argocd = {
      source  = "oboukili/argocd"
      version = ">= 6.0.2"
    }
  }
}
''')

# Create module main.tf
with open(os.path.join(argocd_dir, "main.tf"), "w") as module_main_file:
    module_main_file.write('''
resource "argocd_repository" "repository" {
  count    = var.repository_create ? 1 : 0
  repo     = var.argocd_repository_info["repo"]
  username = var.argocd_repository_info["username"]
  password = var.argocd_repository_info["password"]
}

resource "argocd_application" "application" {
  count = var.application_create ? 1 : 0
  depends_on = [argocd_repository.repository]

  metadata {
    name      = var.argocd_application["name"]
    namespace = "argocd"
    labels = {
      using_sync_policy_options = "true"
    }
  }

  spec {
    destination {
      server    = var.argocd_application["destination_server"]
      namespace = var.argocd_application["destination_namespace"]
    }
    source {
      repo_url        = var.argocd_application["source_repo_url"]
      path            = var.argocd_application["source_path"]
      target_revision = var.argocd_application["source_target_revision"]
    }
    sync_policy {
      automated {
        prune     = false
        self_heal = false
      }
      sync_options = var.argocd_sync_options
    }
  }
}
''')

# Create module variables.tf
with open(os.path.join(argocd_dir, "variables.tf"), "w") as module_vars_file:
    module_vars_file.write('''
variable "repository_create" {
  type = bool
}

variable "argocd_repository_info" {
  type = map(string)
}

variable "application_create" {
  type = bool
}

variable "argocd_application" {
  type = map(string)
}

variable "argocd_sync_options" {
  type = list(string)
}
''')

# Create module terraform.tfvars
with open(os.path.join(argocd_dir, "terraform.tfvars"), "w") as module_tfvars_file:
    module_tfvars_file.write('''
repository_create = false
argocd_repository_info = {
  repo     = "https://YOUR_REPO.git"
  username = "USERNAME"
  password = "CHANGE_ME_WITH_TOKEN"
}

application_create = true
argocd_application = {
  name                   = "APPLICATION_NAME"
  destination_server     = "https://kubernetes.default.svc"
  destination_namespace  = "DESTINATION_NAMESPACE"
  source_repo_url       = "https://YOUR_REPO.git"
  source_path           = "SOURCE_PATH"
  source_target_revision = "SOURCE_TARGET_REVISION"
}

argocd_sync_options = ["CreateNamespace=true", "ApplyOutOfSyncOnly=true", "FailOnSharedResource=true"]
''')

# Create module versions.tf
with open(os.path.join(argocd_dir, "versions.tf"), "w") as module_versions_file:
    module_versions_file.write('''
terraform {
  required_version = ">= 1.0"

  required_providers {
    argocd = {
      source  = "oboukili/argocd"
      version = ">= 6.0.2"
    }
  }
}
''')