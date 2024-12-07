namespace ?= default
releaseName ?= devopsgpt

all: build up

build:
	docker-compose build
up:
	docker-compose up -d
down:
	docker-compose down -v
helm-install:
	helm install $(releaseName) helm/ -f helm/values.yaml -n $(namespace) --create-namespace
helm-uninstall:
	helm uninstall $(releaseName) -n $(namespace)
