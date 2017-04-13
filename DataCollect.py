#collect data from http://aqicn.org/json-api/doc/
#you can name the city to get the real time data
import urllib2
import json

city = "Beijing"
url = "https://api.waqi.info/feed/"+city+"/?token=2d19a625aadb950cfe29d4640996a248d78c0d46"
f = urllib2.urlopen(url)
parsed = json.loads(f.read())
with open('data', 'w') as outfile:
    json.dump(parsed, outfile)
print json.dumps(parsed, indent=4, sort_keys=True)