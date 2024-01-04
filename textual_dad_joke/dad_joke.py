"""Provides a dad joke widget."""

from __future__ import annotations

##############################################################################
# Python imports.
from dataclasses import dataclass
from urllib.error import URLError
from urllib.request import Request, urlopen

##############################################################################
# Textual imports.
from textual import work
from textual.app import RenderResult
from textual.events import Mount
from textual.message import Message
from textual.reactive import reactive
from textual.widget import Widget


##############################################################################
class DadJoke(Widget):
    """A widget that displays a dad joke."""

    DEFAULT_CSS = """
    DadJoke {
        width: 1fr;
        height: 1fr;
        text-align: center;
    }
    """

    _the_joke: reactive[str] = reactive("I don't get it!")
    """The joke."""

    def render(self) -> RenderResult:
        """Render the joke."""
        return self._the_joke

    def _set_the_joke(self, new_joke: str) -> None:
        """Set the new joke.

        Args:
            new_joke: The new joke.

        This is a helper function for `tell`, allowing the joke to be set
        from within the thread.
        """
        self._the_joke = new_joke

    @property
    def the_joke(self) -> str:
        """The current joke."""
        return self._the_joke

    @dataclass
    class FellFlat(Message):
        """Message posted if there was an error getting the joke."""

        telling: "DadJoke"
        """The joke that was being told."""

        because: Exception
        """The reason the joke fell flat."""

        @property
        def control(self) -> DadJoke:
            """The control that posted the message."""
            return self.telling

    @work(thread=True, exclusive=True)
    def tell(self) -> None:
        """Tell another dad joke."""
        try:
            request = Request("https://icanhazdadjoke.com/")
            request.add_header("User-Agent", "textual-dad-joke")
            request.add_header("Accept", "text/plain")
            with urlopen(request) as result:
                self.app.call_from_thread(
                    self._set_the_joke, result.read().decode("utf-8")
                )
        except URLError as error:
            self.post_message(self.FellFlat(self, error))

    def _on_mount(self, event: Mount) -> None:
        """Tell a joke when we're mounted."""
        del event
        self.tell()


### dad_joke.py ends here
