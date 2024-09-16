from pathlib import Path

# Path to the root of the project
ROOT_FOL = Path(__file__).parents[3]
STATIC_FOL = ROOT_FOL / "static"
CACHE_FOL = ROOT_FOL / "cache"
MAPS_CACHE_FOL = CACHE_FOL / "maps"
FIND_PLACE_CACHE_FOL = MAPS_CACHE_FOL / "find_place"
