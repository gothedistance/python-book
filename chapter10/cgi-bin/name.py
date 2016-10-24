#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cgi

html_body = """
<html>
<body>
<p>あなたのお名前は <span style="font-size:48px"> %s </span>さんです！</p>
</body></html>
"""

form = cgi.FieldStorage()

print("Content-type: text/html")
print(html_body % form['name'].value)
