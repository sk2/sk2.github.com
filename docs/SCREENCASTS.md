# CLI Screencasts with VHS

To improve the website's "Show, Don't Tell" philosophy, we use **[vhs](https://github.com/charmbracelet/vhs)** to create automated, high-quality terminal GIFs.

**Implementation Status:** Demo tape files created and moved to project repositories (e.g., `network-simulator/demos/`). Rendering requires VHS in a compatible environment (Linux or Docker recommended for macOS).

## Why VHS?
- **Scriptable**: Write terminal interactions in a `.tape` file.
- **Reproducible**: Regenerate GIFs whenever the CLI output changes.
- **Polished**: Built-in support for window themes, padding, and font styling.

## Installation
```bash
brew install vhs
# or
docker pull charmcli/vhs
```

## Creating a Tape File
Create a file named `demo.tape`:
```tape
# Set up the window
Set FontSize 22
Set Width 1200
Set Height 600
Set Padding 20
Set Theme "Catppuccin Frappe"

# Type commands
Type "netsim --version"
Sleep 500ms
Enter

Sleep 1s

Type "netsim run --topology spine-leaf.yaml"
Sleep 500ms
Enter

# Wait for output
Sleep 5s
```

## Rendering
Run the command to generate the GIF:
```bash
vhs demo.tape -o assets/images/netsim-demo.gif
```

## Integration
Once rendered, add it to the project page in the `## Visuals` or `## Screenshots` section:
```markdown
![Netsim Demo](../assets/images/netsim-demo.gif)
```
