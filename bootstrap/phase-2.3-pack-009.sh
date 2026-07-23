#!/usr/bin/env bash

set -Eeuo pipefail

PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

cd "$PROJECT_ROOT"

echo "========================================="
echo "ALPIP Phase 2.3 Pack 009"
echo "Arabic NLP + Legal Search Foundation"
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
echo "Creating NLP architecture..."


NLP_DIRS=(
"core/nlp"
"core/nlp/arabic"
"core/nlp/processors"
"core/nlp/tokenizers"
"core/nlp/tests"
"core/search"
"core/search/index"
"core/search/models"
"core/search/services"
"core/search/tests"
"plugins/nlp"
"plugins/search"
)


for dir in "${NLP_DIRS[@]}"
do
    create_dir "$dir"
done



echo ""
echo "Creating package files..."


NLP_FILES=(
"core/nlp/__init__.py"
"core/nlp/arabic/__init__.py"
"core/nlp/processors/__init__.py"
"core/nlp/tokenizers/__init__.py"
"core/search/__init__.py"
"core/search/index/__init__.py"
"core/search/models/__init__.py"
"core/search/services/__init__.py"
"plugins/nlp/__init__.py"
"plugins/search/__init__.py"
)


for file in "${NLP_FILES[@]}"
do
    create_file "$file"
done



echo ""
echo "Creating Arabic text normalizer..."


create_file "core/nlp/arabic/normalizer.py"

cat > core/nlp/arabic/normalizer.py <<'EOF'
import re


class ArabicTextNormalizer:


    def normalize(
        self,
        text: str
    ) -> str:

        text = text.strip()

        text = re.sub(
            r"\s+",
            " ",
            text
        )

        return text
EOF



echo ""
echo "Creating Arabic tokenizer..."


create_file "core/nlp/tokenizers/arabic_tokenizer.py"

cat > core/nlp/tokenizers/arabic_tokenizer.py <<'EOF'
class ArabicTokenizer:


    def tokenize(
        self,
        text: str
    ) -> list:

        return text.split()
EOF



echo ""
echo "Creating search models..."


create_file "core/search/models/document_chunk.py"

cat > core/search/models/document_chunk.py <<'EOF'
from dataclasses import dataclass


@dataclass
class DocumentChunk:

    document_id: int
    content: str
    position: int
EOF



echo ""
echo "Creating search index foundation..."


create_file "core/search/index/index.py"

cat > core/search/index/index.py <<'EOF'
class SearchIndex:


    def __init__(self):

        self.documents = []


    def add(
        self,
        document
    ):

        self.documents.append(
            document
        )


    def all(self):

        return self.documents
EOF



echo ""
echo "Pack 009-A completed successfully."
echo ""
echo "Creating text processing services..."


create_file "core/nlp/processors/text_processor.py"

cat > core/nlp/processors/text_processor.py <<'EOF'
from core.nlp.arabic.normalizer import ArabicTextNormalizer
from core.nlp.tokenizers.arabic_tokenizer import ArabicTokenizer


class TextProcessor:


    def __init__(self):

        self.normalizer = ArabicTextNormalizer()
        self.tokenizer = ArabicTokenizer()


    def process(
        self,
        text: str
    ) -> dict:

        normalized = self.normalizer.normalize(
            text
        )

        tokens = self.tokenizer.tokenize(
            normalized
        )

        return {
            "text": normalized,
            "tokens": tokens
        }
EOF



echo ""
echo "Creating document chunking service..."


create_file "core/search/services/chunking.py"

cat > core/search/services/chunking.py <<'EOF'
from core.search.models.document_chunk import DocumentChunk


class DocumentChunker:


    def chunk(
        self,
        document_id: int,
        text: str,
        size: int = 200
    ):

        words = text.split()

        chunks = []

        for index in range(
            0,
            len(words),
            size
        ):

            content = " ".join(
                words[index:index + size]
            )

            chunks.append(
                DocumentChunk(
                    document_id=document_id,
                    content=content,
                    position=index
                )
            )

        return chunks
EOF



echo ""
echo "Creating search service foundation..."


create_file "core/search/services/search.py"

cat > core/search/services/search.py <<'EOF'
class SearchService:


    def __init__(
        self,
        index
    ):

        self.index = index


    def search(
        self,
        query: str
    ):

        results = []

        for document in self.index.all():

            if query in document.content:

                results.append(
                    document
                )

        return results
EOF



echo ""
echo "Creating similarity interface..."


create_file "core/search/services/similarity.py"

cat > core/search/services/similarity.py <<'EOF'
from abc import ABC, abstractmethod


class SimilarityEngine(ABC):


    @abstractmethod
    def calculate(
        self,
        first: str,
        second: str
    ) -> float:

        pass
EOF



echo ""
echo "Creating NLP plugin..."


create_file "plugins/nlp/plugin.py"

cat > plugins/nlp/plugin.py <<'EOF'
from sdk.contracts.plugin import PluginContract


class NLPPlugin(PluginContract):


    @property
    def name(self):

        return "arabic-nlp"


    def initialize(self):

        pass


    def execute(
        self,
        payload: dict
    ):

        return {
            "processed": True,
            "payload": payload
        }
EOF



echo ""
echo "Creating search plugin..."


create_file "plugins/search/plugin.py"

cat > plugins/search/plugin.py <<'EOF'
from sdk.contracts.plugin import PluginContract


class SearchPlugin(PluginContract):


    @property
    def name(self):

        return "legal-search"


    def initialize(self):

        pass


    def execute(
        self,
        payload: dict
    ):

        return {
            "search": payload
        }
EOF



echo ""
echo "Creating NLP and Search tests..."


create_file "core/nlp/tests/test_processor.py"

cat > core/nlp/tests/test_processor.py <<'EOF'
from core.nlp.processors.text_processor import TextProcessor


def test_arabic_processing():

    result = TextProcessor().process(
        "نص قانوني"
    )

    assert len(
        result["tokens"]
    ) == 2
EOF



create_file "core/search/tests/test_index.py"

cat > core/search/tests/test_index.py <<'EOF'
from core.search.index.index import SearchIndex


def test_search_index():

    index = SearchIndex()

    index.add(
        "document"
    )

    assert len(
        index.all()
    ) == 1
EOF



echo ""
echo "Creating search architecture ADR..."


create_file "docs/adr/ADR-005-search-nlp-architecture.md"

cat > docs/adr/ADR-005-search-nlp-architecture.md <<'EOF'
# ADR-005: Arabic NLP and Search Architecture

## Status

Accepted


## Context

ALPIP requires Arabic legal text understanding and retrieval.


## Decision

The platform will separate:

- Text normalization
- Tokenization
- Document chunking
- Search indexing
- Similarity engines


## Benefits

- Better legal document retrieval
- Future AI integration
- Independent NLP modules


## Consequences

All search operations must use the search layer.
EOF



echo ""
echo "Updating roadmap..."

if [ -f "docs/Master-Implementation-Roadmap.md" ]; then

cat >> docs/Master-Implementation-Roadmap.md <<'EOF'


## Pack 009 Progress

Status:

In Progress

Completed:

- Arabic text normalization
- Tokenization foundation
- Text processing pipeline
- Document chunking
- Search index foundation
- Search service
- NLP and Search plugins
- ADR-005 created

EOF

fi


echo ""
echo "Pack 009-B completed successfully."
echo ""
echo "Running Pack 009 validation..."


VALIDATION_FAILED=0


REQUIRED_DIRS=(
"core/nlp"
"core/nlp/arabic"
"core/nlp/processors"
"core/nlp/tokenizers"
"core/search"
"core/search/index"
"core/search/models"
"core/search/services"
"plugins/nlp"
"plugins/search"
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
"core/nlp/arabic/normalizer.py"
"core/nlp/tokenizers/arabic_tokenizer.py"
"core/nlp/processors/text_processor.py"
"core/search/models/document_chunk.py"
"core/search/index/index.py"
"core/search/services/chunking.py"
"core/search/services/search.py"
"core/search/services/similarity.py"
"plugins/nlp/plugin.py"
"plugins/search/plugin.py"
"core/nlp/tests/test_processor.py"
"core/search/tests/test_index.py"
"docs/adr/ADR-005-search-nlp-architecture.md"
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
    echo "PACK 009 COMPLETED SUCCESSFULLY"
    echo "Arabic NLP and Search foundation is ready."
    echo "========================================="


    if [ -f "docs/Master-Implementation-Roadmap.md" ]; then

cat >> docs/Master-Implementation-Roadmap.md <<'EOF'


## Pack 009 Final Status

Status:

Completed

Delivered:

- Arabic NLP foundation
- Text normalization
- Arabic tokenization
- Document chunking
- Search index foundation
- Search service
- Similarity interface
- NLP Plugin
- Search Plugin
- Search Architecture ADR

EOF

    fi


else

    echo "========================================="
    echo "PACK 009 FAILED"
    echo "Review missing items above."
    echo "========================================="

    exit 1

fi


echo ""
echo "Next commands:"
echo "git add ."
echo "git commit -m \"feat(nlp): add arabic nlp and search foundation\""
echo "git push"
