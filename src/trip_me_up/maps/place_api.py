"""Places API wrapper."""

from typing import Any

from trip_me_up.config.constants import FIND_PLACE_CACHE_FOL
from trip_me_up.reqs.cached import req_get_cached
from trip_me_up.reqs.utils import escape_input_text


class FindPlace:
    """Find place using the Google Places API.

    https://developers.google.com/maps/documentation/places/web-service/search-find-place
    """

    url_find_place_tmpl = (
        "https://maps.googleapis.com/maps/api/place/findplacefromtext/json"
        "?fields=formatted_address%2Cname%2Cplace_id"
        "&input={input_text}"
        "&inputtype=textquery"
        "&key={api_key}"
    )

    def __init__(self, api_key) -> None:
        """Initialize the FindPlace object."""
        self.api_key = api_key

    def find_place_id(self, place_description: str) -> str | None:
        """Find places using the Google Places API."""
        # build the URL
        place_description_clean = escape_input_text(place_description)
        url_find_place = self.url_find_place_tmpl.format(
            input_text=place_description_clean,
            api_key=self.api_key,
        )
        # get the data
        data = req_get_cached(url_find_place, FIND_PLACE_CACHE_FOL)
        # extract the place_id if it exists
        candidates = data["candidates"]
        if len(candidates) == 0:
            return None
        place_id = candidates[0]["place_id"]
        return place_id
