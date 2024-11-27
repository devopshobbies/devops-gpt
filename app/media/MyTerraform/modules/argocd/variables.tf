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
