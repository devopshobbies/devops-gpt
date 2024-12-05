{
  "version": "3",
  "services": {
    "webserver": {
      "build": {
        "context": ".",
        "dockerfile": "DockerFile"
      },
      "image": null,
      "container_name": "web_server",
      "command": null,
      "volumes": null,
      "environment": {
        "foo": "bar"
      },
      "ports": [
        "80:80"
      ],
      "networks": [
        "app_network"
      ],
      "args": null,
      "depends_on": null
   

    }
      
}
}