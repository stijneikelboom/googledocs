#!/usr/bin/env python

import webbrowser
import json
import sys

if len(sys.argv) > 1:
    with open(sys.argv[1]) as f:
        data = json.load(f)
    url = data['url']
else:
    url = 'https://docs.google.com/'
webbrowser.open(url)
