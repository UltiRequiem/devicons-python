# devicons

[![CI](https://github.com/UltiRequiem/devicons-python/actions/workflows/ci.yaml/badge.svg)](https://github.com/UltiRequiem/devicons-python/actions/workflows/ci.yaml)
[![PyPI](https://img.shields.io/pypi/v/devicons)](https://pypi.org/project/devicons/)
[![Python](https://img.shields.io/pypi/pyversions/devicons)](https://pypi.org/project/devicons/)
[![License](https://img.shields.io/github/license/UltiRequiem/devicons-python)](./LICENSE)

File and folder icons for the terminal, as [Nerd Font](https://www.nerdfonts.com) glyphs. Give it a path, get
back the one-character icon for it: Python for `.py`, a git logo for `.git`, a book for `README.md`.

Zero dependencies, fully typed, Python 3.9+.

> [!IMPORTANT]
> **The icons only show up if your terminal uses a Nerd Font.** With a normal font you get empty boxes. This is
> the number one question about this package, so it has its own page: **[docs/fonts.md](./docs/fonts.md)**.
> Run `devicons --check-font` to test your setup in ten seconds.

## Install

```sh
pip install devicons
```

## Use it

```python
from devicons import icon_for

print(icon_for("main.py"), "main.py")
print(icon_for("Dockerfile"), "Dockerfile")
print(icon_for(".git"), ".git")  # directories are detected on disk
print(icon_for("src", is_dir=True), "src")
```

Build your own `ls`:

```python
from pathlib import Path
from devicons import icon_for

for entry in sorted(Path(".").iterdir()):
    print(f"{icon_for(entry)} {entry.name}")
```

### Command line

```sh
devicons                 # the current directory, with icons
devicons src README.md   # specific paths
devicons --check-font    # test that your font shows the icons
python -m devicons       # same thing
```

## API

| Function | Returns the icon for |
|---|---|
| `icon_for(path, *, is_dir=None)` | any path. `is_dir=None` asks the filesystem; a path that does not exist counts as a file |
| `icon_for_file(name)` | a file: exact name first (`Makefile`, `.gitignore`), then extension, then a default |
| `icon_for_directory(name)` | a directory name (`.git`, `Documents`), else a generic folder |
| `icon_for_extension(ext)` | an extension, with or without the dot, any case (`"py"`, `".PY"`) |

Unknown names get `DEFAULT_FILE_ICON` / `DEFAULT_DIRECTORY_ICON`, so you always get a character back.
Lookups use only the name, so `some/deep/dir/main.py` works, and `archive.tar.gz` is treated as `gz`.

The raw tables are public if you want to extend them: `FILE_EXTENSIONS`, `FILE_NAMES` and `DIRECTORY_NAMES`
(`dict[str, str]`). Each entry in `src/devicons/_tables.py` has the Nerd Font glyph name in a comment.

## Contributing

```sh
uv sync
uv run pytest
uv run ruff check . && uv run ruff format --check .
```

To add an icon, find its glyph name on the [Nerd Fonts cheat sheet](https://www.nerdfonts.com/cheat-sheet)
and add one line to the right table in `src/devicons/_tables.py`. The tests check that every glyph is a single
Private Use Area character from Nerd Fonts 3.

## Credits

The mapping from file types to icons comes from [vim-devicons](https://github.com/ryanoasis/vim-devicons)
(MIT, Ryan L McIntyre), updated to Nerd Fonts 3 codepoints. Glyphs by [Nerd Fonts](https://www.nerdfonts.com).

## License

MIT, see [LICENSE](./LICENSE).
