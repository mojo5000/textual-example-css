from textual.app import App, ComposeResult
from textual.widgets import Static
from child import Child

class MyApp(App):

    CSS_PATH = "main.tcss"

    def compose(self) -> ComposeResult:
        yield Static(id="bar")
        yield Child()
        yield Child()
        yield Child()


if __name__ == "__main__":
    app = MyApp()
    app.run()
