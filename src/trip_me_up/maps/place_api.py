"""Places API wrapper."""

from dataclasses import dataclass
from typing import Any

from loguru import logger as lg

from trip_me_up.config.constants import FIND_PLACE_CACHE_FOL, PLACE_DETAILS_CACHE_FOL
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
        data = req_get_cached(
            url_find_place,
            FIND_PLACE_CACHE_FOL,
            validator=self.is_place_id_resp_valid,
        )
        # extract the place_id if it exists
        candidates = data["candidates"]
        if len(candidates) == 0:
            return None
        place_id = candidates[0]["place_id"]
        return place_id

    @staticmethod
    def is_place_id_resp_valid(data: Any) -> bool:
        """Check if the response from the Google Places API is valid."""
        match data["status"]:
            case "OK":
                return True
            case "ZERO_RESULTS":
                lg.warning(f"No results found. {data}")
                return True
            case _:
                lg.warning(f"Status not OK. {data}")
                return False


@dataclass
class PlaceDetailsFields:
    """Fields for the PlaceDetails object."""

    # basic fields
    address_components: bool = False
    adr_address: bool = False
    business_status: bool = False
    formatted_address: bool = False
    geometry: bool = False
    icon: bool = False
    icon_mask_base_uri: bool = False
    icon_background_color: bool = False
    name: bool = False
    photo: bool = False
    place_id: bool = True
    plus_code: bool = False
    types: bool = False
    url: bool = False
    utc_offset: bool = False
    vicinity: bool = False
    wheelchair_accessible_entrance: bool = False

    # contact fields
    current_opening_hours: bool = False
    formatted_phone_number: bool = False
    international_phone_number: bool = False
    opening_hours: bool = False
    secondary_opening_hours: bool = False
    website: bool = False

    # atmosphere fields
    curbside_pickup: bool = False
    delivery: bool = False
    dine_in: bool = False
    editorial_summary: bool = False
    price_level: bool = False
    rating: bool = False
    reservable: bool = False
    reviews: bool = False
    serves_beer: bool = False
    serves_breakfast: bool = False
    serves_brunch: bool = False
    serves_dinner: bool = False
    serves_lunch: bool = False
    serves_vegetarian_food: bool = False
    serves_wine: bool = False
    takeout: bool = False
    user_ratings_total: bool = False

    def get_fields(self) -> str:
        """Get the fields, formatted for the PlaceDetails object."""
        active_fields = []
        for field in self.__dataclass_fields__:
            if getattr(self, field):
                active_fields.append(field)
        if len(active_fields) == 0:
            return ""
        fields = "&fields=" + "%2C".join(active_fields)
        return fields


class PlaceDetails:
    """Get place details using the Google Places API.

    https://developers.google.com/maps/documentation/places/web-service/details
    """

    url_place_details_tmpl = (
        "https://maps.googleapis.com/maps/api/place/details/json"
        "?place_id={place_id}"
        "{fields}"
        "&language=en"
        "&key={api_key}"
    )

    def __init__(self, api_key) -> None:
        """Initialize the PlaceDetails object."""
        self.api_key = api_key

    def get_place_details(self, place_id: str, fields: PlaceDetailsFields) -> Any:
        """Get place details using the Google Places API."""
        # build the URL
        fields_str = fields.get_fields()
        url_place_details = self.url_place_details_tmpl.format(
            place_id=place_id,
            fields=fields_str,
            api_key=self.api_key,
        )
        # get the data
        data = req_get_cached(
            url_place_details,
            PLACE_DETAILS_CACHE_FOL,
            validator=self.is_place_details_resp_valid,
        )
        return data

    @staticmethod
    def is_place_details_resp_valid(data: Any) -> bool:
        """Check if the response from the Google Places API is valid."""
        match data["status"]:
            case "OK":
                return True
            case "ZERO_RESULTS":
                lg.warning(f"No results found. {data}")
                return True
            case _:
                lg.warning(f"Status not OK. {data}")
                return False
