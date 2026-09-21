"""Shared logic used by the CLI and web API."""


def shout(text: str) -> str:
    """Add an exclamation point to text, or return a blank-input message."""
    if not text:
        return "Nothing to shout!"
    return f"{text}!"