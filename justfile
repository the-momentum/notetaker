# Variables
containers-tool := "docker compose"
dockercompose-file := "-f docker/docker-compose.yml"

# Development commands

# Build Docker containers and bring them up
docker-build:
    {{containers-tool}} {{dockercompose-file}} build
    just docker-up

# Rebuild Docker containers without using cache and bring them up
docker-rebuild:
    {{containers-tool}} {{dockercompose-file}} build --no-cache
    just docker-up

# Start the default Docker containers
docker-up:
    {{containers-tool}} {{dockercompose-file}} --profile default up --remove-orphans

# Start the demo Docker containers
docker-demo:
    {{containers-tool}} {{dockercompose-file}} --profile demo up --remove-orphans