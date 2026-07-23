#!/usr/bin/env bash

set -Eeuo pipefail

PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

echo "========================================="
echo "ALPIP Phase 2.1 Pack 001"
echo "Initializing project skeleton"
echo "Root: $PROJECT_ROOT"
echo "========================================="

cd "$PROJECT_ROOT"

create_dir() {
    mkdir -p "$1"
    echo "Created: $1"
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
echo "Creating directory structure..."

DIRECTORIES=(
    "frontend"
    "backend"
    "core"
    "plugins"
    "sdk"
    "docs"
    "docs/adr"
    "docs/architecture"
    "docs/specifications"
    "tests"
    "tests/integration"
    "tests/unit"
    "scripts"
    "bootstrap"
    "docker"
    ".github"
    ".github/workflows"
    "config"
    "data"
    "storage"
    "logs"
)

for dir in "${DIRECTORIES[@]}"
do
    create_dir "$dir"
done

echo ""
echo "Creating base placeholder files..."

FILES=(
    "frontend/.gitkeep"
    "backend/.gitkeep"
    "core/.gitkeep"
    "plugins/.gitkeep"
    "sdk/.gitkeep"
    "tests/.gitkeep"
    "data/.gitkeep"
    "storage/.gitkeep"
    "logs/.gitkeep"
    "docs/adr/.gitkeep"
    "docs/architecture/.gitkeep"
    "docs/specifications/.gitkeep"
)

for file in "${FILES[@]}"
do
    create_file "$file"
done

echo ""
echo "Pack 001-A completed successfully."
echo ""
echo "Creating project configuration files..."

create_file ".gitignore"

cat > .gitignore <<'EOF'
# OS files
.DS_Store
Thumbs.db

# Environment
.env
.env.*
!.env.example

# Python
__pycache__/
*.py[cod]
*.egg-info/
.venv/
venv/

# Node
node_modules/
.next/
out/
dist/

# Logs
logs/*
!logs/.gitkeep

# Data
data/*
!data/.gitkeep

# Storage
storage/*
!storage/.gitkeep

# IDE
.vscode/
.idea/

# Temporary
*.tmp
*.swp
EOF


create_file "README.md"

cat > README.md <<'EOF'
# ALPIP
## Arabic Legal Intelligence Platform

ALPIP is a modular legal intelligence platform designed with:

- Offline First principles
- Plugin-Based Architecture
- Next.js Frontend
- FastAPI Backend
- AI-assisted legal analysis
- Extensible SDK architecture

## Project Status

Phase 2 - Implementation

Current stage:
Production project skeleton initialization.

## Architecture

Core components:

- Frontend Layer
- Backend Services
- Core Engine
- Plugin System
- SDK
- Documentation
- Automated Testing

## Development

Each implementation phase is delivered through Execution Packs.

Example:

```bash
bash bootstrap/phase-x-pack-xxx.sh
License
See LICENSE file. EOF
create_file "LICENSE"
cat > LICENSE <<'EOF' MIT License
Copyright (c) ALPIP
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files.
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software. EOF
echo "" echo "Creating Master Implementation Roadmap..."
create_file "docs/Master-Implementation-Roadmap.md"
cat > docs/Master-Implementation-Roadmap.md <<'EOF'
ALPIP Master Implementation Roadmap
Mission
Build Arabic Legal Intelligence Platform (ALPIP) as a professional, modular and extensible legal intelligence system.
Project Status
Phase
Status
Progress
Phase 2.1 Foundation
In Progress
20%
Completed
Project repository initialized
Production directory structure created
Documentation structure created
Current Execution Pack
Pack 001
Status: In Progress
Objective:
Initialize production-ready project skeleton.
Next Steps
Frontend foundation
Backend foundation
Core services
Plugin SDK
Testing infrastructure
EOF
echo "" echo "Pack 001-B completed successfully."
echo ""
echo "Running final validation..."

REQUIRED_DIRS=(
    "frontend"
    "backend"
    "core"
    "plugins"
    "sdk"
    "docs"
    "tests"
    "scripts"
    "bootstrap"
    "docker"
    ".github/workflows"
)

VALIDATION_FAILED=0

for dir in "${REQUIRED_DIRS[@]}"
do
    if [ -d "$dir" ]; then
        echo "OK: $dir"
    else
        echo "MISSING: $dir"
        VALIDATION_FAILED=1
    fi
done


REQUIRED_FILES=(
    "README.md"
    ".gitignore"
    "LICENSE"
    "docs/Master-Implementation-Roadmap.md"
)

for file in "${REQUIRED_FILES[@]}"
do
    if [ -f "$file" ]; then
        echo "OK: $file"
    else
        echo "MISSING: $file"
        VALIDATION_FAILED=1
    fi
done


echo ""

if [ "$VALIDATION_FAILED" -eq 0 ]; then
    echo "========================================="
    echo "PACK 001 COMPLETED SUCCESSFULLY"
    echo "Project skeleton is ready."
    echo "========================================="
else
    echo "========================================="
    echo "PACK 001 FAILED VALIDATION"
    echo "Review missing items above."
    echo "========================================="
    exit 1
fi


echo ""
echo "Execution summary:"
echo "- Directory structure: READY"
echo "- Documentation base: READY"
echo "- Roadmap: CREATED"
echo "- Repository foundation: READY"

echo ""
echo "Next:"
echo "git add ."
echo "git commit -m \"feat(bootstrap): initialize production-ready project skeleton\""
echo "git push"

