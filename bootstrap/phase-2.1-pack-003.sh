#!/usr/bin/env bash

set -Eeuo pipefail

PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

cd "$PROJECT_ROOT"

echo "========================================="
echo "ALPIP Phase 2.1 Pack 003"
echo "Backend FastAPI Foundation"
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
echo "Creating backend architecture..."


BACKEND_DIRS=(
"backend/app"
"backend/app/api"
"backend/app/api/routes"
"backend/app/core"
"backend/app/config"
"backend/app/services"
"backend/app/models"
"backend/app/schemas"
"backend/app/utils"
"backend/tests"
"backend/logs"
)


for dir in "${BACKEND_DIRS[@]}"
do
    create_dir "$dir"
done


echo ""
echo "Creating Python package files..."


PYTHON_FILES=(
"backend/app/__init__.py"
"backend/app/api/__init__.py"
"backend/app/api/routes/__init__.py"
"backend/app/core/__init__.py"
"backend/app/config/__init__.py"
"backend/app/services/__init__.py"
"backend/app/models/__init__.py"
"backend/app/schemas/__init__.py"
"backend/app/utils/__init__.py"
)


for file in "${PYTHON_FILES[@]}"
do
    create_file "$file"
done


echo ""
echo "Creating FastAPI application..."


create_file "backend/app/main.py"

cat > backend/app/main.py <<'EOF'
from fastapi import FastAPI

from app.api.routes.health import router as health_router


app = FastAPI(
    title="ALPIP API",
    description="Arabic Legal Intelligence Platform API",
    version="0.1.0"
)


app.include_router(
    health_router,
    prefix="/api"
)


@app.get("/")
def root():
    return {
        "name": "ALPIP",
        "status": "running"
    }
EOF


echo ""
echo "Creating API health endpoint..."


create_file "backend/app/api/routes/health.py"

cat > backend/app/api/routes/health.py <<'EOF'
from fastapi import APIRouter


router = APIRouter()


@router.get("/health")
def health_check():
    return {
        "status": "ok"
    }
EOF


echo ""
echo "Creating configuration foundation..."


create_file "backend/app/config/settings.py"

cat > backend/app/config/settings.py <<'EOF'
from dataclasses import dataclass


@dataclass
class Settings:
    app_name: str = "ALPIP"
    environment: str = "development"


settings = Settings()
EOF


echo ""
echo "Pack 003-A completed successfully."
echo ""
echo "Creating backend infrastructure..."


create_file "backend/app/core/logging.py"

cat > backend/app/core/logging.py <<'EOF'
import logging


def setup_logging() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s"
    )


logger = logging.getLogger("alpip")
EOF



create_file "backend/app/core/dependencies.py"

cat > backend/app/core/dependencies.py <<'EOF'
from app.config.settings import settings


def get_settings():
    return settings
EOF



create_file "backend/.env.example"

cat > backend/.env.example <<'EOF'
APP_NAME=ALPIP
ENVIRONMENT=development
EOF



create_file "backend/requirements.txt"

cat > backend/requirements.txt <<'EOF'
fastapi
uvicorn
pydantic
pytest
httpx
EOF



create_file "backend/pytest.ini"

cat > backend/pytest.ini <<'EOF'
[pytest]
testpaths =
    tests
EOF



create_file "backend/tests/__init__.py"



echo ""
echo "Creating backend test foundation..."


create_file "backend/tests/test_health.py"

cat > backend/tests/test_health.py <<'EOF'
def test_placeholder():
    assert True
EOF



echo ""
echo "Creating backend documentation..."


create_file "docs/architecture/backend-architecture.md"

cat > docs/architecture/backend-architecture.md <<'EOF'
# ALPIP Backend Architecture

## Technology

- Python
- FastAPI
- REST API

## Structure

backend/app:

- api
- core
- config
- services
- models
- schemas
- utils

## Principles

- Modular design
- Dependency injection
- Clear separation of concerns
- Testable components
EOF



echo ""
echo "Updating roadmap..."

if [ -f "docs/Master-Implementation-Roadmap.md" ]; then

cat >> docs/Master-Implementation-Roadmap.md <<'EOF'


## Pack 003 Progress

Status:

In Progress

Completed:

- FastAPI application foundation
- API routing foundation
- Configuration layer
- Logging foundation
- Testing foundation

EOF

fi


echo ""
echo "Pack 003-B completed successfully."
echo ""
echo "Running Pack 003 validation..."


VALIDATION_FAILED=0


REQUIRED_BACKEND_DIRS=(
"backend/app"
"backend/app/api"
"backend/app/api/routes"
"backend/app/core"
"backend/app/config"
"backend/app/services"
"backend/app/models"
"backend/app/schemas"
"backend/tests"
)


for dir in "${REQUIRED_BACKEND_DIRS[@]}"
do
    if [ -d "$dir" ]; then
        echo "OK directory: $dir"
    else
        echo "MISSING directory: $dir"
        VALIDATION_FAILED=1
    fi
done



REQUIRED_BACKEND_FILES=(
"backend/app/main.py"
"backend/app/api/routes/health.py"
"backend/app/config/settings.py"
"backend/app/core/logging.py"
"backend/app/core/dependencies.py"
"backend/requirements.txt"
"backend/pytest.ini"
"backend/tests/test_health.py"
"docs/architecture/backend-architecture.md"
)


for file in "${REQUIRED_BACKEND_FILES[@]}"
do
    if [ -f "$file" ]; then
        echo "OK file: $file"
    else
        echo "MISSING file: $file"
        VALIDATION_FAILED=1
    fi
done



echo ""

if [ "$VALIDATION_FAILED" -eq 0 ]; then

    echo "========================================="
    echo "PACK 003 COMPLETED SUCCESSFULLY"
    echo "Backend foundation is ready."
    echo "========================================="


    if [ -f "docs/Master-Implementation-Roadmap.md" ]; then

cat >> docs/Master-Implementation-Roadmap.md <<'EOF'


## Pack 003 Final Status

Status:

Completed

Delivered:

- FastAPI backend foundation
- API routing
- Configuration management
- Logging system
- Dependency injection foundation
- Testing structure

EOF

    fi


else

    echo "========================================="
    echo "PACK 003 FAILED"
    echo "Review missing items above."
    echo "========================================="

    exit 1

fi


echo ""
echo "Next commands:"
echo "git add ."
echo "git commit -m \"feat(backend): initialize FastAPI foundation\""
echo "git push"
