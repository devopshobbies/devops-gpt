
terraform {
  required_version = ">= 1.0"

  required_providers {
    argocd = {
      source  = "oboukili/argocd"
      version = ">= 6.0.2"
    }
  }
}
