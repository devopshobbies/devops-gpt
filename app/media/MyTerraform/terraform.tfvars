
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
