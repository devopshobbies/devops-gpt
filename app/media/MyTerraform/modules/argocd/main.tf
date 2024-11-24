
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
      repo_url = var.argocd_application["source_repo_url"]
      path     = var.argocd_application["source_path"]
      target_revision = var.argocd_application["source_target_revision"]
    }
    sync_policy {
      automated {
        prune     = true
        self_heal = true
      }
      sync_options = var.argocd_sync_options
    }
  }
}
