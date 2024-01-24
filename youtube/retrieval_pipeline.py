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