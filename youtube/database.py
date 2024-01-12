# # DATABASES
# #creating table and records, updating, reading and deleting records through our application.
# import sqlite3

# conn = sqlite3.connect('emaildb.sqlite')
# cur = conn.cursor()

# cur.execute('DROP TABLE IF EXISTS Counts')
# cur.execute('CREATE TABLE Counts (email TEXT, count INTEGER)')

# fname = input('Enter file name: ')
# if len(fname) < 1: fname = 'clown.txt'
# fh = open(fname)
# for line in fh:
#     if not line.startswith('From: '): continue
#     pieces = line.split()
#     email = pieces[1]
#     cur.execute('SELECT count FROM Counts WHERE email = ? ', (email,))
#     row = cur.fetchone()
#     if row is None:
#         cur.execute('INSERT INTO Counts (email, count) VALUES (?, 1)', (email,))
#     else:
#         cur.execute('UPDATE Counts SET count = count + 1 WHERE email = ?', (email,))
#     conn.commit()
    
# # https://www.sqlite.org/lang_select.html
# sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'

# for row in cur.execute(sqlstr):
#     print(str(row[0]), row[1])
# cur.close()


# Talking to twitter api and storing on a database

from urllib.request import urlopen
import urllib.error
import twurl
import json
import sqlite3
import ssl

TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

conn = sqlite3.connect('spider.sqlite')
cur = conn.cursor()

cur. execute('''
             CREATE TABLE IF NOT EXISTS Twitter (name TEXT, retrieved INTEGER, friends INTEGER)''')

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
    
    url = twurl.augment(TWITTER_URL, {'scree_name': acct, 'count': '5'})
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
        print(friend)
        cur.execute('SELECT friends FROM Twitter WHERE name = ? LIMIT 1', (friend, ))
        try:
            count =  cur.fetchone()[0]
            cur.execute('UPDATE Twitter SET friend = ? WHERE name = ?', (count+1, friend))
            countold = countold + 1
        except:
            cur.execute('''INSERT INTO Twitter (name, retrieved, friends) VALUES (?, 0, 1)''', (friend, ))
            countnew = countnew + 1
    print('New accounts=', countnew, ' revisited=', countold)
    conn.commit()
cur.close()
