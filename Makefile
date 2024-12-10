namespace ?= default
releaseName ?= devopsgpt

all: update-submodule build up

update-submodule:
	git submodule init && git submodule update

build:
	docker compose build
up:
	docker compose up -d
down:
	docker compose down -v
helm-install:
	helm install $(releaseName) helm/ -f helm/values.yaml -n $(namespace) --create-namespace
helm-uninstall:
	helm uninstall $(releaseName) -n $(namespace)
