from pathlib import Path


def test_reference_engine_exists():
    base = Path("core/legal_reference")

    assert base.exists()
    assert (base / "engine.py").exists()
    assert (base / "graph.py").exists()
    assert (base / "index.py").exists()
    assert (base / "parser").is_dir()
    assert (base / "models").is_dir()
