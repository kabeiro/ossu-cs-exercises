"""
Write a program that will prompt for a URL, read the JSON data from that URL using urllib
and then parse and extract the comment counts from the JSON data,
compute the sum of the numbers in the file.
"""
import urllib.request
import urllib.parse
import urllib.error
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

serviceurl = input('Enter location: ')
print('Retrieving', serviceurl)

uh = urllib.request.urlopen(serviceurl, context=ctx)
data = uh.read()

info = json.loads(data)
print('Comments count:', len(info["comments"]))

commentsSum = 0

for item in info["comments"]:
    commentsSum += item["count"]

print('Comments sum:', commentsSum)
