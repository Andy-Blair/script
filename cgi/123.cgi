#!D:\Python27\python.exe
import cgitb; cgitb.enable()
import cgi
import os
import urllib
import re
import IIS_WebList
form = cgi.FieldStorage()
name = form.getvalue('name','world')
list = os.listdir('d:\\py')
path = 'd:\\py'
displaypath = cgi.escape(urllib.unquote(path))
web_list = IIS_WebList.weblist
print """Content-type: text/html

<html>
<head>
<title>Greeting Page</title>
</head>
<body>
<h1>Hello, %s!</h1>
<form action = '123.cgi'>
Change name <input type='text' name='name' />
<input type='submit' />
<hr>
%s
<hr>
""" % (name,web_list)
for names in list:
    fullname = os.path.join(path, name)
    colorName = displayname = linkname = names
    # Append / for directories or @ for symbolic links
    if os.path.isdir(fullname):
        colorName = '<span style="background-color: #CEFFCE;">' + names + '/</span>'
        displayname = names
        linkname = names + "/"
    if os.path.islink(fullname):
        colorName = '<span style="background-color: #FFBFFF;">' + names + '@</span>'
        displayname = names
        # Note: a link to a directory displays with @ and links with /
    filename =displaypath + '\\' + displayname
    print """<table><tr><td width="60%%"><a href="%s">%s</a></td><td width="20%%">%s</td></tr></table>
	""" % (urllib.quote(linkname), colorName,os.path.getsize(filename))
"""
</form>
</body>
</html>
"""