"""
Write a program that will use urllib to read the HTML from the data files,
extract the href= vaues from the anchor tags, scan for a tag that is in a particular position 
relative to the first name in the list, follow that link and repeat the process a number of times 
and report the last name you find. 
"""

# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')
count = int(input('Enter count: '))
# the first name is 1
position = int(input('Enter position: ')) - 1
while count > 0:
    url = tags[position].get('href', None)
    print('Retrieving: ', url)
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    count -= 1
