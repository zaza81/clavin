/bin/bash 

# Output nodes that have place and name keys to be further processed by python script
# Apache License, Version 2.0 http://www.apache.org/licenses/LICENSE-2.0

./osmosis --read-pbf $1 --node-key keyList="place" --node-key keyList="name" --write-xml - | python parse_places.py 

