"""Test the constants file."""

import pytest

from trip_me_up.config.constants import ROOT_FOL


def test_root_is_trip_me_up() -> None:
    """Test that the root folder is named 'trip-me-up'."""
    assert ROOT_FOL.name == "trip-me-up"
