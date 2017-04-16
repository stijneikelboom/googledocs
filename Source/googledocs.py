#!/usr/bin/env python

from webbrowser import open as browser
from json import load
from sys import argv

if len(argv) > 1:
    for file in argv[1:]:
        with open(file) as f:
            data = load(f)
        browser(data['url'])
else:
    browser('https://docs.google.com/')
