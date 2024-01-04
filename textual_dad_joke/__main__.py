"""Example application for the library."""

##############################################################################
# Textual imports.
from textual.app import App, ComposeResult
from textual.widgets import Footer

##############################################################################
# Local imports.
from textual_dad_joke import DadJoke


##############################################################################
class DadJokeApp(App[None]):
    """Example DadJoke widget application."""

    CSS = """
    Screen {
        layout: grid;
        grid-size: 2;
    }

    DadJoke {
        border: round cornflowerblue;
    }
    """

    BINDINGS = [
        ("space", "refresh", "Refresh the jokes"),
    ]

    def compose(self) -> ComposeResult:
        """Compose the application."""
        for _ in range(4):
            yield DadJoke()
        yield Footer()

    def action_refresh(self) -> None:
        """Refresh the jokes."""
        for joke in self.query(DadJoke).results():
            joke.tell()


##############################################################################
if __name__ == "__main__":
    DadJokeApp().run()

### __main__.py ends here
