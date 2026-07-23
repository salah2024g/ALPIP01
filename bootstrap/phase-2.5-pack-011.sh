#!/usr/bin/env bash

set -Eeuo pipefail

PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

cd "$PROJECT_ROOT"

echo "========================================="
echo "ALPIP Phase 2.5 Pack 011"
echo "Backend Application Integration Layer"
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
echo "Creating backend integration architecture..."


BACKEND_DIRS=(
"backend/app/api"
"backend/app/api/routes"
"backend/app/api/routes/system"
"backend/app/config"
"backend/app/container"
"backend/app/services"
"backend/app/factory"
"backend/tests/integration"
)


for dir in "${BACKEND_DIRS[@]}"
do
    create_dir "$dir"
done



echo ""
echo "Creating package files..."


BACKEND_FILES=(
"backend/app/api/__init__.py"
"backend/app/api/routes/__init__.py"
"backend/app/api/routes/system/__init__.py"
"backend/app/config/__init__.py"
"backend/app/container/__init__.py"
"backend/app/services/__init__.py"
"backend/app/factory/__init__.py"
)


for file in "${BACKEND_FILES[@]}"
do
    create_file "$file"
done



echo ""
echo "Creating application configuration..."


create_file "backend/app/config/settings.py"

cat > backend/app/config/settings.py <<'EOF'
from dataclasses import dataclass


@dataclass
class Settings:

    app_name: str = "ALPIP"
    version: str = "2.5"
    environment: str = "development"



settings = Settings()
EOF



echo ""
echo "Creating service container..."


create_file "backend/app/container/container.py"

cat > backend/app/container/container.py <<'EOF'
class ServiceContainer:


    def __init__(self):

        self.services = {}



    def register(
        self,
        name: str,
        service
    ):

        self.services[name] = service



    def resolve(
        self,
        name: str
    ):

        return self.services.get(name)



container = ServiceContainer()
EOF



echo ""
echo "Creating application factory..."


create_file "backend/app/factory/application.py"

cat > backend/app/factory/application.py <<'EOF'
from fastapi import FastAPI

from backend.app.config.settings import settings


def create_application():

    app = FastAPI(
        title=settings.app_name,
        version=settings.version
    )


    return app
EOF



echo ""
echo "Creating system health route..."


create_file "backend/app/api/routes/system/health.py"

cat > backend/app/api/routes/system/health.py <<'EOF'
from fastapi import APIRouter


router = APIRouter(
    prefix="/system",
    tags=["System"]
)


@router.get("/health")
def health():

    return {
        "status": "ok",
        "platform": "ALPIP"
    }
EOF



echo ""
echo "Creating backend entry point..."


create_file "backend/app/main.py"

cat > backend/app/main.py <<'EOF'
from backend.app.factory.application import (
    create_application
)


app = create_application()
EOF



echo ""
echo "Pack 011-A completed successfully."
echo ""
echo "Creating API router integration..."


create_file "backend/app/api/router.py"

cat > backend/app/api/router.py <<'EOF'
from fastapi import APIRouter

from backend.app.api.routes.system.health import (
    router as health_router
)


api_router = APIRouter()

api_router.include_router(
    health_router
)
EOF



echo ""
echo "Updating application factory..."


cat > backend/app/factory/application.py <<'EOF'
from fastapi import FastAPI

from backend.app.config.settings import settings
from backend.app.api.router import api_router



def create_application():

    app = FastAPI(
        title=settings.app_name,
        version=settings.version
    )


    app.include_router(
        api_router
    )


    return app
EOF



echo ""
echo "Creating dependency injection helpers..."


create_file "backend/app/container/dependencies.py"

cat > backend/app/container/dependencies.py <<'EOF'
from backend.app.container.container import (
    container
)


def get_service(
    name: str
):

    return container.resolve(
        name
    )
EOF



echo ""
echo "Creating plugin loader foundation..."


create_dir "core/plugins"


create_file "core/plugins/__init__.py"

create_file "core/plugins/loader.py"

cat > core/plugins/loader.py <<'EOF'
class PluginLoader:


    def __init__(self):

        self.plugins = []



    def register(
        self,
        plugin
    ):

        self.plugins.append(
            plugin
        )



    def list_plugins(self):

        return [
            plugin.name
            for plugin in self.plugins
        ]
EOF



echo ""
echo "Creating plugin registry..."


create_file "core/plugins/registry.py"

cat > core/plugins/registry.py <<'EOF'
from core.plugins.loader import (
    PluginLoader
)


plugin_registry = PluginLoader()
EOF



echo ""
echo "Creating integration test..."


create_file "backend/tests/integration/test_application.py"

cat > backend/tests/integration/test_application.py <<'EOF'
from backend.app.factory.application import (
    create_application
)


def test_application_creation():

    app = create_application()

    assert app.title == "ALPIP"
EOF



echo ""
echo "Creating backend architecture ADR..."


create_file "docs/adr/ADR-007-backend-application-architecture.md"

cat > docs/adr/ADR-007-backend-application-architecture.md <<'EOF'
# ADR-007: Backend Application Architecture

## Status

Accepted


## Context

ALPIP requires a unified backend layer integrating all core modules.


## Decision

Backend architecture will use:

- FastAPI application factory
- API Router aggregation
- Dependency injection container
- Plugin loader


## Benefits

- Modular backend
- Easier testing
- Plugin extensibility


## Consequences

All backend modules must be registered through application integration layers.
EOF



echo ""
echo "Updating roadmap..."

if [ -f "docs/Master-Implementation-Roadmap.md" ]; then

cat >> docs/Master-Implementation-Roadmap.md <<'EOF'


## Pack 011 Progress

Status:

In Progress

Completed:

- FastAPI application factory
- API router integration
- Dependency injection foundation
- Plugin loader foundation
- Backend integration tests
- ADR-007 created

EOF

fi


echo ""
echo "Pack 011-B completed successfully."
echo ""
echo "Running Pack 011 validation..."


VALIDATION_FAILED=0


REQUIRED_DIRS=(
"backend/app/api"
"backend/app/api/routes"
"backend/app/api/routes/system"
"backend/app/config"
"backend/app/container"
"backend/app/services"
"backend/app/factory"
"core/plugins"
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



REQUIRED_FILES=(
"backend/app/config/settings.py"
"backend/app/container/container.py"
"backend/app/container/dependencies.py"
"backend/app/factory/application.py"
"backend/app/api/router.py"
"backend/app/api/routes/system/health.py"
"backend/app/main.py"
"core/plugins/loader.py"
"core/plugins/registry.py"
"backend/tests/integration/test_application.py"
"docs/adr/ADR-007-backend-application-architecture.md"
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



echo ""

if [ "$VALIDATION_FAILED" -eq 0 ]; then

    echo "========================================="
    echo "PACK 011 COMPLETED SUCCESSFULLY"
    echo "Backend Integration Layer is ready."
    echo "========================================="


    if [ -f "docs/Master-Implementation-Roadmap.md" ]; then

cat >> docs/Master-Implementation-Roadmap.md <<'EOF'


## Pack 011 Final Status

Status:

Completed

Delivered:

- FastAPI Application Factory
- API Router Integration
- Dependency Injection Foundation
- Service Container
- Plugin Loader Foundation
- Health Monitoring Endpoint
- Backend Architecture ADR

EOF

    fi


else

    echo "========================================="
    echo "PACK 011 FAILED"
    echo "Review missing items above."
    echo "========================================="

    exit 1

fi


echo ""
echo "Next commands:"
echo "git add ."
echo "git commit -m \"feat(backend): add application integration layer\""
echo "git push"
