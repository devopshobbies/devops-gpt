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

    tfvars_file = """
argocd_instance_info = {
  server_addr = "ARGOCD_DOMAIN"
  username    = "admin"
  password    = "ARGOCD_ADMIN_PASS"
  insecure    = true
}

repository_create = true
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

argocd_sync_options = ["CreateNamespace=true", "ApplyOutOfSyncOnly=true", "FailOnSharedResource=true"]"""
    return tfvars_file