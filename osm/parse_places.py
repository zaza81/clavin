#!/usr/bin/env python 


# Parse places from output of osmosis
# Apache License, Version 2.0 http://www.apache.org/licenses/LICENSE-2.0


from lxml.etree import XMLParser, parse , iterparse, tostring
p = XMLParser(huge_tree=True)
import sys
 
 
# write to disk 
fo = open("osm-places.tsv","w")
 
# Documentation on iterparse
# http://effbot.org/zone/element-iterparse.htm
 
context = iterparse(sys.stdin, events=("start", "end"), huge_tree=True)
context = iter(context)
event, root = context.next()
 
 
for event, elem in context:
    if event == "end" and elem.tag == "node":
        geonameid = unicode(elem.get("id"))
        modification_date = unicode(elem.get("timestamp")[:10])
        latitude = unicode(elem.get("lat"))
        longitude = unicode(elem.get("lon"))
        td = {}
        for i in elem.findall("tag"):
            if isinstance(i.get("v"), str):
                td[i.get("k")] = unicode(i.get("v"))
            else:
                td[i.get("k")] = i.get("v")
 
        an = [] 
 
        if "name:en" in td:
            name = td["name:en"]
        elif "int_name" in td:
            name = td["int_name"]
        elif "name" in td:
            name = td["name"]
        
        if "old_name" in td:
            an.append(td["old_name"])
        if "alt_name" in td:
            an.append(td["alt_name"])
        if "int_name" in td:
            an.append(td["int_name"])
        if "name:en" in td:
            an.append(td["name:en"])
        if "name" in td:
            an.append(td["name"])
 
        # remove duplicates from alternative name list 
        # and remove the current value of name
        s1 = set(an)  
    
        s1.discard(td["name"])
 
        alternatenames = u",".join(s1)
 
        if "population" in td:
            population = td["population"]
        else:
            population = u"0";
 
        rvals = [ geonameid, name, u'', alternatenames, latitude, longitude, u'', u'', u'', u'', u'', u'', u'', u'', population, u'', u'', u'', modification_date]
 
        outline = u"\t".join(rvals) + u"\n"
        
        fo.write(outline.encode("utf8"))
        
        # free up memory
        root.clear()
