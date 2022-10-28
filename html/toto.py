#!C:\Users\33659\AppData\Local\Programs\Python\Python310\python.exe

import cgi

print("Content-type: text/html\n\n")

form = cgi.FieldStorage()

username = form.getvalue("username")
print(username)