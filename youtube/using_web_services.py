# Exchangin XML data btw 2 apps
# using built-in xml parser in python, 'ElementTree'

import xml.etree.ElementTree as ET

# In xml, you get to name your tag anything unlike in html
data = '''
<person>
    <name>Stone</name>
    <phone type="intl">
        +1 734 303 3356
    </phone>
    <email hide="yes"/>
</person>
'''
tree = ET.fromstring(data)
print('Name:', tree.find('name').text) # look for the 'name' tag and get its text
print('Attr:', tree.find('email').get('hide')) #look for line that has the email tag and get its 'hide' attr 


#example2
input = '''
<stuff>
    <users>
        <user x="2">
            <id>001</id>
            <name>Stone</name>
        </user>
        <user x="7">
            <id>007</id>
            <name>Chisom</name>
        </user>
    </users>
</stuff>
'''
stuff = ET.fromstring(input) #read the xml string
lst = stuff.findall('users/user')
print('User count:', len(lst))

for item in lst:
    print('Name', item.find('name').text)
    print('Id', item.find('id').text)
    print('Attribute', item.get('x'))


# XML Schema
