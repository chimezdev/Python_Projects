# SOCKETS IN PYTHON
# python has built-in support for TCP Sockets

# import socket
# mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# mysock.connect( ('data.pr4e.org', 80)) #ensure that the host is up else it will throw an error.
# cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n' .encode()
# mysock.send(cmd)

# while True:
#     data = mysock.recv(512)
#     if (len(data) < 1 ):
#         break
#     print(data.decode())
# mysock.close()


# USING urllib instead of sockets (Making http easier with urllib)
# since HTTP is so common, we have a library that does all the socket(opening a connection and sending http request) work and makes web pages look like a file

import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
counts = dict()
for line in fhand:
    print(line.decode().strip())
# you can treat the web page as if it's a file that you open
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
print (counts)


# Parsing html (aka web scraping)
# Web scraping is when a program or script pretends to be a browser and retrieves web pages, look at it extracts information and then look at more web pages
# search engines scrape web pages - this is called 'spidering the web' or 'web crawling'
# Using BeautifulSoup

from bs4 import BeautifulSoup 
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx = check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
# necessary when u have a site with cert that is not in python's list of certs

url = input('Enter url: ')
html = urllib.request.urlopen(url, context=ctx).read() #oprns the url and reads the content
soup = BeautifulSoup(html, 'html.parser') # the html content is parsed and the 'BeautifulSoup' class returns object

# Retrieve all of the anchor tags
tags = soup('a') #you can do a whole lot like retrieving all anchor tags
for tag in tags:
    print(tag.get('href', None))
