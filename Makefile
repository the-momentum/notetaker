### Variables ###

# please note that docker-compose is deprecated in Compose V2 and replaced by docker compose. See more here: https://docs.docker.com/compose/migrate/
containers-tool = docker compose
dockercompose-file = -f docker/docker-compose.yml

### Development ###

.PHONY: docker-build
docker-build:
	$(containers-tool) $(dockercompose-file) build
	make docker-up

.PHONY: docker-rebuild
docker-rebuild:
	$(containers-tool) $(dockercompose-file) build --no-cache
	make docker-up

.PHONY: docker-up
docker-up:
	$(containers-tool) $(dockercompose-file) --profile default up --remove-orphans

.PHONY: docker-demo
docker-demo:
	$(containers-tool) $(dockercompose-file) --profile demo up --remove-orphans
