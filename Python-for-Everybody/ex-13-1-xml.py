"""
Write a program that will prompt for a URL, read the XML data from that URL using urllib
and then parse and extract the comment counts from the XML data, compute the sum of the numbers in the file. 
"""

import urllib.request
import urllib.parse
import urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

serviceurl = input('Enter location: ')
print('Retrieving', serviceurl)

uh = urllib.request.urlopen(serviceurl, context=ctx)
data = uh.read()
tree = ET.fromstring(data)

print('Retrieved', len(data), 'characters')

results = tree.findall('.//count')
resultCount = 0

for result in results:
    resultCount += int(result.text)

print('Count:', len(results))
print('Sum:', resultCount)
