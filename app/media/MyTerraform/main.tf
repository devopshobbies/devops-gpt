
provider "argocd" {
  server_addr = var.argocd_instance_info["server_addr"]
  username    = var.argocd_instance_info["username"]
  password    = var.argocd_instance_info["password"]
  insecure    = var.argocd_instance_info["insecure"]
}

module "argocd" {
  source = "./modules/argocd"
  
  repository_create        = var.repository_create
  argocd_repository_info   = var.argocd_repository_info
  application_create       = var.application_create
  argocd_application       = var.argocd_application
  argocd_sync_options      = var.argocd_sync_options
}
