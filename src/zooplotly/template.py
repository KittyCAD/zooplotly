import json
from enum import StrEnum
from pathlib import Path

import plotly.graph_objects as go
import plotly.io as pio


class DefaultFont(StrEnum):
    OCRA = "OCRA"
    SPACE_MONO = "Space Mono"
    ROBOTO_MONO = "Roboto Mono"


def use_zoo_style(font: str = DefaultFont.OCRA) -> None:
    """
    Apply the Zoo style template to Plotly visualizations.

    This function loads a predefined Plotly template from a JSON file and applies it as
    the default template. It also allows customization of the font used in the template.

    Args:
        font (str): The font family to use in the template. Defaults to DefaultFont.OCRA.
    Returns:
        None
    """

    # Load json.
    template_path = Path(__file__).parent / "templates" / "zoo.json"
    with open(template_path) as f:
        config = json.load(f)

    # Handle font.
    config["layout"]["font_family"] = font

    template = go.layout.Template()
    template.layout = go.Layout(**config["layout"])
    pio.templates["zoo"] = template
    pio.templates.default = "zoo"
