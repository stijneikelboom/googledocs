#!/usr/bin/env python3

import webbrowser
import json
import sys

file = sys.stdin.readline().rstrip()
if file:
    with open(file, encoding='utf-8') as f:
        data = json.load(f)
    url = data['url']
else:
    url = 'https://docs.google.com/'
webbrowser.open(url)
