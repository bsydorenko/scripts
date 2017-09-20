#!/usr/bin/python
import requests
#asd
#nakonec to blyat'
f = open(r'path_to_file', 'wb')
r = requests.get('link')
f.write(r.content)
f.close