# Lecture, Networked Technology

##################################################
## Networked Technology
####################################
##
## Transport control protocol (TCP)
##
##	Built on top of IP (Internet Protocol)
## 	Assume IP might lose some data - store and retransmits data if it seems to be lost
## 	Handles "flow control" using a transmit window
## 	Provides a nice reliable pipe
## 	We call communcations between two applications
##
## Sockets | TCP connections
##
##	socket is an endpoint of a bidirectional inter-process communication flow across an Internet
##
## TCP Port Numbers
##
##	A port is an application specific or process-specific software communications endpoint
## 	It allows multiple networked applications to coexist on the same server.## 	There is a list of well-known TCP port numbers
##	Analogy to telephone number
##
## Common TCP Port
##
##	HTTP (80)
##
## For all operation, it is simple. We need three line of python

import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org",80))

##################################################
## Hypertext Transfer Protocol (HTTP)
######################################
##
## Application Protocol
##
##  Since TCP gives us a reliable socket, what do we want to do with the socket? What problem do you want to solve?
##  Application protocols
##      Mail
##      World Wide Web
##
## HTTP - Hypertext Transfer Protocol
##
##  The dominant Application Layer Protocol on the Internet
##  Invented for the Web - to Retrieve HTML, Images, Documents, etc
##  Extended to be data in addition to documents - RSS, Web Services, etc.. Basic Concept - Make a Connection - Request a document - Retrive the document - Close the Connection.
##
## What is Protocol?
##
##  A set of rules that all parties follow so we can predict each other's behaviour
##  And not bump into each other
##
## Getting Data From The Server
##
##  Each the user clicks on anchor tag with an href= value to switch to a new page.
##  The browser makes a connection to the web server and issue a "GET" request - to GET the content of the page at the specified URL
##  The server returns the HTML document to the Browser which formats and displays the document to the user.
##
## Internet Standards
##
##  The standards for all of the Internet protocols (inner workings) are developed by an organization.
##  Internet Engineering Task Force (IETF)
##  Standards are Request for Comments (RFCs)
##
## Making an HTTP request
##  Connect to server, request a document
##  e.g. GET https://host/document
## telnet data.pr4e.org 80 in command line
##
## An HTTP request in python

import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(("data.pr4e.org",80))
cmd = 'GET https://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    print(data.decode())

mysock.close()

##################################################
## Worked Example: Sockets
###########################

import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(("data.pr4e.org",80))
cmd = 'GET https://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode() # if not work use above code
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    print(data.decode())

mysock.close()

##################################################
## Using the Developer Console to Explore HTTP
###############################################

##################################################
## QUIZ
########

import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')

mysock.close()

# Lecture, Unicode Characters and Strings

##################################################
## Unicode Characters and Strings
##################################
##
## ASCII
##
##  American Standard Code for Information Interchange
##
## Representing Simple String
##
##  Each character is represented by a number between 0 and 256 stored in 8 bits of memory
##  We refer to "8 bits of memory as a "byte" of memory
##  The ord() function tells us the numeric value of a simple ASCII character
##
## Multi-Byte Character
##
##  To represent the wide range of characters computers must handle we represent characters with more than one byte
##  UTF-16 - Fixed length - Two bytes
##  UTF-32 - Fixed length - Four bytes
##  UTF-8 - 1-4 bytes
##      Upwards compatible with ASCII
##      Automatic detection between ASCII and UTF-8
##      UTF-8 is recommended practice for encoding data to be exchanged between systems
##
## Two kinds of Strings in Python
##
##  In python 3, all strings are unicode
##
## Python 3 and Unicode
##
##  In python 3, all strings internally are UNICODE
##  Working with string variables in Python programs and reading data from files usually "just works"
##  When we talk to a network resource using sockets or talk to a database we have to encode and decode data (usually to UTF-8)
##
## Python Strings to Bytes
##
##  When we talk to an external resource like a network socket we sends bytes, so we need to encode Python 3 strings into a given character encoding
##  When we read data from an external resource, we must decode it based on the character set so it is properly represented in Python 3 sting as

while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    mystring = data.decode()
    print(mystring)

##################################################
## Retrieving Web Pages
########################
##
## Using urllib in Python
##
##  Since HTTP is so common, we have a library that does all the socket work for us and amkes web pages look like a file

import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen("http://data.pr4e.org/romeo.txt")
for line in fhand:
    print(line.decode().strip())

## Like a file

counts = dict()
for line in fhand:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word,0) + 1
print(counts)

##################################################
## Worked Example: Using Urllib
################################

import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen("http://data.pr4e.org/romeo.txt")
for line in fhand:
    print(line.decode().strip())

# or

counts = dict()
for line in fhand:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
print(counts)

##################################################
## Parsing Web Pages
#####################
##
## What is Web Scraping?
##
##  When a program or script pretends to be a browser and retrieves web pages,
##  look at those webpages, extract information, and then look at more webpages.
##
##  Search engine scrape web pages - we call this "web crawling"
##
## Why Scrape?
##
##  Pull data - paricularly
##  Get your own data back out of some system that has no "export capability"
##  Monitor a site for new information
##  Spider the web to make a database for a search engine.
##
## Scrapping Web Pages
##
##  There is some controversy about web page scraping and some sites are a bit snippy about it
##  Republishing and copyrighted information is not allowed
##  Violating terms of service is not allowed
##
## The Easy Way - Beautiful Soup
##
##  You could do string searches the hard way or use BeautifulSoup

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input("Enter")
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

tags = soup('a')
for tag in tags:
    print(tag.get('href',None))

## Summary
##
##  The TCP/IP gives us pipes/sockets between applications
##  We designed application protocols to make use of these pipes
##  HyperText Transfer Protocol (HTTP) is a simple yet powerful protocol
##  Python has good support for sockets, HTTP, and HTML parsing

##################################################
## Worked Example: BeautifulSoup
#################################

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore ssl cert

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter -')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# retrieve all anchor tag

tags = soup('a')
for tag in tags:
    print(tag.get('href',None))

##################################################
## QUIZ
########

#1

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter -')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

tags = soup('span')
tagl = [int(str(tag.contents[0])) for tag in tags]
count = len(tagl)
s= sum(tagl)

print("Count: ",count,"\nSum: ",s)

#2

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = None
pos = 18
for i in range(int(input("How many times?"))+1):

    if url is None:
        url = input('Enter -')
    else:
        pass

    print(url.split("_")[-1][:-5])

    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    tags = soup('a')
    url = [str(tag.get('href',None)) for tag in tags][pos-1]

# Lecture, Data on the web

##################################################
## Data On the Web
###################
##
##  Web service add a layer of formalism on top of urllib, html and such
##
##  With the HTTP Request/Response well understood and well supported, there
##  was a natural move toward exchanging data between programs using these
##  protocols
##
##  We needed to come up with an agreed way to represent data going between
##  applications and across networks
##
##  There are two commonly used formats: XML and JSON
##
## Sending data across the "Net"
##
##  Python dictionary -> Network (wire protocol) -> Java Hashmap
##
## Agreeing on a "Wire Format"
##
##  Python dictionary -> Serialize <person> <name> .... </name> </person> ->
##  Deserialize
##
##  Two serialization is XML or JSON
##
## XML
##
##  Marking up data to send across the network

##################################################
## eXtensible Markup Language
##############################
##
## XML elements or Nodes

#<people> - start tag
#    <person>
#     <name>XXX</name> - end tag
#     <phone type="intl"> - Attribute
#        12345 - text content
#     <\phone>
#     <email hide="yes"/> - Self closing Tag
#    </person>

#    ....

#</people>

## eXtensible Markup Language
##
##  Primary purpose is to help information systems shared structural data
##
##  It started as a simplified subset of the Standard Generalized Markup
##  Language (SGML), and is designed to be relatively human-legible
##
## White Space
##
##  Line ends do not matter. White space is generally discarded on text
##  elements. We indent only to be readable.
##
## XML Terminology
##
##  Tags indicate the beginning and ending of elements
##  Attributes - Keyword/value pairs on the opening tag of XML
##  Serialize/De-Serialize - Convert data in one program into a common format
##                           that can be stored and/or transmitted between
##                           systems in a programming language-independent
##                           manner.
##
## XML as a tree
##
##  Outer doument as a top node of a tree
##
## XML as a path

##################################################
## XML Schema
##############
##
## XML Schema
##
##  Description of the legal format of an XML document
##
##  Expressed in terms of constraints on the structure and content of documents
##
##  Often used to specify a "contract" between systems
##
##  If a particular piece of XML meets the specification of the Schema - it
##  is said to "validate"
##
## Many XML Schema Languages
##
##  Document Type Definition (DTD)
##  Standard Generalized Markup Language
##  XML Schema from W3C (XSD)
##
## XSD XML Schema (W3C spec)
##
##  World Wide Web Consortium (W3C) version
##  It is often called W3C schema
##  More commonly XSD as the file ends in .xsd
##
## XSD Data Types
##
##  It is common to represent time in UTC/GMT, given that servers are often
##  scattered around the world
##
## ISO 8601 Data/Time Format
##
##  Year-month-day/time of day/timezone

##################################################
## Parsing XML
###############

import xml.etree.ElementTree as ET
data = '''
<person>
    <name>Chuck/<name>
    <phone type="intl">
        + 1 734 303 4456
    </phone>
    <email hide="yes"/>
 </person>
 '''

 tree = ET.fromstring(data)
 print("Name:", tree.find('name').text)
 print("Attr:", tree.find('email').get('hide'))

##################################################
## Worked Example: XML
#######################

import xml.etree.ElementTree as ET

input = '''
<stuff>
    <users>
        <user x="2">
            <id>001</id>
            <name>Ch</name>
        </user>
        <user x="7">
            <id>009</id>
            <name>Br</name>
        </user>
    </users>
</stuff>'''

stuff = ET.fromstring(input)
lst = stuff.findall('users/user')
print('User count:', len(lst))

for item in lst:
    print("Name:", item.find("name").text)
    print("ID:", item.find("id").text)
    print("Attribute:", item.get("x"))

##################################################
## QUIZ
########

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import xml.etree.ElementTree as ET

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter -')
html = urllib.request.urlopen(url, context=ctx)
data = html.read().decode()

print("Retrieved", len(data), "characters")

tree = ET.fromstring(data)
numbers = tree.findall('.//count')
print('Count:', len(numbers))

count = 0
for item in numbers:
    count += int(item.text)
print("Sum:", count)

# Lecture, JavaScript Object Notation (JSON)

##################################################
## JavaScript Object Notation (JSON)
#####################################
##
## JavaScript Object Notation (JSON)
##
##  Object literal notation in JavaScript discovered by Douglas Crockford
##
##  JSON represents data as nested "lists" and "dictionaries"
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
