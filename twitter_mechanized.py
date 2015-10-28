import mechanize as mc  
import cookielib
import html2text
import re
from flask import Flask,render_template

#credentials
user = ""
pwd = ""

# Browser
br = mc.Browser()

# Cookie Jar
cj = cookielib.LWPCookieJar()
br.set_cookiejar(cj)

# Browser options
br.set_handle_equiv(True)
br.set_handle_gzip(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)


# Follows refresh 0 but not hangs on refresh > 0
br.set_handle_refresh(mc._http.HTTPRefreshProcessor(), max_time=1)

br.addheaders = [('User-Agent', 'Chrome')]
# br.addheaders.append( ['Accept-Encoding','gzip'] )
br.open('https://twitter.com')

# Select the second (index 1) form to login
br.select_form(nr=1)

#Login 
for control in br.form.controls:
  if control.name == 'session[username_or_email]':
    br[control.name] = user 
  if control.name == 'session[password]':
    br[control.name] = pwd

br.submit()

#verify success
# print(bs(br.response().read()))

#Find our link
# for link in br.links():
# 	print(link)
# 	print ""

#Go to settings
url = '/settings/account'
br.find_link(url=url)
request = br.click_link(url = url)
br.open(request)

#Go to widgets
url2 = '/settings/widgets'
br.find_link(url=url2)
req2 = br.click_link(url=url2)
br.open(req2)

#Create new widget link
url3 = '/settings/widgets/new'
br.find_link(url=url3)
req3 = br.click_link(url=url3)
br.open(req3)

#Create new user timeline link
url4 = '/settings/widgets/new/user'
br.find_link(url=url4)
req4 = br.click_link(url=url4)
br.open(req4)

#find form
# for form in br.forms():
#   print form
#   print ""

#select form 3 (index 2) and test with Elon Musk
br.select_form(nr=2)
control = br.form.find_control("timeline_config[screen_name]")

for control in br.form.controls:
  if control.name == 'timeline_config[screen_name]':
    br[control.name] = 'elonmusk'

br.submit()

#extract widget_id

br.select_form(nr=2)
# print br.form.attrs['action']
widget_url = br.form.attrs['action']
temp = re.search(r'widgets/(\d+)',widget_url)
widget_id = int(temp.group(1))

href = "https://twitter.com/elonmusk"

#flask stuff for rendering template
app = Flask(__name__)

@app.route("/")
def template_test():
  return render_template('widget_render.html',l1=widget_id,l2=href)

if __name__ == '__main__':
  app.run(debug=True)