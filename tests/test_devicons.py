import io
from pathlib import Path

import pytest

from devicons import (
    DEFAULT_DIRECTORY_ICON,
    DEFAULT_FILE_ICON,
    DIRECTORY_NAMES,
    FILE_EXTENSIONS,
    FILE_NAMES,
    icon_for,
    icon_for_directory,
    icon_for_extension,
    icon_for_file,
)
from devicons.cli import check_font, main


def test_extension_lookup_ignores_dot_and_case():
    assert icon_for_extension("py") == icon_for_extension(".PY") == FILE_EXTENSIONS["py"]


def test_unknown_extension_gets_the_default():
    assert icon_for_extension("definitely-not-real") == DEFAULT_FILE_ICON


def test_exact_file_names_win_over_extensions():
    assert icon_for_file("package.json") == FILE_NAMES.get("package.json", icon_for_extension("json"))
    assert icon_for_file(".gitignore") == FILE_NAMES[".gitignore"]


def test_dotfiles_without_a_known_name_use_the_default():
    assert icon_for_file(".some-unknown-rc") == DEFAULT_FILE_ICON


def test_multi_dot_names_use_the_last_extension():
    assert icon_for_file("archive.tar.gz") == icon_for_extension("gz")


def test_paths_are_reduced_to_their_name():
    assert icon_for_file("some/deep/dir/main.py") == icon_for_extension("py")
    assert icon_for_file(Path("some") / "main.py") == icon_for_extension("py")


def test_directories():
    assert icon_for_directory(".git") == DIRECTORY_NAMES[".git"]
    assert icon_for_directory("whatever") == DEFAULT_DIRECTORY_ICON


def test_icon_for_checks_the_filesystem(tmp_path):
    folder = tmp_path / ".git"
    folder.mkdir()
    file = tmp_path / "main.py"
    file.write_text("")
    assert icon_for(folder) == DIRECTORY_NAMES[".git"]
    assert icon_for(file) == icon_for_extension("py")
    assert icon_for(tmp_path / "missing.py") == icon_for_extension("py")


def test_is_dir_overrides_the_filesystem():
    assert icon_for("src", is_dir=True) == DEFAULT_DIRECTORY_ICON
    assert icon_for("src", is_dir=False) == DEFAULT_FILE_ICON


@pytest.mark.parametrize("table", [FILE_EXTENSIONS, DIRECTORY_NAMES, FILE_NAMES])
def test_every_glyph_is_a_single_nerd_font_character(table):
    for name, glyph in table.items():
        assert len(glyph) == 1, name
        # Private Use Area: BMP (U+E000..U+F8FF) or Supplementary PUA-A (U+F0000..)
        assert 0xE000 <= ord(glyph) <= 0xF8FF or ord(glyph) >= 0xF0000, name


@pytest.mark.parametrize("table", [FILE_EXTENSIONS, DIRECTORY_NAMES, FILE_NAMES])
def test_no_glyph_uses_the_range_removed_in_nerd_fonts_3(table):
    for name, glyph in table.items():
        assert not 0xF500 <= ord(glyph) <= 0xFD46, name


def test_extensions_are_lowercase_without_dots():
    for extension in FILE_EXTENSIONS:
        assert extension == extension.lower() and not extension.startswith("."), extension


def test_check_font_lists_every_glyph_set():
    out = io.StringIO()
    assert check_font(out) == 0
    text = out.getvalue()
    for family in ("Seti-UI", "Devicons", "Font Awesome", "Octicons", "Material Design"):
        assert family in text


def test_cli_prints_icon_and_name(tmp_path, capsys):
    file = tmp_path / "main.py"
    file.write_text("")
    assert main([str(file)]) == 0
    assert capsys.readouterr().out == f"{icon_for_extension('py')} {file}\n"


def test_cli_reports_missing_paths(tmp_path, capsys):
    assert main([str(tmp_path / "nope")]) == 1
    assert "no such file or directory" in capsys.readouterr().err
