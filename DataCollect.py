#collect data from http://aqicn.org/json-api/doc/
#you can name the city to get the real time data, there are five different way to request data based on the API
import urllib2
import json

token = "2d19a625aadb950cfe29d4640996a248d78c0d46"

#request data by city feed
city = "Beijing"
url = "https://api.waqi.info/feed/"+city+"/?token="+token+""

#request data by ip based geolocalized feed(your nearest city/station)
'''
url = "https://api.waqi.info/feed/here/?token="+token+""
'''

#request data for the nearest station from a given latitude/longitude
'''
lat = "10.3"
long = "20.7"
url = "https://api.waqi.info/feed/geo:"+lat+";"+long+"/?token="+token+""
'''

#request data for all the stations within a given latitude/longitudebounds
'''
lating = "39.379436,116.091230,40.235643,116.784382"
url = "https://api.waqi.info/map/bounds/?latlng="+lating+"&token="+token+""
'''

#request data for the station search by keyword
""
keyword = "shanghai"
url = "https://api.waqi.info/search/?token="+token+"&keyword="+keyword+""
""

f = urllib2.urlopen(url)
parsed = json.loads(f.read())
with open('data', 'w') as outfile:
    json.dump(parsed, outfile)
print json.dumps(parsed, indent=4, sort_keys=True)