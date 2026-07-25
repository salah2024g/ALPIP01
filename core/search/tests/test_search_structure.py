from pathlib import Path


def test_search_structure_exists():
    required = [
        "core/search/models",
        "core/search/indexer",
        "core/search/query",
        "core/search/services",
    ]

    for item in required:
        assert Path(item).exists()


def test_search_models_exist():
    assert Path("core/search/models/document.py").exists()
    assert Path("core/search/models/query.py").exists()
