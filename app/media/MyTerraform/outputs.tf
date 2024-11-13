
output "container_id" {
  description = "The ID of the Docker container."
  value       = module.docker_container.container_id
}

output "container_ip" {
  description = "The IP address of the Docker container."
  value       = module.docker_container.container_ip
}
