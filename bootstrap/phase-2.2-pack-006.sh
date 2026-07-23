#!/usr/bin/env bash

set -Eeuo pipefail

PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

cd "$PROJECT_ROOT"

echo "========================================="
echo "ALPIP Phase 2.2 Pack 006"
echo "Data Layer + Database Foundation"
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
echo "Creating data architecture..."


DATA_DIRS=(
"backend/app/database"
"backend/app/database/models"
"backend/app/database/repositories"
"backend/app/database/migrations"
"backend/app/database/session"
"backend/tests/database"
)


for dir in "${DATA_DIRS[@]}"
do
    create_dir "$dir"
done



echo ""
echo "Creating database package files..."


DATABASE_FILES=(
"backend/app/database/__init__.py"
"backend/app/database/models/__init__.py"
"backend/app/database/repositories/__init__.py"
"backend/app/database/session/__init__.py"
)


for file in "${DATABASE_FILES[@]}"
do
    create_file "$file"
done



echo ""
echo "Creating database configuration..."


create_file "backend/app/database/session/database.py"

cat > backend/app/database/session/database.py <<'EOF'
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


DATABASE_URL = "sqlite:///./alpip.db"


engine = create_engine(
    DATABASE_URL,
    connect_args={
        "check_same_thread": False
    }
)


SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()
EOF



echo ""
echo "Creating base model..."


create_file "backend/app/database/models/base.py"

cat > backend/app/database/models/base.py <<'EOF'
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass
EOF



echo ""
echo "Creating initial entity model..."


create_file "backend/app/database/models/plugin.py"

cat > backend/app/database/models/plugin.py <<'EOF'
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from .base import Base


class PluginModel(Base):

    __tablename__ = "plugins"


    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True
    )


    name: Mapped[str] = mapped_column(
        String(100),
        unique=True
    )


    version: Mapped[str] = mapped_column(
        String(50)
    )
EOF



echo ""
echo "Pack 006-A completed successfully."
echo ""
echo "Creating repository layer..."


create_file "backend/app/database/repositories/base.py"

cat > backend/app/database/repositories/base.py <<'EOF'
from typing import Generic, TypeVar


T = TypeVar("T")


class BaseRepository(Generic[T]):

    def __init__(self, model):
        self.model = model


    def get_model(self):
        return self.model
EOF



create_file "backend/app/database/repositories/plugin_repository.py"

cat > backend/app/database/repositories/plugin_repository.py <<'EOF'
from .base import BaseRepository

from app.database.models.plugin import PluginModel


class PluginRepository(
    BaseRepository
):

    def __init__(self):
        super().__init__(
            PluginModel
        )
EOF



echo ""
echo "Creating database initialization..."


create_file "backend/app/database/init_db.py"

cat > backend/app/database/init_db.py <<'EOF'
from app.database.session.database import engine
from app.database.models.base import Base


def initialize_database():

    Base.metadata.create_all(
        bind=engine
    )
EOF



echo ""
echo "Adding database dependencies..."


if [ -f "backend/requirements.txt" ]; then

cat >> backend/requirements.txt <<'EOF'

sqlalchemy
alembic
EOF

fi



echo ""
echo "Creating migration foundation..."


create_file "backend/alembic.ini"

cat > backend/alembic.ini <<'EOF'
[alembic]

script_location = migrations

sqlalchemy.url = sqlite:///./alpip.db
EOF



create_dir "backend/migrations"

create_file "backend/migrations/README.md"

cat > backend/migrations/README.md <<'EOF'
# ALPIP Database Migrations

Migration scripts will be managed using Alembic.
EOF



echo ""
echo "Creating database architecture ADR..."


create_file "docs/adr/ADR-002-database-architecture.md"

cat > docs/adr/ADR-002-database-architecture.md <<'EOF'
# ADR-002: Database Architecture

## Status

Accepted

## Context

ALPIP requires a structured persistence layer.

## Decision

The platform will use:

- SQLAlchemy ORM
- Repository Pattern
- Migration Management

## Benefits

- Separation between business logic and persistence
- Easier testing
- Future database migration support

## Consequences

All database access should pass through repositories.
EOF



echo ""
echo "Updating roadmap..."

if [ -f "docs/Master-Implementation-Roadmap.md" ]; then

cat >> docs/Master-Implementation-Roadmap.md <<'EOF'


## Pack 006 Progress

Status:

In Progress

Completed:

- Database configuration
- SQLAlchemy foundation
- Base models
- Repository layer
- Migration foundation
- ADR-002 created

EOF

fi


echo ""
echo "Pack 006-B completed successfully."


echo ""
echo "Running Pack 006 validation..."


VALIDATION_FAILED=0


REQUIRED_DIRS=(
"backend/app/database"
"backend/app/database/models"
"backend/app/database/repositories"
"backend/app/database/session"
"backend/migrations"
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
"backend/app/database/session/database.py"
"backend/app/database/models/base.py"
"backend/app/database/models/plugin.py"
"backend/app/database/repositories/base.py"
"backend/app/database/repositories/plugin_repository.py"
"backend/app/database/init_db.py"
"backend/alembic.ini"
"backend/migrations/README.md"
"docs/adr/ADR-002-database-architecture.md"
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
    echo "PACK 006 COMPLETED SUCCESSFULLY"
    echo "Database foundation is ready."
    echo "========================================="


    if [ -f "docs/Master-Implementation-Roadmap.md" ]; then

cat >> docs/Master-Implementation-Roadmap.md <<'EOF'


## Pack 006 Final Status

Status:

Completed

Delivered:

- Database Layer Foundation
- SQLAlchemy Integration
- Initial Models
- Repository Pattern
- Migration Foundation
- Database Architecture ADR

EOF

    fi


else

    echo "========================================="
    echo "PACK 006 FAILED"
    echo "Review missing items above."
    echo "========================================="

    exit 1

fi


echo ""
echo "Next commands:"
echo "git add ."
echo "git commit -m \"feat(data): add database layer foundation\""
echo "git push"
