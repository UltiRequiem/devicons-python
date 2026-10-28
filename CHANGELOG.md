# Changelog

## 0.2.0

First real release. The 0.1.0 on PyPI was only the raw tables.

- `icon_for`, `icon_for_file`, `icon_for_directory`, `icon_for_extension` with sensible fallbacks.
- `devicons` command and `devicons --check-font` to test your font.
- Typed (`py.typed`), zero dependencies, Python 3.9+.
- Tables renamed `FILE_EXTENSIONS`, `FILE_NAMES`, `DIRECTORY_NAMES` (the old `file_node_extensions`,
  `file_node_exact_matches` and `dir_node_exact_matches` names are gone).
- Glyphs moved to Nerd Fonts 3 codepoints: the old Material Design range (`U+F500`–`U+FD46`) no longer exists, which made
  `.pdf`, `.pptx`, `.xlsx`, `.cs`, `.r`, `.vue` and `fifo` show as boxes on current fonts. `.ml` now uses a font glyph instead of `λ`.
- Removed vim-devicons' own test fixtures from the tables.
- Documentation, including a guide to getting fonts working ([docs/fonts.md](./docs/fonts.md)).
