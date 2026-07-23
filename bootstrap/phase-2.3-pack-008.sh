#!/usr/bin/env bash

set -Eeuo pipefail

PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

cd "$PROJECT_ROOT"

echo "========================================="
echo "ALPIP Phase 2.3 Pack 008"
echo "Legal Domain Core Foundation"
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
echo "Creating legal domain architecture..."


LEGAL_DIRS=(
"core/legal"
"core/legal/models"
"core/legal/types"
"core/legal/services"
"core/legal/extractors"
"core/legal/tests"
"plugins/legal"
"plugins/legal/models"
"plugins/legal/services"
"plugins/legal/tests"
)


for dir in "${LEGAL_DIRS[@]}"
do
    create_dir "$dir"
done



echo ""
echo "Creating package files..."


LEGAL_FILES=(
"core/legal/__init__.py"
"core/legal/models/__init__.py"
"core/legal/types/__init__.py"
"core/legal/services/__init__.py"
"core/legal/extractors/__init__.py"
"plugins/legal/__init__.py"
"plugins/legal/models/__init__.py"
"plugins/legal/services/__init__.py"
)


for file in "${LEGAL_FILES[@]}"
do
    create_file "$file"
done



echo ""
echo "Creating legal document types..."


create_file "core/legal/types/document_type.py"

cat > core/legal/types/document_type.py <<'EOF'
from enum import Enum


class DocumentType(str, Enum):

    LAW = "law"
    REGULATION = "regulation"
    DECISION = "decision"
    INSTRUCTION = "instruction"
EOF



echo ""
echo "Creating legislation model..."


create_file "core/legal/models/legislation.py"

cat > core/legal/models/legislation.py <<'EOF'
from dataclasses import dataclass


@dataclass
class Legislation:

    id: int
    title: str
    number: str
    year: int
    document_type: str
EOF



echo ""
echo "Creating article model..."


create_file "core/legal/models/article.py"

cat > core/legal/models/article.py <<'EOF'
from dataclasses import dataclass


@dataclass
class LegalArticle:

    id: int
    article_number: str
    text: str
    legislation_id: int
EOF



echo ""
echo "Creating document metadata..."


create_file "core/legal/models/document.py"

cat > core/legal/models/document.py <<'EOF'
from dataclasses import dataclass


@dataclass
class LegalDocument:

    filename: str
    file_type: str
    source: str
    language: str = "ar"
EOF



echo ""
echo "Pack 008-A completed successfully."
echo ""
echo "Creating document processing foundation..."


create_file "core/legal/extractors/base.py"

cat > core/legal/extractors/base.py <<'EOF'
from abc import ABC, abstractmethod


class DocumentExtractor(ABC):

    @abstractmethod
    def extract(self, file_path: str) -> str:
        pass
EOF



echo ""
echo "Creating PDF extractor foundation..."


create_file "core/legal/extractors/pdf.py"

cat > core/legal/extractors/pdf.py <<'EOF'
from .base import DocumentExtractor


class PDFExtractor(DocumentExtractor):

    def extract(
        self,
        file_path: str
    ) -> str:

        return ""
EOF



echo ""
echo "Creating legal processing service..."


create_file "core/legal/services/document_service.py"

cat > core/legal/services/document_service.py <<'EOF'
from core.legal.extractors.pdf import PDFExtractor


class LegalDocumentService:

    def __init__(self):

        self.extractor = PDFExtractor()


    def process(
        self,
        file_path: str
    ) -> dict:

        text = self.extractor.extract(
            file_path
        )

        return {
            "file": file_path,
            "text": text
        }
EOF



echo ""
echo "Creating legal plugin foundation..."


create_file "plugins/legal/plugin.py"

cat > plugins/legal/plugin.py <<'EOF'
from sdk.contracts.plugin import PluginContract


class LegalPlugin(PluginContract):

    @property
    def name(self):

        return "legal-domain"


    def initialize(self):

        pass


    def execute(
        self,
        payload: dict
    ):

        return {
            "status": "processed",
            "payload": payload
        }
EOF



echo ""
echo "Creating legal domain tests..."


create_file "core/legal/tests/test_models.py"

cat > core/legal/tests/test_models.py <<'EOF'
from core.legal.models.article import LegalArticle


def test_article_creation():

    article = LegalArticle(
        id=1,
        article_number="1",
        text="sample",
        legislation_id=10
    )

    assert article.article_number == "1"
EOF



echo ""
echo "Creating legal architecture ADR..."


create_file "docs/adr/ADR-004-legal-domain-architecture.md"

cat > docs/adr/ADR-004-legal-domain-architecture.md <<'EOF'
# ADR-004: Legal Domain Architecture

## Status

Accepted


## Context

ALPIP is designed for legal intelligence workflows.


## Decision

Legal capabilities will be isolated as a domain module.

The domain contains:

- Legislation
- Articles
- Documents
- Extraction services


## Benefits

- Clear legal data model
- Extensible legal plugins
- Independent processing pipelines


## Consequences

All legal features should follow domain boundaries.
EOF



echo ""
echo "Updating roadmap..."

if [ -f "docs/Master-Implementation-Roadmap.md" ]; then

cat >> docs/Master-Implementation-Roadmap.md <<'EOF'


## Pack 008 Progress

Status:

In Progress

Completed:

- Legal domain structure
- Legislation model
- Article model
- Document metadata
- PDF extraction interface
- Legal plugin foundation
- ADR-004 created

EOF

fi


echo ""
echo "Pack 008-B completed successfully."

echo ""
echo "Running Pack 008 validation..."


VALIDATION_FAILED=0


REQUIRED_DIRS=(
"core/legal"
"core/legal/models"
"core/legal/types"
"core/legal/services"
"core/legal/extractors"
"plugins/legal"
"plugins/legal/models"
"plugins/legal/services"
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
"core/legal/types/document_type.py"
"core/legal/models/legislation.py"
"core/legal/models/article.py"
"core/legal/models/document.py"
"core/legal/extractors/base.py"
"core/legal/extractors/pdf.py"
"core/legal/services/document_service.py"
"plugins/legal/plugin.py"
"core/legal/tests/test_models.py"
"docs/adr/ADR-004-legal-domain-architecture.md"
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
    echo "PACK 008 COMPLETED SUCCESSFULLY"
    echo "Legal Domain foundation is ready."
    echo "========================================="


    if [ -f "docs/Master-Implementation-Roadmap.md" ]; then

cat >> docs/Master-Implementation-Roadmap.md <<'EOF'


## Pack 008 Final Status

Status:

Completed

Delivered:

- Legal Domain Core
- Legislation Entity
- Legal Article Entity
- Document Metadata Model
- Document Extraction Pipeline Foundation
- Legal Plugin Foundation
- Legal Domain ADR

EOF

    fi


else

    echo "========================================="
    echo "PACK 008 FAILED"
    echo "Review missing items above."
    echo "========================================="

    exit 1

fi


echo ""
echo "Next commands:"
echo "git add ."
echo "git commit -m \"feat(legal): add legal domain foundation\""
echo "git push"
