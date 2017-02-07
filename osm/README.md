# OpenStreetMap utilties

## Prerequisites

libxml2
libxslt
lxml 

osmosis 0.43 : http://bretth.dev.openstreetmap.org/osmosis-build/osmosis-0.43-RELEASE.zip


## Usage 

osmosis must be in PATH  

    sh extract_places.sh district-of-columbia-latest.osm.pbf

This will extract to osm-places.tsv 


## Future work 

Roads and Buildings

## Caveats 

Geonames.org is a richer dataset and should most likely be used over the 
default extraction setings. This script is meant to be  used as a base to 
work with OSM or OSM-like data and be customized to pull more data 
(e.g. Hospital names) for specific use cases.

 
## Debugging 

Try outputing from xml to pbf 

    osmosis --read-pbf ~/Downloads/planet-latest.osm.pbf --write-xml -

If this works try using the filter

    osmosis --read-pbf ~/Downloads/planet-latest.osm.pbf --node-key keyList="place" --node-key keyList="name" --write-xml -

Next step is to use the full script 

osmosis --read-pbf ~/Downloads/planet-latest.osm.pbf --node-key keyList="place" --node-key keyList="name" --write-xml - | python parse_places.py










