"""Tools for caching requests."""

import json
from pathlib import Path
from typing import Any

import requests

from trip_me_up.llm.hasher import Hasher
from trip_me_up.utils import check_create_fol


def req_get_cached(
    url: str,
    cache_fol: Path,
    cache_fn: str | None = None,
    force_update: bool = False,
) -> Any:
    """Get the content of a URL as json, caching it."""
    # create the cache folder if it does not exist
    check_create_fol(cache_fol)
    # build a file name if one is not provided
    if cache_fn is None:
        cache_fn = Hasher.hash(url)
    # build the cache file path
    cache_fp = cache_fol / f"{cache_fn}.json"
    # return the cached content if it exists
    if not force_update and cache_fp.exists():
        return json.loads(cache_fp.read_text())
    # fetch the content
    response = requests.get(url)
    # check the status code
    response.raise_for_status()
    # get the json content
    data = response.json()
    # cache the content
    cache_fp.write_text(json.dumps(data, indent=2))
    return data
