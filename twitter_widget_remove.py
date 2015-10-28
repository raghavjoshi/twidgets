import mechanize as mc  
import cookielib
import html2text

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
br.set_handle_refresh(mc._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-Agent', 'Chrome')]

#open twitter (different attempt)
br.open('https://twitter.com/settings/widgets')

# Select the second (index 1) form to login
br.select_form(nr=1)

#Login 
for control in br.form.controls:
  if control.name == 'session[username_or_email]':
    br[control.name] = user 
  if control.name == 'session[password]':
    br[control.name] = pwd

br.submit()

#Find our magical form
for form in br.forms();
	print form	
	print ""

#Select the third one
br.select_form(nr=2)
control = br.form.find_control(type="submit")
br.submit()
