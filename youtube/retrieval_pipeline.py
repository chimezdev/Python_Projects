import sqlite3
import time
import ssl
import urllib.request, urllib.parse, urllib.error
from urllib.parse import urlparse
import re
from datetime import datetime, timedelta

# Not all systems have this so conditionally define parser
try:
    import dateutil.parser as parser
except:
    pass

def parsemaildate(md):
    # See if we have dateutil
    try:
        pdate = parser.parse(tdate)
        test_at = pdate.isoformat()
        return test_at
    except:
        pass

    # Non-deteutil version - we try our best
    pieces = md.split()
    notz = " ".join(pieces[:4]).strip()

    # Try a bunch of format variations - strptime() is *lame*

    dnotz = None
    for form in ['%d %b %Y %H:%M:%S', '%d %b %Y %H:%M:%S', 
        '%d %b %Y %H:%M', '%d %b %Y %H:%M', '%d %b %y %H:%M:%S', 
         '%d %b %y %H:%M:%S', '%d %b %y %H:%M', '%d %b %y %H:%M']:
        try:
            dnotz = datetime.strptime(notz, form)
            break
        except:
            continue

    if dnotz is None:
        #print ('Bad Date:', md)
        return None
    
    iso = dnotz.isoformat()

    tz = "+0000"
    try: 
        tz = pieces[4]
        ival = int(tz) # Only want numeric timezone values
        if tz == '-0000': tz = '+0000'
        tzh = tz[:3]
        tzm = tz[3:]
        tz = tzh+":"+tzm
    except:
        pass

        return iso+tz
    
#Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

conn = sqlite3.connect('content.sqlite')
cur = conn.cursor()

baseurl = "http://gmame.dr-chuck.net/gmane.comp.cms.sakai.devel/"

cur.execute('''CREATE TABLE IF NOT EXISTS Messages(id INTEGER UNIQUE, email TEXT, sent_at TEXT,
            subject TEXT, headers TEXT, body TEXT)''')

# Pick up where we left off
start = None
cur.execute('SELECT max(id) FROM Messages')
try:
    row = cur.fetchone()
    if row is None:
        start = 0
    else:
        start = row[0]
except:
    start = 0 

if start is None: start = 0

many = 0 
count = 0
fail = 0
while True:
    if(many<1):
        sval = input('How many messages:')
        if(len(sval) < 1): break
        many = int(sval)

    start = start + 1
    cur.execute('SELECT id FROM Messages WHERE id=?', (start,))
    try:
        row = cur.fetchone()
        if row is not None : continue
    except:
        row = None
        
    many = many-1
    url = baseurl + str(start) + '/' + str(start + 1)

    text = "None"
    try:
        # Open with a timeout of 30 seconds
        document = urllib.request.urlopen(url, None, 30, context=ctx)
        text = document.read().decode()
        if document.getcode() != 200:
            print("Error code=",document.getcode(), url)
            break
    except KeyboardInterrupt:
        print('')
        print('Program interrupted by user...')
        break
    except Exception as e:
        print('Unable to retrieve or parse page', url)
        print('Error', e)
        fail = fail + 1
        if fail > 5: break
        continue

    print(url, len(text))
    count = count + 1

    if not text.startswith("From "):
        print(text)
        print("Did not find From ")
        fail = fail + 1
        if fail > 5: break
        continue

    pos = text.find("\n\n")
    if pos > 0 :
        hdr = text[:pos]
        body = text[pos+2:]
    else:
        print(text)
        print("Could not find break between headers and body")
        fail = fail + 1
        if fail > 5: break
        continue

    email = None
    x = re.findall('\nFrom: .* <(\S+@\S+)>\N')

