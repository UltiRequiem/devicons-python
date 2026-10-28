"""File and folder icons for the terminal, as Nerd Font glyphs.

>>> from devicons import icon_for
>>> icon_for("main.py")
'\\ue606'

The glyphs only render when your terminal or editor uses a Nerd Font, see
https://github.com/UltiRequiem/devicons-python/blob/main/docs/fonts.md
"""

from __future__ import annotations

import os
from pathlib import PurePath

from ._tables import DIRECTORY_NAMES, FILE_EXTENSIONS, FILE_NAMES

__all__ = [
    "DEFAULT_DIRECTORY_ICON",
    "DEFAULT_FILE_ICON",
    "DIRECTORY_NAMES",
    "FILE_EXTENSIONS",
    "FILE_NAMES",
    "icon_for",
    "icon_for_directory",
    "icon_for_extension",
    "icon_for_file",
]

__version__ = "0.2.0"

DEFAULT_FILE_ICON = ""  # fa-file
DEFAULT_DIRECTORY_ICON = ""  # custom-folder


def icon_for_extension(extension: str) -> str:
    """Icon for a file extension, with or without the leading dot, case-insensitive.

    Returns the default file icon for unknown extensions.
    """
    return FILE_EXTENSIONS.get(extension.lstrip(".").lower(), DEFAULT_FILE_ICON)


def icon_for_file(name: str | os.PathLike[str]) -> str:
    """Icon for a file, by its name (`Makefile`, `.gitignore`) and then by its extension."""
    base = PurePath(os.fspath(name)).name
    icon = FILE_NAMES.get(base) or FILE_NAMES.get(base.lower())
    if icon:
        return icon
    # `.bashrc` has no extension for pathlib, and `archive.tar.gz` is a `gz`
    _, dot, extension = base.rpartition(".")
    if not dot or not _:
        return DEFAULT_FILE_ICON
    return icon_for_extension(extension)


def icon_for_directory(name: str | os.PathLike[str]) -> str:
    """Icon for a directory, by its name (`.git`, `Documents`)."""
    base = PurePath(os.fspath(name)).name
    return DIRECTORY_NAMES.get(base) or DIRECTORY_NAMES.get(base.lower()) or DEFAULT_DIRECTORY_ICON


def icon_for(path: str | os.PathLike[str], *, is_dir: bool | None = None) -> str:
    """Icon for a path.

    `is_dir` says whether it is a directory. When omitted the filesystem is checked,
    so a path that does not exist is treated as a file.
    """
    if is_dir is None:
        is_dir = os.path.isdir(path)
    return icon_for_directory(path) if is_dir else icon_for_file(path)
