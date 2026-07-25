from pathlib import Path


def test_project_structure():
    assert Path("backend").exists()
    assert Path("plugins").exists()
    assert Path("core").exists()
    assert Path("docs").exists()


def test_sample_exists():
    assert Path("samples/legal_sample.aldf").exists()
