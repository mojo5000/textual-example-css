from textual.app import ComposeResult
from textual.widgets import Static, Label

class Child(Static):

    CSS_PATH = "child.tcss"

    def compose(self) -> ComposeResult:
        yield Label("Foo")
