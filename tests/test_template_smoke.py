from pathlib import Path


def test_template_core_files_exist():
    root = Path(__file__).parents[1]
    for name in ("README.md", "build.toml", "requirements-dev.txt", ".gitattributes", ".env.example"):
        assert (root / name).is_file()
