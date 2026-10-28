# Fonts: why you see boxes, and how to fix it

The icons are **Nerd Font glyphs**. They live in the Unicode *Private Use Area*, which means
no normal font has them. If your terminal or editor uses a regular font, every icon shows as an
empty box, a `?`, or nothing at all. This is the most common problem with this package, and it is a
font problem, not a bug.

To see icons you need **two things**:

1. A **Nerd Font installed** on the machine that *displays* the text (your laptop, not the server
   you are connected to over SSH).
2. Your **terminal or editor set to use it**. Installing the font is not enough.

## 1. Check what you have

```sh
devicons --check-font
```

Every line should show an icon. If you see boxes, continue below.

## 2. Install a Nerd Font

Any font from [nerdfonts.com/font-downloads](https://www.nerdfonts.com/font-downloads) works. Use
**version 3.0 or newer**: version 2 fonts are missing the Material Design icons this package uses
(PDF, PowerPoint, Excel, C#, R, Vue and pipe files show as boxes on a v2 font).

Good defaults: **JetBrainsMono Nerd Font**, **FiraCode Nerd Font**, **Hack Nerd Font**,
**Meslo Nerd Font**.

| System | Install |
|---|---|
| macOS | `brew install --cask font-jetbrains-mono-nerd-font` |
| Arch | `sudo pacman -S ttf-jetbrains-mono-nerd` |
| Debian/Ubuntu, Fedora, other | download the zip from nerdfonts.com, unzip into `~/.local/share/fonts`, run `fc-cache -fv` |
| Windows | `winget install DEVCOM.JetBrainsMonoNerdFont`, or download, select the `.ttf` files, right-click, *Install* |

Which variant? Every download has `Nerd Font`, `Nerd Font Mono` and `Nerd Font Propo`:

- **`Nerd Font Mono`**: icons are forced to one cell wide. Best for terminals, nothing overlaps.
- **`Nerd Font`** (default): icons may be wider than a cell. Looks bigger, can overlap the next character.
- **`Nerd Font Propo`**: proportional, for editors and UIs that are not monospaced.

## 3. Tell your terminal or editor to use it

The font family name usually ends in `Nerd Font` or `NF`, for example `JetBrainsMono Nerd Font Mono`.

| App | Where |
|---|---|
| iTerm2 | Settings → Profiles → Text → Font (turn off *Use a different font for non-ASCII text* or set it to the Nerd Font too) |
| macOS Terminal | Settings → Profiles → Text → Font |
| Windows Terminal | Settings → Profiles → Defaults → Appearance → Font face |
| VS Code (integrated terminal) | `"terminal.integrated.fontFamily": "JetBrainsMono Nerd Font Mono"` |
| VS Code (editor) | `"editor.fontFamily": "JetBrainsMono Nerd Font, monospace"` |
| Alacritty | `[font.normal] family = "JetBrainsMono Nerd Font Mono"` |
| kitty | `font_family JetBrainsMono Nerd Font Mono` |
| WezTerm | `config.font = wezterm.font("JetBrainsMono Nerd Font Mono")` |
| GNOME Terminal | Preferences → your profile → Text → Custom font |

Restart the terminal afterwards, then run `devicons --check-font` again.

## Already have a font you love?

You do not have to switch. Keep your normal font and let the terminal fall back to a symbols-only font:

- Install **Symbols Nerd Font Mono** (it ships with the Nerd Fonts releases, `NerdFontsSymbolsOnly.zip`).
- kitty and WezTerm fall back to it automatically. In other terminals add it as the fallback or
  non-ASCII font (iTerm2: *Use a different font for non-ASCII text*).

## Which glyph sets are used

All of these are included in every Nerd Font 3.x:

| Set | Range | Used for |
|---|---|---|
| Seti-UI + Custom | U+E5FA–U+E6B8 | most languages and config files |
| Devicons | U+E700–U+E7C5 | JavaScript, Python, databases, tools |
| Font Awesome | U+F000–U+F2E0 | generic files, archives, media, folders |
| Font Awesome Extension | U+E200–U+E2A9 | a few extras |
| Octicons | U+F400–U+F532 | git and GitHub |
| Material Design | U+F0001–U+F1AF0 | PDF, Office, C#, R, Vue, pipes |

## Still not working?

- **Over SSH or in a container:** the font must be installed where you are *looking*, not on the remote machine.
- **tmux / screen:** run `export LANG=en_US.UTF-8` and make sure the terminal outside tmux already shows icons.
- **Some icons work, some are boxes:** your font is Nerd Fonts 2.x. Update to 3.x.
- **Icons look cut off or overlap:** switch to the `Nerd Font Mono` variant, or add a space after the icon.
- **GitHub, browsers, chat apps, PDFs:** these do not use your terminal font, so the icons will not render there
  even though they are in the text.
