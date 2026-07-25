from pathlib import Path


def test_repository_layout():
    required = [
        "backend",
        "core",
        "plugins",
        "tests",
        "docs",
        "samples",
    ]

    for item in required:
        assert Path(item).exists()
