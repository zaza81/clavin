# JIFX Experiment 2013-Aug-05



## Data Pre-Prep 

Get access to twitter data

Conversion to TSV 
   
Use LibreOffice and export as CSV using tab as a delimeter, and no formatting for text.

Generate unique ids for datasets

    python make_geo_ids.py > GeocodedTweets_id.tsv
	python make_tweet_ids.py > JIFX_tweets_id.tsv

Create a combined dataset

	make_combined.py
	

## Analysis

Install R-Studio
Install ggplot2 package 

Load data 

    tweets <- read.delim("JIFX_tweets_id.tsv")


Create bar chart of language counts 

    ggplot(data=tweets, aes(x=Language)) + geom_bar(stat="bin") + ggtitle("JIFX - Twitter Language Counts")


Generated Plot 

https://raw.github.com/Berico-Technologies/CLAVIN-contrib/master/jifx/jifx_twitter_language_counts.png


Create bar chart for combined language counts.

	library(scales)
	ggplot(data=ctweets, aes(x=language)) + geom_bar(stat="bin") + ggtitle("JIFX - Combined Twitter Language Counts") + scale_y_continuous(labels = comma)


Geotag tweets of combined database

	cd tweet
	# open src/main/java/com/berico/tweet/App.java and modify the IndexDirectory location and tweets location
	mvn package
    java -Xms512M -Xmx2048M -jar target/tweet-exp-0.1.0-RELEASE.jar > ../jifx_tweets_combined_geoparsed.tsv

This will add extra columns named "res_name", "res_lat", "res_lon" which stand for the
resolved locations in the tweet. If no locations where resolved, an empty string is used for
the values.
















