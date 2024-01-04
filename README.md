# Textual Dad Joke

## Introduction

This library provides a widget that displays a dad joke. No, I'm not even
kidding.

## Installing

The package can be installed with `pip` or related tools, for example:

```sh
$ pip install textual-dad-joke
```

## Then what?

Import it as you would any other widget from a library:

```python
from textual_data_joke import DadJoke
```

and then compose the `DadJoke` widget into your application as you would any
other widget.

The widget has a `tell` method if you want it to tell another joke. It'll
also swallow any errors but will post a `DadJoke.FellFlat` message if there
was an error.

## Erm... okay. Anything else I should know?

The widget needs an internet connection and is using
[icanhazdadjoke.com](https://icanhazdadjoke.com/) as the backend. Also, I
won't be held responsible for the content of any joke served. That's all on
you.


[//]: # (README.md ends here)
