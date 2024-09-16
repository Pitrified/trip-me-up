# Trip me up

## Description

This is a simple application that allows users to plan trips based on a Google Maps list of places.

## Installation

```bash
poetry install
```

## Code structure

1. Get the list of places from Google Maps
    * use Google takeout
    * use Google Maps API?
    * scrape the page?
1. Get the place ids for each place
1. Get the place details for each place
    * Name
    * Address
    * Neighborhood
    * City
1. Compute the distance between each pair of neighborhoods
1. Plan the trip
1. Chat with the user to get feedback

## Google takeout

1. Go to the [Google takeout page](https://takeout.google.com/settings/takeout?pli=1)
1. Select "Save" ("Salvato" in Italian)
1. Download the csv files
