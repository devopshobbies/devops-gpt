import os

project_name = "app/media/MyCompose"
compose_file_path = os.path.join(project_name, "docker-compose.yaml")

# Create project directories
os.makedirs(project_name, exist_ok=True)

# Create docker-compose.yaml
with open(compose_file_path, "w") as compose_file:
    compose_file.write("version: '3'\n")
    compose_file.write("services:\n")
    compose_file.write("  web_server:\n")
    compose_file.write("    image: nginx:latest\n")
    compose_file.write("    volumes:\n")
    compose_file.write("      - ./nginx/nginx.conf:/etc/nginx/nginx.conf\n")
    compose_file.write("    depends_on:\n")
    compose_file.write("      - string\n")
    compose_file.write("    ports:\n")
    compose_file.write("      - '80:80'\n")
    compose_file.write("    environment:\n")
    compose_file.write("      - foo=bar\n")
    compose_file.write("    networks:\n")
    compose_file.write("      - app_network\n")
    compose_file.write("  monitoring_server:\n")
    compose_file.write("    image: grafana:latest\n")
    compose_file.write("    volumes:\n")
    compose_file.write("      - ./nginx/nginx.conf:/etc/nginx/nginx.conf\n")
    compose_file.write("    depends_on:\n")
    compose_file.write("      - string\n")
    compose_file.write("    ports:\n")
    compose_file.write("      - '82:80'\n")
    compose_file.write("    environment:\n")
    compose_file.write("      - foo=bar\n")
    compose_file.write("    networks:\n")
    compose_file.write("      - app_network\n")
    compose_file.write("networks:\n")
    compose_file.write("  app_network:\n")
    compose_file.write("    driver: bridge\n")