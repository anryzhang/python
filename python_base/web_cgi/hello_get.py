# coding:utf-8

import  cgi, cgitb

form =  cgi.FieldStorage()

site_name = form.getvalue('name')
site_url = form.getvalue('url')

print 'Content-type:text/html'
print
print '<html>'
print '<header>'
print '<meta charset=\"utf-8\">'
print '<title>我的小网站</title>'
print '</header>'
print '<body>'

print '<h2>%s  %s</h2>' %(site_name,site_url)

print '</body>'

print '</html>'
