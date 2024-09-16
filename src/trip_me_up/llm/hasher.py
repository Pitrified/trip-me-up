"""Hasher tool to hash long text and metadata."""

import hashlib
import json
from typing import Self


class Hasher:
    """Hasher tool to hash long text and metadata."""

    # the chunk size for hashing the stringified content
    chunk_size = 4096

    def __init__(self, data: str | dict) -> None:
        """Initialize the hasher tool."""
        # create a hash object
        self.hash_object = hashlib.sha256()
        # update the hash object with the data
        self.update(data)

    def update(self, data: str | dict) -> str:
        """Update the hash object with the new data.

        Return the hexadecimal representation of the hash.
        """
        # if the data is a dict, turn it to a json string
        data = self.stringify(data)
        # update the hash object with the stringified content in chunks
        for i in range(0, len(data), self.chunk_size):
            chunk = data[i : i + self.chunk_size]
            self.hash_object.update(chunk.encode("utf-8"))
        # return the hexadecimal representation of the hash
        return self.hexdigest()

    def hexdigest(self) -> str:
        """Get the hexadecimal representation of the hash."""
        return self.hash_object.hexdigest()

    @staticmethod
    def stringify(data: str | dict) -> str:
        """Stringify the data."""
        if isinstance(data, dict):
            return json.dumps(data, sort_keys=True)
        return data

    @staticmethod
    def hash(data: str | dict) -> str:
        """Hash the data."""
        hasher = Hasher(data)
        return hasher.hexdigest()
