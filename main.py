from dash import Dash
from dash_bootstrap_components.themes import BOOTSTRAP

from src.components.layout import create_layout
from src.data.sleep_data import load_sleep_data


def main() -> None:
    sleep_data = load_sleep_data()

    app = Dash(external_stylesheets=[BOOTSTRAP])
    app.title = "Health Dashboard"
    app.layout = create_layout(app, sleep_data)
    app.run()


if __name__ == "__main__":
    main()
