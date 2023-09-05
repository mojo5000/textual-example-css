from textual.app import App, ComposeResult
from textual.screen import Screen
from textual.widgets import Static


class SampleScreen2(Screen):

    CSS_PATH = "sample_screen2.tcss"

    def compose(self) -> ComposeResult:
        yield Static("Sample Screen 2", id="sample_screen2")
