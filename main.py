from dash import Dash
from dash_bootstrap_components.themes import BOOTSTRAP

from src.components.layout import create_layout
from src.data.sleep_data import load_sleep_data

sleep_data = load_sleep_data()

app = Dash(
    __name__,
    use_pages=True,
    external_stylesheets=[BOOTSTRAP],
    suppress_callback_exceptions=True,
    meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}],
)

app.title = "Health Dashboard"
app.layout = create_layout()


if __name__ == "__main__":
    app.run_server(
        debug=True,
        #    host="0.0.0.0",
        #    port=8080
    )
