#!/usr/bin/python

import random, os.path
# Let's create a file and write it to disk.
filename = "random.kml"

# Header info for the KML
header = ('<?xml version="1.0" encoding="UTF-8"?>\n'
			'<kml xmlns="http://www.opengis.net/kml/2.2">\n'
			'<Document>\n')

FILE = open(filename,"w")
FILE.write(header)
numMarkers = int(raw_input("How many markers: "))
nLat = int(raw_input("Northern-most Latitude: "))
sLat = int(raw_input("Southern-most Latitude: "))
wLong = int(raw_input("Western-most Longitude: "))
eLong = int(raw_input("Eastern-most Longitude: "))
maxZed = int(raw_input("Maximum Z Value (meters): "))


count = 0
while (count < numMarkers):
	latitude = random.uniform(sLat,nLat) #you can go -90 to 90
	longitude = random.uniform(wLong,eLong) # you can go -180 to 180
	zed = random.uniform(0, maxZed) #extrude value
	azimuth = random.randrange(0,359) #random heading 0-359
	kml = (
	   '<Placemark>\n'
	   '<name>'), str(count), ('</name>\n' #uses the count to make an ID
			'<visibility>1</visibility>\n'
		  '<description>Tethered to the ground by a customizable tail</description>\n'
			'<Style>\n'
				'<IconStyle>\n'
		  	'<color>ff00ff00</color>\n'
		  	'<colorMode>random</colorMode>\n'
		  	'<scale>1</scale>\n'
		  	'<heading>'), str(azimuth), ('</heading>\n' #uses random azimuth for heading
		  	'<Icon>\n'
		    	'<href>http://maps.google.com/mapfiles/kml/shapes/arrow.png</href>\n' #just look at your placemarks for urls
		  	'</Icon>\n' 
				'</IconStyle>\n'
			'</Style>\n'
	   '<Point>\n'
			'<extrude>1</extrude>\n' #yes, extrude
		  '<altitudeMode>relativeToGround</altitudeMode>\n'
	   	'<coordinates>%f,%f,%d</coordinates>\n' # use %d if you just want an integer instead of a float
	   '</Point>\n'
	   '</Placemark>\n'
	   ) %(longitude, latitude, zed)
	print kml

	# Create a file object:
	# in "write" mode
	count = count + 1
	# Write all the lines at once:
	FILE.writelines(kml)

footer = ('</Document>\n'
					'</kml>')
FILE.write(footer)

print "Nice and random!"
FILE.close()