terraform {
  required_version = ">= 1.0"

  required_providers {
    docker = {
      source  = "hashicorp/docker"
      version = ">= 2.0"
    }
  }
}
