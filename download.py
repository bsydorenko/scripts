#!/usr/bin/python
import requests
#asd
f = open(r'path_to_file', 'wb')
r = requests.get('link')
f.write(r.content)
f.close