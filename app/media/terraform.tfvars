
argocd_instance_info = {
  server_addr = "http://argocd.local"
  username    = "username"
  password    = "password"
  insecure    = true
}
    

repository_create = true
argocd_repository_info = {
  repo     = "https://your_repo.git"
  username = "username"
  password = "token"
}
    

application_create = false
argocd_application = {
  name                   = "myapp"
  destination_server     = "https://kubernetes.default.svc"
  destination_namespace  = "default"
  source_repo_url       = "https://your_repo.git"
  source_path           = "myapp/manifests"
  source_target_revision = "master"
}
    

argocd_sync_options = ["CreateNamespace=true", "ApplyOutOfSyncOnly=true", "FailOnSharedResource=true"]

auto_prune = false
self_heal = false 