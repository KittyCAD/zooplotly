import math

import plotly.graph_objects as go

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


def generate_default_ocra_plot():
    template.use_zoo_style()
    fig = generate_plot()
    fig.write_image("tests/reference_images/test_default_ocra_plot.png")


def generate_space_mono_plot():
    template.use_zoo_style(font="Space Mono")
    fig = generate_plot()
    fig.write_image("tests/reference_images/test_space_mono_plot.png")


def generate_roboto_mono_plot():
    template.use_zoo_style(font="Roboto Mono")
    fig = generate_plot()
    fig.write_image("tests/reference_images/test_roboto_mono_plot.png")


if __name__ == "__main__":
    generate_default_ocra_plot()
    generate_space_mono_plot()
    generate_roboto_mono_plot()
