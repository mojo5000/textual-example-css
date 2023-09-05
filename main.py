from textual.app import App, ComposeResult
from textual.widgets import Static
from child import Child
from sample_screen import SampleScreen
from sample_screen2 import SampleScreen2

class MyApp(App):

    CSS_PATH = "main.tcss"
    SCREENS = { "sample1": SampleScreen(), "sample2": SampleScreen2() }
    BINDINGS = [
        ("1", "push_screen('sample1')", "Sample"),
        ("2", "push_screen('sample2')", "Sample2"),
        ("u", "pop_screen()"), # KNOWN: this will err if pressed on main screen.
    ]

    def compose(self) -> ComposeResult:     
        yield Static("Stuffs before Screen")
    

if __name__ == "__main__":
    app = MyApp()
    app.run()

