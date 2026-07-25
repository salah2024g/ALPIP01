from pathlib import Path


def test_plugins_directory_exists():
    assert Path("plugins").exists()


def test_plugins_is_not_empty():
    plugins = list(Path("plugins").glob("*"))
    assert len(plugins) > 0
