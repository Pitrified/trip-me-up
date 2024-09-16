from pathlib import Path

# Path to the root of the project
ROOT_FOL = Path(__file__).parents[3]

# data folders
STATIC_FOL = ROOT_FOL / "static"
DATA_FOL = ROOT_FOL / "data"

# cache folders
CACHE_FOL = ROOT_FOL / "cache"
MAPS_CACHE_FOL = CACHE_FOL / "maps"
FIND_PLACE_CACHE_FOL = MAPS_CACHE_FOL / "find_place"
PLACE_DETAILS_CACHE_FOL = MAPS_CACHE_FOL / "place_details"
