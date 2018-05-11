#! /usr/bin/python

import cgi

form = cgi.FieldStorage()
message = form.getvalue("message", "(no message)")

# call another script


print message 

