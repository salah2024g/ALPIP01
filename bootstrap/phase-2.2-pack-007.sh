#!/usr/bin/env bash

set -Eeuo pipefail

PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

cd "$PROJECT_ROOT"

echo "========================================="
echo "ALPIP Phase 2.2 Pack 007"
echo "Authentication + Security Foundation"
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
echo "Creating security architecture..."


SECURITY_DIRS=(
"backend/app/security"
"backend/app/security/auth"
"backend/app/security/services"
"backend/app/security/utils"
"backend/app/security/models"
"backend/app/api/routes/auth"
"backend/tests/security"
)


for dir in "${SECURITY_DIRS[@]}"
do
    create_dir "$dir"
done



echo ""
echo "Creating security package files..."


SECURITY_FILES=(
"backend/app/security/__init__.py"
"backend/app/security/auth/__init__.py"
"backend/app/security/services/__init__.py"
"backend/app/security/utils/__init__.py"
"backend/app/security/models/__init__.py"
"backend/app/api/routes/auth/__init__.py"
)


for file in "${SECURITY_FILES[@]}"
do
    create_file "$file"
done



echo ""
echo "Creating user security model..."


create_file "backend/app/security/models/user.py"

cat > backend/app/security/models/user.py <<'EOF'
from dataclasses import dataclass


@dataclass
class User:

    id: int
    username: str
    email: str
    is_active: bool = True
EOF



echo ""
echo "Creating password security utility..."


create_file "backend/app/security/utils/password.py"

cat > backend/app/security/utils/password.py <<'EOF'
import hashlib


def hash_password(password: str) -> str:

    return hashlib.sha256(
        password.encode()
    ).hexdigest()



def verify_password(
    password: str,
    hashed_password: str
) -> bool:

    return (
        hash_password(password)
        == hashed_password
    )
EOF



echo ""
echo "Creating JWT service foundation..."


create_file "backend/app/security/services/jwt.py"

cat > backend/app/security/services/jwt.py <<'EOF'
from datetime import datetime, timedelta


SECRET_KEY = "change-me"
ALGORITHM = "HS256"



def create_token(subject: str) -> dict:

    expires = datetime.utcnow() + timedelta(
        minutes=30
    )

    return {
        "sub": subject,
        "expires": expires.isoformat()
    }



def decode_token(token: dict):

    return token.get("sub")
EOF



echo ""
echo "Pack 007-A completed successfully."
echo ""
echo "Creating authentication services..."


create_file "backend/app/security/services/auth.py"

cat > backend/app/security/services/auth.py <<'EOF'
from app.security.utils.password import (
    hash_password,
    verify_password
)


class AuthService:

    def create_user_password(
        self,
        password: str
    ) -> str:

        return hash_password(password)


    def authenticate(
        self,
        password: str,
        stored_password: str
    ) -> bool:

        return verify_password(
            password,
            stored_password
        )
EOF



echo ""
echo "Creating permission foundation..."


create_file "backend/app/security/services/permissions.py"

cat > backend/app/security/services/permissions.py <<'EOF'
from enum import Enum


class Permission(str, Enum):

    READ = "read"
    WRITE = "write"
    ADMIN = "admin"



def has_permission(
    user_permissions: list,
    required: Permission
) -> bool:

    return required.value in user_permissions
EOF



echo ""
echo "Creating authentication API foundation..."


create_file "backend/app/api/routes/auth/router.py"

cat > backend/app/api/routes/auth/router.py <<'EOF'
from fastapi import APIRouter


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.get("/status")
def auth_status():

    return {
        "authentication": "ready"
    }
EOF



echo ""
echo "Creating security tests..."


create_file "backend/tests/security/test_password.py"

cat > backend/tests/security/test_password.py <<'EOF'
from app.security.utils.password import (
    hash_password,
    verify_password
)


def test_password_hash():

    password = "secret"

    hashed = hash_password(
        password
    )

    assert verify_password(
        password,
        hashed
    )
EOF



echo ""
echo "Updating requirements..."


if [ -f "backend/requirements.txt" ]; then

cat >> backend/requirements.txt <<'EOF'

python-jose
passlib
EOF

fi



echo ""
echo "Creating Security ADR..."


create_file "docs/adr/ADR-003-security-architecture.md"

cat > docs/adr/ADR-003-security-architecture.md <<'EOF'
# ADR-003: Security Architecture

## Status

Accepted

## Context

ALPIP requires secure access control before handling legal data.

## Decision

The system will use:

- Token-based authentication
- Password hashing
- Permission-based authorization

## Principles

- Secure by design
- Least privilege
- Separation of authentication and authorization

## Consequences

All protected resources must pass security checks.
EOF



echo ""
echo "Updating roadmap..."

if [ -f "docs/Master-Implementation-Roadmap.md" ]; then

cat >> docs/Master-Implementation-Roadmap.md <<'EOF'


## Pack 007 Progress

Status:

In Progress

Completed:

- Security architecture
- User identity foundation
- Password hashing
- JWT foundation
- Permission model
- ADR-003 created

EOF

fi


echo ""
echo "Pack 007-B completed successfully."
echo ""
echo "Running Pack 007 validation..."


VALIDATION_FAILED=0


REQUIRED_DIRS=(
"backend/app/security"
"backend/app/security/auth"
"backend/app/security/services"
"backend/app/security/utils"
"backend/app/security/models"
"backend/app/api/routes/auth"
"backend/tests/security"
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
"backend/app/security/models/user.py"
"backend/app/security/utils/password.py"
"backend/app/security/services/jwt.py"
"backend/app/security/services/auth.py"
"backend/app/security/services/permissions.py"
"backend/app/api/routes/auth/router.py"
"backend/tests/security/test_password.py"
"docs/adr/ADR-003-security-architecture.md"
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
    echo "PACK 007 COMPLETED SUCCESSFULLY"
    echo "Security foundation is ready."
    echo "========================================="


    if [ -f "docs/Master-Implementation-Roadmap.md" ]; then

cat >> docs/Master-Implementation-Roadmap.md <<'EOF'


## Pack 007 Final Status

Status:

Completed

Delivered:

- Authentication foundation
- JWT service foundation
- Password security utilities
- Permission model
- Security architecture ADR

EOF

    fi


else

    echo "========================================="
    echo "PACK 007 FAILED"
    echo "Review missing items above."
    echo "========================================="

    exit 1

fi


echo ""
echo "Next commands:"
echo "git add ."
echo "git commit -m \"feat(security): add authentication foundation\""
echo "git push"
