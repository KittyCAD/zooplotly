import math
from pathlib import Path
from typing import Optional

import numpy as np
import plotly.graph_objects as go
from PIL import Image

from zooplotly import template


def generate_plot() -> go.Figure:
    x = [i for i in range(360)]
    y_sin = [math.sin(math.radians(val)) for val in x]
    y_cos = [math.cos(math.radians(val)) for val in x]
    y_tan = [math.tan(math.radians(val)) for val in x]

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y_sin, name="sin(x)"))
    fig.add_trace(go.Scatter(x=x, y=y_cos, name="cos(x)"))
    fig.add_trace(go.Scatter(x=x, y=y_tan, name="tan(x)"))

    fig.update_layout(
        xaxis_title="Angle [deg]",
        yaxis_title="Value [-]",
        title="Trig Functions",
        xaxis_range=[0, 360],
        yaxis_range=[-1, 1],
    )
    return fig


def compare_images(
    test_image: np.ndarray, ref_image: np.ndarray, threshold: float = 0.01
) -> tuple[bool, Optional[float]]:
    """
    Compare two images and return if they're similar enough.

    Args:
        test_image: Generated test image array
        ref_image: Reference image array
        threshold: Maximum allowed average pixel difference (0-1 range)

    Returns:
        Tuple of (is_similar, difference)
        If images are different shapes, returns (False, None)
    """
    if test_image.shape != ref_image.shape:
        return False, None

    diff = np.abs(test_image.astype(float) - ref_image.astype(float)) / 255.0
    avg_diff = np.mean(diff)

    return bool(avg_diff <= threshold), float(avg_diff)


def test_default_ocra_plot(tmp_path: Path):
    template.use_zoo_style()
    fig = generate_plot()

    # Generate test image in temporary directory
    test_image_path = tmp_path / "test_default_ocra_plot.png"
    fig.write_image(str(test_image_path))

    # Load and compare images
    ref_image_path = Path("tests/reference_images/test_default_ocra_plot.png")
    test_img = np.array(Image.open(test_image_path))
    ref_img = np.array(Image.open(ref_image_path))

    is_similar, diff = compare_images(test_img, ref_img)
    assert is_similar, f"Plot images don't match (difference: {diff:.4f})"


def test_space_mono_plot(tmp_path: Path):
    template.use_zoo_style(font="Space Mono")
    fig = generate_plot()

    test_image_path = tmp_path / "test_space_mono_plot.png"
    fig.write_image(str(test_image_path))

    ref_image_path = Path("tests/reference_images/test_space_mono_plot.png")
    test_img = np.array(Image.open(test_image_path))
    ref_img = np.array(Image.open(ref_image_path))

    is_similar, diff = compare_images(test_img, ref_img)
    assert is_similar, f"Plot images don't match (difference: {diff:.4f})"


def test_roboto_mono_plot(tmp_path: Path):
    template.use_zoo_style(font="Roboto Mono")
    fig = generate_plot()

    test_image_path = tmp_path / "test_roboto_mono_plot.png"
    fig.write_image(str(test_image_path))

    ref_image_path = Path("tests/reference_images/test_roboto_mono_plot.png")
    test_img = np.array(Image.open(test_image_path))
    ref_img = np.array(Image.open(ref_image_path))

    is_similar, diff = compare_images(test_img, ref_img)
    assert is_similar, f"Plot images don't match (difference: {diff:.4f})"
