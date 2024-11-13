
image = "nginx:latest"
name  = "my-nginx-container"
ports = ["80:80"]
env   = { "MY_ENV_VAR" = "value" }
