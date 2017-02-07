import sys


f = open("GeocodedTweets.tsv")
f.readline()

print "id\tUnknown1\tUnknown2\tUserName\tTweet\tGeocoded\tLat\tLong\tDateTime"
i = 0
for line in f:
    i += 1
    print str(i) + "\t" + line,


