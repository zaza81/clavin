package com.berico.tweet;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

import org.apache.lucene.queryparser.classic.ParseException;

import com.berico.clavin.GeoParser;
import com.berico.clavin.GeoParserFactory;
import com.berico.clavin.resolver.ResolvedLocation;

/**
 * Experimental Twitter Processor for CLAVIN
 * You will need to modify the IndexDirectory location and tweets location
 */
public class App 
{
    public static void main( String[] args ) throws Exception
    {
    	
    	GeoParser parser = GeoParserFactory.getDefault("/Users/tpinney/project/CLAVIN/IndexDirectory");  	
    	BufferedReader br = new BufferedReader(new FileReader("/Users/tpinney/project/CLAVIN-contrib/jifx/jifx_tweets_combined.tsv"));
    	String line;
    	
    	// skip header 
    	br.readLine();
    	
    	// print the header for the new file 
    	System.out.println("tid\tuser\tuserid\tlanguage\tunknown1\tunknown2\ttweet\tgeocoded\tlat\tlon\tdatetime\tres_name\tres_lat\tres_lon");

    	while ((line = br.readLine()) != null) {
    		String[] sl = line.split("\t");
    		String lang = sl[3];
    		String tweet = sl[6];
    		
    		// only handle english tweets for now    		
    		if (lang.equals("en") ) { 
    			// process the tweet with CLAVIN
    			// this will need to be optimized to deal with the twitter format 
    
    			List<ResolvedLocation> resolvedLocations = parser.parse(tweet);
    			
    			// take the first location for now, should be able to handle multiple 
    			// multiple locations in a tweet 	
    			String name = "";
    			String latitude = "";
    			String longitude = "";
    			if (resolvedLocations.size() > 0) {
    				name = resolvedLocations.get(0).geoname.name;
    				latitude = Double.toString(resolvedLocations.get(0).geoname.latitude);
    				longitude = Double.toString(resolvedLocations.get(0).geoname.longitude);
    			}
    			
    			System.out.println(line + "\t" + name + "\t" + latitude + "\t" + longitude);
    		
    		} else {
    			
    			System.out.println(line + "\t\t\t");
    		}
    			
    		
    		
    		
    		
    	}
    		
    	br.close();
        
        
        
    }
}
