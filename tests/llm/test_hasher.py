"""Test the hasher module."""

import pytest

from trip_me_up.llm.hasher import Hasher


def test_hexdigest() -> None:
    """Test the hexdigest method."""
    h = Hasher("data")
    s = h.hexdigest()
    assert isinstance(s, str)


def test_update() -> None:
    """Test the update method."""
    h = Hasher("data")
    s = h.update("new data")
    assert isinstance(s, str)


def test_hash() -> None:
    """Test the hash method."""
    s = Hasher.hash("data")
    assert isinstance(s, str)
