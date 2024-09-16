"""Utils for the requests module."""

from urllib import parse


def escape_input_text(input_text: str) -> str:
    """Escape input text for URL."""
    return parse.quote(input_text)
