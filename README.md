# Zooplotly

A packaged Plotly template and some associated (hacky) font tooling that provides consistent Zoo-brand styling for Plotly plots.

The repo includes a custom template with engineering-appropriate defaults, and a font installation script **appropriate for Linux systems only**.

Color ordering is derived from the [Ordnance Survey GeoDataViz-Toolkit](https://github.com/OrdnanceSurvey/GeoDataViz-Toolkit/blob/master/Colours/GDV%20colour%20palettes%200.7.pdf).


## Font installation

Before you can use the package, you will need to either manually install the required fonts or use the supplied bash script. The package will use the OCR-A font by default, but you can specify a different system font if you wish.

### Manual installation

Download and install each of the following:
- OCR-A: https://raw.githubusercontent.com/opensourcedesign/fonts/master/OCR/OCRA.otf
- Space Mono: https://raw.githubusercontent.com/google/fonts/main/ofl/spacemono/SpaceMono-Regular.ttf
- Roboto Mono: https://raw.githubusercontent.com/googlefonts/RobotoMono/main/fonts/ttf/RobotoMono-Regular.ttf

### Scripted installation

**For Linux systems only:** to install the default fonts, first download `install_fonts.sh` from the `scripts` directory, then run:

```bash
chmod +x install_fonts.sh
./install_fonts.sh
```

This will download and install the three default fonts to your system.


## Package installation

We recommend usage of [uv](https://docs.astral.sh/uv/). With uv installed, you can install the package with:

```bash
uv add git+ssh://git@github.com/KittyCAD/zooplotly.git
```

If you wish to install with HTTPS rather than SSH, you will need to configure a [.netrc](https://everything.curl.dev/usingcurl/netrc) file or include your user and password in the URL.

See: https://docs.astral.sh/uv/configuration/authentication/#git-authentication for more information.

## Usage

### Basic usage
Basic usage with the default style is straightforward. Import the package and call `use_zoo_style` to apply the Zoo-brand style to your plot; no additional configuration is necessary.

```python
from zooplotly import template

template.use_zoo_style()
```

### Changing font
Note that the package will use the OCR-A font by default. To use one of the other default fonts:
```python
template.use_zoo_style(font="Roboto Mono")
```

### Custom fonts
You should be able to use the `use_zoo_style` function to apply any font that is installed on your system. If you have a custom font that you would like to use, you can specify the font name as an argument to the function.
```python
template.use_zoo_style(
    font="Acme"
)
```

### Example

```python
import plotly.graph_objects as go
from zooplotly import template

# Apply the Zoo style.
template.use_zoo_style()

# Create a simple plot.
fig = go.Figure()
fig.add_trace(go.Scatter(x=[1, 2, 3], y=[1, 2, 3], name="data"))

# Update layout with titles.
fig.update_layout(
    title="Plot Title",
    xaxis_title="X Label",
    yaxis_title="Y Label"
)

# Save or display the plot.
fig.write_image("plot.png")  

```

## Testing

The package uses `pytest-mpl` for visual regression testing. Tests can be run
using the makefile:
```bash
make run-tests
```

Which is a simple wrapper around `uv` and `pytest`:
```bash
uv run pytest
```

To generate new baseline images for the visual regression tests, run:
```bash
make generate-reference-images
```