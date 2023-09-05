from textual.app import App, ComposeResult
from textual.screen import Screen
from textual.widgets import Static


class SampleScreen(Screen):

    CSS_PATH = "sample_screen.tcss"

    def compose(self) -> ComposeResult:
        yield Static("Sample Screen 1", id="sample_screen")
