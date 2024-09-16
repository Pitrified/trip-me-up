"""Utils for the package."""

from pathlib import Path


def check_create_fol(fol: Path) -> None:
    """Check if a folder exists, and create it if it does not."""
    if not fol.exists():
        fol.mkdir(parents=True)
