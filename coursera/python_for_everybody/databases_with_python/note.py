# Lecture, Object Oriented Definitions and Terminology

##############################################################################
## Object Oriented Definitions and Terminology
###############################################
##
## Object Oriented
##
##  A program is made up of many cooperating objects
##
##  Instead of being the "whole program" - each object is a little island
##  within the program and cooperatively working with other objects.
##
##  A program is made up of one or more objects working together - obejcts
##  make use of each other's capabilities.
##
## Object
##
##  An object is a bit self-contained Code and Data
##
##  A key aspect of the Object approach is to break the problem into smaller
##  understandable part (divide and conquer)
##
##  Objects have boundaries that allow us to ignore un-needed detail
##
##  We have been using objects all along: String Objects, Integer, Dictionary
##  List......
##
## Definitions
##
##  Class - a template
##
##  Method or Message - A defined capability of a class
##
##  Field or Attribute - A bit of data in a class
##
##  Object or Instance - A particular instance of a class
##
## Class
##
##  Defines abstract characteristic of a thing, including characteristic,
##  behaviours. Class is a blueprint that describes the nature of a thing.
##
## Instance
##
##  One can have an instance of a class or particular object. The instance
##  is the actual object created at runtime.
##
## Method
##
##  An object's abilities.

x = 'abc'
type(x) # object
dir(x) # methods

##############################################################################
## Our First Class and Object
##############################

class PartyAnimal: # class is a reserved word
    x=0 # Each PartyAnimal object has a bit of data

    def party(self): # also has a bit of code
        self.x = self.x + 1
        print("So far",self.x)

an = PartyAnimal() # construct a PartyAnimal and store in var

an.party() # PartyAnimal.party(an) # Tell the object to run party() code within

## Playing with dir() and type()
##
##  The dir() commands lists capabilities
##  Ignore the ones with underscores - these are used by python itself
##  The rest are real operatation that the object can perform
##  It is like type() - it tells us something about a var

##############################################################################
## Object Life Cycle
#####################
##
## Object Lifecyle
##
##  Objects are created, used and discarded
##
##  We have special block of code that get called (constructor and destructor)
##
##  Constructor are used a lot, but the other is not
##
## Constructor
##
##  The primary purpose of the constructor is to set up some instance variables
##  to have the proper initial values when the object is created.
##
##  In object oriented programming, a constructor in a class is a special block
##  of statements called when an object is created

class PartyAnimal: # class is a reserved word

    def __init__(self):
        print("I am constructor")

    def party(self): # also has a bit of code
        self.x = self.x + 1
        print("So far",self.x)

    def __del__(self):
        print("I am destructed", self.x)

an = PartyAnimal()
an.party()
an=42 # destructed

##  Many Instance
##
##  We can create lot of objects
##
##  We can store each distinct object in its own var
##
##  We call this having multiple instances of the same class
##
##  Each instance has its own copy of the instance variables

class PartyAnimal: # class is a reserved word
    x=0
    name = ""
    def __init__(self,z):
        self.name = z
        print(self.name"I am constructor")

    def party(self): # also has a bit of code
        self.x = self.x + 1
        print(self.name,"party count",self.x)

s = PartyAnimal("Sally")
s.party()

j = PartyAnimal("Jim")
j,party()

##############################################################################
## Object Inheritance
######################
##
## Inheritance
##
##  When we make a new class - we can reuse an existing class and inherit
##  all capabilities of an existing class and then add our own
##
##  Another form of store and reuse
##
##  Write once - reuse many times
##
##  The new class (child) has all the capabilities of the old class (parent)
##  - and then some more
##
## Terminology: Inheritance
##
##  Subclasses more specialized version of a class, which inherit attibutes
##  and behaviours from their parent classes

class FootballFan(PartyAnimal): # behave like an extension
    points = 0
    def touchdown(self):
        self.points = self.points +7
        self.party()
        print(self.name, "points", self.points)

## Definitions
##
##  Class - a template
##
##  Attribute - A variable within a class
##
##  Method - A function within a class
##
##  Object - A particular instance of a class
##
##  Constructor - Code that runs when an object is created
##
##  Inheritance - The ability to extend a class to make a new class

##############################################################################
## Relational Databases
########################
##
## Relational Databases
##
##  Relational databases model data by storing rows and columns in tables.
##  The power of the relational databases lies in its ability to efficiently
##  retrieve data from those tables and in particular where there are mutliple
##  tables.
##
## Terminology
##
##  Database - contain many tables
##
##  Relation (or Table) - contains tuple and attributes
##
##  Tuple (or row) - a set of fields that generally represents an "object" like
##                   a person or a music track
##
##  Attribute (also column or field) - one of possibly many elements of data
##                                     corresponding to the object represented
##                                     by row
##
## Relation is defined as a set of tuples that have same attributes. A tuple
## usually represents an object and information about that object. Objects are
## typically physical objects or concepts. A relation is usually described as a
## table, which is organized into rows and columns.
##
## SQL
##
##  Structured Query Language is the language we use to issue commands to the
##  database.
##
##  create table / retrieve some data / insert data / delete data

##############################################################################
## Using Databases
###################
##
## Two Roles in Large Projects
##
##  Application developer - build the logic for the application, the look and
##                          feel of the application - monitors the applications
##                          for problems.
##
##  Database Administrator - Monitors and adjusts the database as the program
##                           runs in production.
##
##  Often both involves in building the data model.
##
## Database Administrator (dba)
##
##  responsible for design, implementation, maintenance, and repair of an
##  organization's database.
##
## Database model
##
##  A database model or database schema is the structure or format of a
##  database.
##
## Common Database Systems
##
##  Three majors - Oracle, MySql, SqlServer
##
##  for smaller projects, SQLite ....

##############################################################################
## Single Table CRUD
#####################
##
## SQLite Browser
##
##  popular database - free and small
##
##  direct manipulation of SQLite files is possible
##
##  plugins in Firefox or embedded in python ...
##
## Start Simple - A single table
##
## SQL Insert
##
##  The insert statement inserts a row into a table
##  INSERT INTO Users (name, email) VALUES ('NAME', 'EMAIL')
##
## SQL Delete
##
##  Deletes a row in a table based on a selection criteria
##  DELETE FROM User WHERE email='EMAIL'
##
## SQL Update
##
##  Allows the updating of a field with a where clause
##  UPDATE Users SET name = "NAME" WHERE email = "EMAIL"
##
## Retrieving Records: Select
##
##  The select statement retrieves a group of records - you can either retrieve
##  all the records or a subset of the records with a WHERE clause
##
##  SELECT * FROM Users WHERE email="EMAIL"
##
## Sorting with ORDER BY
##
##  You can add an ORDER BY clause to SELECT statements to get the results
##  sorted in ascending or descending order
##
##  SELECT * FROM Users ORDER BY name

##############################################################################
## Worked Example: Counting Email in a Database
################################################

import sqlite3

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('''
CREATE TABLE Counts (email TEXT, count INTEGER)''')

fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox-short.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split()
    email = pieces[1]
    cur.execute('SELECT count FROM Counts WHERE email = ? ', (email,))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (email, count)
                VALUES (?, 1)''', (email,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE email = ?',
                    (email,))
    conn.commit()

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()

#############################################################################
## QUIZ
########

# 1

CREATE TABLE Ages (
  name VARCHAR(128),
  age INTEGER
)

DELETE FROM Ages;
INSERT INTO Ages (name, age) VALUES ('Emily', 19);
INSERT INTO Ages (name, age) VALUES ('Fionnah', 32);
INSERT INTO Ages (name, age) VALUES ('Saraah', 37);
INSERT INTO Ages (name, age) VALUES ('Raegan', 14);
INSERT INTO Ages (name, age) VALUES ('Madison', 37);

SELECT hex(name || age) AS X FROM Ages ORDER BY X

# 2

import sqlite3

conn = sqlite3.connect('orgdb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

#cur.execute('''
#CREATE TABLE Counts (email TEXT, count INTEGER)''')

fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split('@')
    org = pieces[1]
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (org,))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count)
                VALUES (?, 1)''', (org,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',
                    (org,))
    conn.commit()

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()

# Bonus

from urllib.request import urlopen
import urllib.error
import twurl
import json
import sqlite3
import ssl

TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

conn = sqlite3.connect('spider.sqlite')
cur = conn.cursor()

cur.execute('''
            CREATE TABLE IF NOT EXISTS Twitter
            (name TEXT, retrieved INTEGER, friends INTEGER)''')

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    acct = input('Enter a Twitter account, or quit: ')
    if (acct == 'quit'): break
    if (len(acct) < 1):
        cur.execute('SELECT name FROM Twitter WHERE retrieved = 0 LIMIT 1')
        try:
            acct = cur.fetchone()[0]
        except:
            print('No unretrieved Twitter accounts found')
            continue

    url = twurl.augment(TWITTER_URL, {'screen_name': acct, 'count': '20'})
    print('Retrieving', url)
    connection = urlopen(url, context=ctx)
    data = connection.read().decode()
    headers = dict(connection.getheaders())

    print('Remaining', headers['x-rate-limit-remaining'])
    js = json.loads(data)
    # Debugging
    # print json.dumps(js, indent=4)

    cur.execute('UPDATE Twitter SET retrieved=1 WHERE name = ?', (acct, ))

    countnew = 0
    countold = 0
    for u in js['users']:
        friend = u['screen_name']
        print(friend)
        cur.execute('SELECT friends FROM Twitter WHERE name = ? LIMIT 1',
                    (friend, ))
        try:
            count = cur.fetchone()[0]
            cur.execute('UPDATE Twitter SET friends = ? WHERE name = ?',
                        (count+1, friend))
            countold = countold + 1
        except:
            cur.execute('''INSERT INTO Twitter (name, retrieved, friends)
                        VALUES (?, 0, 1)''', (friend, ))
            countnew = countnew + 1
    print('New accounts=', countnew, ' revisited=', countold)
    conn.commit()

cur.close()

Lecture, Designing a Data Model

##############################################################################
## Designing a Data Model
##########################
##
## Database Design
##
##  Database design is an art form of its own with particular skills and
##  experience
##
##  Our goal is to avoid the really bad mistakes and design clean and easily
##  understood databases.
##
## Building a Data Model
##
##  Drawing a picture of the data objects for our application and then figuring
##  out how to represent the objects and their relationships
##
##  Basic Rule: Don't put the same string data in twice - use a relationship
##              instead
##
## For each piece of info
##
##  Is the column an object or an attribute of another object?

##############################################################################
## Representing a Data Model in Tables
#######################################
##
## Primary id, foreign id, logical id

##############################################################################
## Inserting Relational Data
#############################
##
## insert into Artist (name) values ('Artist name')
##
## insert into Genre (name) values ('Rock')
##
## insert into Album (title, artist_id) value ('Name Title', 1)
##
## insert into Track (title, rating, len, count, album_id, genre_id) values (.)

##############################################################################
## Reconstructing Data with JOIN
#################################
##
## Relational Power
##
##  By removing the replicated data and replacing it with references to a
##  single copy of each bit of data we build a "web" of information that the
##  relational database can read through very quickly.
##
##  Often when you want some data it comes from a number of tables linked by
##  foreign keys.
##
## If we want tile and name
##
##  select Album.title, Artist.name from Album join Artist on Album.artist_id
##  = Artist.id
##
## Joining two tables without an ON clause gives all possible combinations of
## rows.

#############################################################################
## Worked Example: Tracks.py
#############################

import xml.etree.ElementTree as ET
import sqlite3

conn = sqlite3.connect('trackdb.sqlite')
cur = conn.cursor()

# Make some fresh tables using executescript()
cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;


CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);

CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY
        AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);
''')


fname = input('Enter file name: ')
if ( len(fname) < 1 ) : fname = 'Library.xml'

# <key>Track ID</key><integer>369</integer>
# <key>Name</key><string>Another One Bites The Dust</string>
# <key>Artist</key><string>Queen</string>
def lookup(d, key):
    found = False
    for child in d:
        if found : return child.text
        if child.tag == 'key' and child.text == key :
            found = True
    return None

stuff = ET.parse(fname)
all = stuff.findall('dict/dict/dict')
print('Dict count:', len(all))
for entry in all:
    if ( lookup(entry, 'Track ID') is None ) : continue

    name = lookup(entry, 'Name')
    artist = lookup(entry, 'Artist')
    album = lookup(entry, 'Album')
    count = lookup(entry, 'Play Count')
    rating = lookup(entry, 'Rating')
    length = lookup(entry, 'Total Time')

    if name is None or artist is None or album is None :
        continue

    print(name, artist, album, count, rating, length)

    cur.execute('''INSERT OR IGNORE INTO Artist (name)
        VALUES ( ? )''', ( artist, ) )
    cur.execute('SELECT id FROM Artist WHERE name = ? ', (artist, ))
    artist_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Album (title, artist_id)
        VALUES ( ?, ? )''', ( album, artist_id ) )
    cur.execute('SELECT id FROM Album WHERE title = ? ', (album, ))
    album_id = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Track
        (title, album_id, len, rating, count)
        VALUES ( ?, ?, ?, ?, ? )''',
        ( name, album_id, length, rating, count ) )

    conn.commit()

#############################################################################
## QUIZ
########

import xml.etree.ElementTree as ET
import sqlite3

conn = sqlite3.connect('trackdb.sqlite')
cur = conn.cursor()

# Make some fresh tables using executescript()
cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;
DROP TABLE IF EXISTS Genre;


CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);

CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY
        AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);
''')


fname = input('Enter file name: ')
if ( len(fname) < 1 ) : fname = 'Library.xml'

# <key>Track ID</key><integer>369</integer>
# <key>Name</key><string>Another One Bites The Dust</string>
# <key>Artist</key><string>Queen</string>
def lookup(d, key):
    found = False
    for child in d:
        if found : return child.text
        if child.tag == 'key' and child.text == key :
            found = True
    return None

stuff = ET.parse(fname)
all = stuff.findall('dict/dict/dict')
print('Dict count:', len(all))
for entry in all:
    if ( lookup(entry, 'Track ID') is None ) : continue

    name = lookup(entry, 'Name')
    artist = lookup(entry, 'Artist')
    genre = lookup(entry, 'Genre')
    album = lookup(entry, 'Album')
    count = lookup(entry, 'Play Count')
    rating = lookup(entry, 'Rating')
    length = lookup(entry, 'Total Time')

    if name is None or genre is None or artist is None or album is None :
        continue

    print(name, artist, album, count, rating, length)

    cur.execute('''INSERT OR IGNORE INTO Artist (name)
        VALUES ( ? )''', ( artist, ) )
    cur.execute('SELECT id FROM Artist WHERE name = ? ', (artist, ))
    artist_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Genre (name)
        VALUES ( ? )''', ( genre, ) )
    cur.execute('SELECT id FROM Genre WHERE name = ? ', (genre, ))
    genre_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Album (title, artist_id)
        VALUES ( ?, ? )''', ( album, artist_id ) )
    cur.execute('SELECT id FROM Album WHERE title = ? ', (album, ))
    album_id = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Track
        (title, album_id, genre_id, len, rating, count)
        VALUES ( ?, ?, ?, ?, ?, ? )''',
        ( name, album_id, genre_id, length, rating, count ) )

    conn.commit()
cur.close()

# Lecture, Many-to-Many Relationships

#############################################################################
## Many-to-Many Relationships
##############################
##
## Many to Many
##
##  Sometimes we need to model a relationship that is many-to-many
##
##  We need to add a "connection" table with two foreign keys
##
##  There is usually no separate primary key
##
## Start with a fresh database

CREATE TABLE User (
id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
name TEXT,
email TEXT
)

CREATE TABLE Course (
id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
title TEXT,
)

CREATE TABLE Member (
user_id INTEGER,
course_id INTEGER,
role INTEGER,
PRIMARY KEY (user_id, course_id)
)

INSERT INTO User (name, email) VALUES ... ;
INSERT INTO Course (title) VALUES ... ;

INSERT INTO MEMBER (user_id, course_id, role) VALUES ... ;

SELECT User.name, Member.role, Course.title
FROM User JOIN Member JOIN Course
ON Member.user_id = User.id AND Member.course_id = Course.id
ORDER BY Course.title, Member.role DESC, User.name

############################################################################
## Worked Example: roster.py
#############################

import json
import sqlite3

conn = sqlite3.connect('rosterdb.sqlite')
cur = conn.cursor()

# Do some setup
cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Course;

CREATE TABLE User (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name   TEXT UNIQUE
);

CREATE TABLE Course (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title  TEXT UNIQUE
);

CREATE TABLE Member (
    user_id     INTEGER,
    course_id   INTEGER,
    role        INTEGER,
    PRIMARY KEY (user_id, course_id)
)
''')

fname = input('Enter file name: ')
if len(fname) < 1:
    fname = 'roster_data_sample.json'

# [
#   [ "Charley", "si110", 1 ],
#   [ "Mea", "si110", 0 ],

str_data = open(fname).read()
json_data = json.loads(str_data)

for entry in json_data:

    name = entry[0];
    title = entry[1];

    print((name, title))

    cur.execute('''INSERT OR IGNORE INTO User (name)
        VALUES ( ? )''', ( name, ) )
    cur.execute('SELECT id FROM User WHERE name = ? ', (name, ))
    user_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Course (title)
        VALUES ( ? )''', ( title, ) )
    cur.execute('SELECT id FROM Course WHERE title = ? ', (title, ))
    course_id = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Member
        (user_id, course_id) VALUES ( ?, ? )''',
        ( user_id, course_id ) )

    conn.commit()

##############################################################################
## QUIZ
########

import json
import sqlite3

conn = sqlite3.connect('rosterdb.sqlite')
cur = conn.cursor()

# Do some setup
cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Course;

CREATE TABLE User (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name   TEXT UNIQUE
);

CREATE TABLE Course (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title  TEXT UNIQUE
);

CREATE TABLE Member (
    user_id     INTEGER,
    course_id   INTEGER,
    role        INTEGER,
    PRIMARY KEY (user_id, course_id)
)
''')

fname = input('Enter file name: ')
if len(fname) < 1:
    fname = 'roster_data.json'

# [
#   [ "Charley", "si110", 1 ],
#   [ "Mea", "si110", 0 ],

str_data = open(fname).read()
json_data = json.loads(str_data)

for entry in json_data:

    name = entry[0];
    title = entry[1];
    role = entry[2];

    print((name, title, role))

    cur.execute('''INSERT OR IGNORE INTO User (name)
        VALUES ( ? )''', ( name, ) )
    cur.execute('SELECT id FROM User WHERE name = ? ', (name, ))
    user_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Course (title)
        VALUES ( ? )''', ( title, ) )
    cur.execute('SELECT id FROM Course WHERE title = ? ', (title, ))
    course_id = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Member
        (user_id, course_id, role) VALUES ( ?, ?, ? )''',
        ( user_id, course_id, role ) )

    conn.commit()
cur.close()

SELECT User.name,Course.title, Member.role FROM
    User JOIN Member JOIN Course
    ON User.id = Member.user_id AND Member.course_id = Course.id
    ORDER BY User.name DESC, Course.title DESC, Member.role DESC LIMIT 2;

SELECT 'XYZZY' || hex(User.name || Course.title || Member.role ) AS X FROM
    User JOIN Member JOIN Course
    ON User.id = Member.user_id AND Member.course_id = Course.id
    ORDER BY X LIMIT 1;

#############################################################################
## Geocoding
#############
##
## GeoData
##
##  Makes a google map from user entered data
##
##  Use the Google Geodata API
##
##  Caches data in a database to avoid rate limiting and allow restarting
##
##  Visualized in a browser using the Google Maps API

#############################################################################
## Geocoding Visualization
###########################

#############################################################################
## Worked Example: Geodata
###########################

import urllib.request, urllib.parse, urllib.error
import http
import sqlite3
import json
import time
import ssl
import sys

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'

if api_key is False:
    api_key = 42
    serviceurl = "http://py4e-data.dr-chuck.net/json?"
else :
    serviceurl = "https://maps.googleapis.com/maps/api/geocode/json?"

# Additional detail for urllib
# http.client.HTTPConnection.debuglevel = 1

conn = sqlite3.connect('geodata.sqlite')
cur = conn.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS Locations (address TEXT, geodata TEXT)''')

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

fh = open("where.data")
count = 0
for line in fh:
    if count > 200 :
        print('Retrieved 200 locations, restart to retrieve more')
        break

    address = line.strip()
    print('')
    cur.execute("SELECT geodata FROM Locations WHERE address= ?",
        (memoryview(address.encode()), ))

    try:
        data = cur.fetchone()[0]
        print("Found in database ",address)
        continue
    except:
        pass

    parms = dict()
    parms["address"] = address
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters', data[:20].replace('\n', ' '))
    count = count + 1

    try:
        js = json.loads(data)
    except:
        print(data)  # We print in case unicode causes an error
        continue

    if 'status' not in js or (js['status'] != 'OK' and js['status'] != 'ZERO_RESULTS') :
        print('==== Failure To Retrieve ====')
        print(data)
        break

    cur.execute('''INSERT INTO Locations (address, geodata)
            VALUES ( ?, ? )''', (memoryview(address.encode()), memoryview(data.encode()) ) )
    conn.commit()
    if count % 10 == 0 :
        print('Pausing for a bit...')
        time.sleep(5)

print("Run geodump.py to read the data from the database so you can vizualize it on a map.")

# 2

import sqlite3
import json
import codecs

conn = sqlite3.connect('geodata.sqlite')
cur = conn.cursor()

cur.execute('SELECT * FROM Locations')
fhand = codecs.open('where.js', 'w', "utf-8")
fhand.write("myData = [\n")
count = 0
for row in cur :
    data = str(row[1].decode())
    try: js = json.loads(str(data))
    except: continue

    if not('status' in js and js['status'] == 'OK') : continue

    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    if lat == 0 or lng == 0 : continue
    where = js['results'][0]['formatted_address']
    where = where.replace("'", "")
    try :
        print(where, lat, lng)

        count = count + 1
        if count > 1 : fhand.write(",\n")
        output = "["+str(lat)+","+str(lng)+", '"+where+"']"
        fhand.write(output)
    except:
        continue

fhand.write("\n];\n")
cur.close()
fhand.close()
print(count, "records written to where.js")
print("Open where.html to view the data in a browser")



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
