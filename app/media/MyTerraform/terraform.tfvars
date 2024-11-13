
docker_host = "tcp://localhost:2375"
image      = "nginx:latest"
name       = "my-nginx-container"
ports      = ["80:80"]
env        = { "MY_ENV_VAR" = "value" }
