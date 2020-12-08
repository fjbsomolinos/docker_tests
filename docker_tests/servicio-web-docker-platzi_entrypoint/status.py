#!/usr/bin/env python

import requests
import sys

host = "localhost:8000"

if len(sys.argv) > 1:
    hito = sys.argv[1]
else:
    hito = None

if hito == None:
    r=requests.get('http://'+host+'/status')
else:
    r=requests.get('http://'+host+'/one/'+hito)

print(r.status_code, "\n", r.text)
