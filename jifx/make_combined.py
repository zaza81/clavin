import time 
import sys
from datetime import datetime




f = open("JIFX_tweets_id.tsv")
f.readline()

f2 = open("GeocodedTweets_id.tsv")
f2.readline()

d = {} 
d2 = {}

for line in f:
    tid, user, userid, language, tweet, dt = line.strip().split("\t")
    # normalize the date format 
    try:
        if dt == "None":
            dt = "None"
        else:
            dt = datetime.strptime(dt, "%m/%d/%Y %H:%M")
            dt = dt.strftime("%m/%d/%Y %H:%M")
    except:
        print line
        sys.exit()

    d["%s:%s:%s" % ( user, tweet, dt )] = (tid, user, userid, language, tweet, dt)

for line in f2:
    tid, u1, u2, user, tweet, geocoded, lat, lon, dt = line.strip().split("\t")

    try:
        if dt == "None":
            dt = "None"
        else:
            dt = datetime.strptime(dt, "%m/%d/%Y %H:%M:%S")
            dt = dt.strftime("%m/%d/%Y %H:%M")
    except:
        print line 
        sys.exit()


    d2["%s:%s:%s" % ( user, tweet, dt )] = (tid, u1, u2, user, tweet, geocoded, lat, lon, dt)


#print len(d)
#print len(d2)

# go through each tweet in and see if its exists in d2 

#c = 0
#for k in d.keys():
#    if k not in d2:
        #print k
#        c += 1

#print c 


print "tid\tuser\tuserid\tlanguage\tunknown1\tunknown2\ttweet\tgeocoded\tlat\tlon\tdatetime"

c = 0
for k in d2.keys():
    if k in d:
        print d2[k][0] + "\t" + d[k][1] + "\t" + d[k][2] + "\t" + d[k][3] + "\t" + d2[k][1] + "\t" + d2[k][2] + "\t" + d2[k][4] + "\t" + d2[k][5] + "\t" + d2[k][6] + "\t" + d2[k][7] + "\t" + d2[k][8]

#print c



# 251688 tweets from JIFX not in the "geocoded" tweets
# 4520 tweets from "geocoded" tweets not in JIFX data




