
output "container_id" {
  description = "The ID of the Docker container."
  value       = docker_container.app.id
}

output "container_ip" {
  description = "The IP address of the Docker container."
  value       = docker_container.app.ip_address
}
