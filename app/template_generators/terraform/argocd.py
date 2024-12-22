def IaC_template_generator_argocd(input) -> str:
    
    argocd = ['argocd_repository', 'argocd_application']

    argocd_create_repository = 'true' if input.argocd_repository else 'false'
    if input.argocd_application != None:
      argocd_create_application = 'true'
      argocd_application_auto_prune = 'true' if input.argocd_application.sync_policy.auto_prune else 'false'
      argocd_application_selfheal = 'true' if input.argocd_application.sync_policy.self_heal else 'false'
    else:
      argocd_create_application = 'false'
      argocd_application_auto_prune = "false"
      argocd_application_selfheal = "false"
    
   
    argocd_instance_info = """{
  server_addr = "http://argocd.local"
  username    = "username"
  password    = "password"
  insecure    = true
}
    """
    argocd_repository_info = """{
  repo     = "https://your_repo.git"
  username = "username"
  password = "token"
}
    """
    argocd_application = """{
  name                   = "myapp"
  destination_server     = "https://kubernetes.default.svc"
  destination_namespace  = "default"
  source_repo_url       = "https://your_repo.git"
  source_path           = "myapp/manifests"
  source_target_revision = "master"
}
    """
    
    tfvars_file = f"""
argocd_instance_info = {argocd_instance_info}

repository_create = {argocd_create_repository}
argocd_repository_info = {argocd_repository_info}

application_create = {argocd_create_application}
argocd_application = {argocd_application}

argocd_sync_options = ["CreateNamespace=true", "ApplyOutOfSyncOnly=true", "FailOnSharedResource=true"]

auto_prune = {argocd_application_auto_prune}
self_heal = {argocd_application_selfheal} """
    return tfvars_file