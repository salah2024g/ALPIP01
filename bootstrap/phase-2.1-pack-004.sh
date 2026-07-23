#!/usr/bin/env bash

set -Eeuo pipefail

PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

cd "$PROJECT_ROOT"

echo "========================================="
echo "ALPIP Phase 2.1 Pack 004"
echo "Docker & CI Foundation"
echo "========================================="


create_dir() {
    mkdir -p "$1"
    echo "Created directory: $1"
}


create_file() {
    if [ ! -f "$1" ]; then
        touch "$1"
        echo "Created file: $1"
    else
        echo "Exists: $1"
    fi
}


echo ""
echo "Creating Docker structure..."


DOCKER_DIRS=(
"docker/backend"
"docker/frontend"
)


for dir in "${DOCKER_DIRS[@]}"
do
    create_dir "$dir"
done



echo ""
echo "Creating backend Dockerfile..."


create_file "docker/backend/Dockerfile"

cat > docker/backend/Dockerfile <<'EOF'
FROM python:3.12-slim

WORKDIR /app

COPY backend/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY backend .

EXPOSE 8000

CMD [
    "uvicorn",
    "app.main:app",
    "--host",
    "0.0.0.0",
    "--port",
    "8000"
]
EOF



echo ""
echo "Creating frontend Dockerfile..."


create_file "docker/frontend/Dockerfile"

cat > docker/frontend/Dockerfile <<'EOF'
FROM node:20-alpine

WORKDIR /app

COPY frontend/package.json .

RUN npm install

COPY frontend .

EXPOSE 3000

CMD [
    "npm",
    "run",
    "dev"
]
EOF



echo ""
echo "Creating docker ignore..."


create_file ".dockerignore"

cat > .dockerignore <<'EOF'
.git
.github
node_modules
.next
__pycache__
*.pyc
.env
logs
data
storage
EOF



echo ""
echo "Pack 004-A completed successfully."
echo ""
echo "Creating Docker Compose configuration..."


create_file "docker-compose.yml"

cat > docker-compose.yml <<'EOF'
services:

  backend:
    build:
      context: .
      dockerfile: docker/backend/Dockerfile
    container_name: alpip-backend
    ports:
      - "8000:8000"
    environment:
      - ENVIRONMENT=development
    volumes:
      - ./backend:/app


  frontend:
    build:
      context: .
      dockerfile: docker/frontend/Dockerfile
    container_name: alpip-frontend
    ports:
      - "3000:3000"
    environment:
      - NEXT_PUBLIC_API_URL=http://localhost:8000
    volumes:
      - ./frontend:/app
EOF



echo ""
echo "Creating environment templates..."


create_file ".env.example"

cat > .env.example <<'EOF'
# ALPIP Global Environment

PROJECT_NAME=ALPIP
ENVIRONMENT=development

BACKEND_PORT=8000
FRONTEND_PORT=3000
EOF



echo ""
echo "Creating GitHub Actions workflow..."


create_dir ".github/workflows"


create_file ".github/workflows/ci.yml"

cat > .github/workflows/ci.yml <<'EOF'
name: ALPIP CI

on:
  push:
    branches:
      - main

  pull_request:
    branches:
      - main


jobs:

  validate:

    runs-on: ubuntu-latest

    steps:

      - name: Checkout repository
        uses: actions/checkout@v4


      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.12"


      - name: Validate backend structure
        run: |
          python --version
          test -f backend/app/main.py


      - name: Validate frontend structure
        run: |
          test -f frontend/package.json
EOF



echo ""
echo "Updating architecture documentation..."


create_file "docs/architecture/development-environment.md"

cat > docs/architecture/development-environment.md <<'EOF'
# ALPIP Development Environment

## Containers

ALPIP uses:

- Backend container
- Frontend container

## Ports

Backend:

8000

Frontend:

3000

## CI/CD

GitHub Actions validates:

- Repository structure
- Backend foundation
- Frontend foundation
EOF



echo ""
echo "Updating roadmap..."

if [ -f "docs/Master-Implementation-Roadmap.md" ]; then

cat >> docs/Master-Implementation-Roadmap.md <<'EOF'


## Pack 004 Progress

Status:

In Progress

Completed:

- Docker foundation
- Docker Compose setup
- CI workflow foundation
- Development environment documentation

EOF

fi


echo ""
echo "Pack 004-B completed successfully."
echo ""
echo "Running Pack 004 validation..."


VALIDATION_FAILED=0


REQUIRED_FILES=(
"docker/backend/Dockerfile"
"docker/frontend/Dockerfile"
".dockerignore"
"docker-compose.yml"
".env.example"
".github/workflows/ci.yml"
"docs/architecture/development-environment.md"
)


for file in "${REQUIRED_FILES[@]}"
do
    if [ -f "$file" ]; then
        echo "OK file: $file"
    else
        echo "MISSING file: $file"
        VALIDATION_FAILED=1
    fi
done



REQUIRED_DIRS=(
"docker"
"docker/backend"
"docker/frontend"
".github/workflows"
)


for dir in "${REQUIRED_DIRS[@]}"
do
    if [ -d "$dir" ]; then
        echo "OK directory: $dir"
    else
        echo "MISSING directory: $dir"
        VALIDATION_FAILED=1
    fi
done



echo ""

if [ "$VALIDATION_FAILED" -eq 0 ]; then

    echo "========================================="
    echo "PACK 004 COMPLETED SUCCESSFULLY"
    echo "Docker and CI foundation is ready."
    echo "========================================="


    if [ -f "docs/Master-Implementation-Roadmap.md" ]; then

cat >> docs/Master-Implementation-Roadmap.md <<'EOF'


## Pack 004 Final Status

Status:

Completed

Delivered:

- Docker backend container
- Docker frontend container
- Docker Compose environment
- GitHub Actions CI foundation
- Development environment documentation

EOF

    fi


else

    echo "========================================="
    echo "PACK 004 FAILED"
    echo "Review missing items above."
    echo "========================================="

    exit 1

fi


echo ""
echo "Next commands:"
echo "git add ."
echo "git commit -m \"feat(devops): add docker and ci foundation\""
echo "git push"
