import sys


f = open("JIFX_Tweets.tsv")
f.readline()

print "id\tUser\tUserID\tLanguage\tTweet\tDate"
i = 0
for line in f:
    i += 1
    print str(i) + "\t" + line,


