# # Exchangin XML data btw 2 apps
# # using built-in xml parser in python, 'ElementTree'

# import xml.etree.ElementTree as ET

# # In xml, you get to name your tag anything unlike in html
# data = '''
# <person>
#     <name>Stone</name>
#     <phone type="intl">
#         +1 734 303 3356
#     </phone>
#     <email hide="yes"/>
# </person>
# '''
# tree = ET.fromstring(data)
# print('Name:', tree.find('name').text) # look for the 'name' tag and get its text
# print('Attr:', tree.find('email').get('hide')) #look for line that has the email tag and get its 'hide' attr 


# #example2
# input = '''
# <stuff>
#     <users>
#         <user x="2">
#             <id>001</id>
#             <name>Stone</name>
#         </user>
#         <user x="7">
#             <id>007</id>
#             <name>Chisom</name>
#         </user>
#     </users>
# </stuff>
# '''
# stuff = ET.fromstring(input) #read the xml string
# lst = stuff.findall('users/user')
# print('User count:', len(lst))

# for item in lst:
#     print('Name', item.find('name').text)
#     print('Id', item.find('id').text)
#     print('Attribute', item.get('x'))


# # Other serialization format: JavaScript Object Notation, JSON
# # Processing json with python

# import json
# data = '''
#     {
#         "name": "Stone",
#         "phone": {
#             "type": "intl",
#             "number" : "+1 734 303 4456"
#         },
#         "email" : {
#             "hide" : "yes"
#         }
#     }
# '''
# info =json.loads(data)
# print('Name:', info["name"])
# print('Hide:', info["email"]["hide"])


# #example 2
# input = '''
#     [
#         {
#             "id": "001",
#             "x": "2",
#             "name": "Chuck"
#         },
#         {
#            "id": "002",
#             "x": "4",
#             "name": "Stone" 
#         }
#     ]
# '''
# data = json.loads(input)
# print('User count:', len(data))
# for item in data:
#     print('Name', item['name'])
#     print('Id', item['id'])
#     print('Attribute', item['x'])


# Service Oriented Approach
# consuming google map api

import urllib.request, urllib.parse, urllib.error
import json

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?' #this api returns the json format blw
# {
#     "status": "OK",
#     "results": [
#         {
#             "geometry": {
#                 "location_type": "APPROXIMATE",
#                 "location": {
#                     "lat": 42.2808256,
#                     "lng": -83.7430378
#                 }
#             },
#             "address_components": [
#                 {
#                     "long_name": "Ann Arbor",
#                     "type": [
#                         "locality",
#                         "political"
#                     ],
#                     "short_name": "Ann Arbor"
#                 }
#             ],
#             "formatted_address": "Ann Arbor, MI, USA",
#             "type": [
#                 "locality",
#                 "political"
#             ]
#         }
#     ]
# }

while True:
    address = input('Enter your location: ')
    if len(address) < 1: break
    url = serviceurl + urllib.parse.urlencode({'address': address}) #the library parses the text we read from user
    
    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode() #data is now a string 
    print('Retrieved', len(data), 'characters')
    
    try: 
        js = json.loads(data)
    except:
        js = None
    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue
    lat = js['results'][0]['geometry']['location']['lat']
    lng = js['results'][0]['geometry']['location']['lng']
    print('lat', lat, 'lng', lng)
    location = js['results'][0]['formatted_address']
    print(location)



# API Security and Rate Limiting
