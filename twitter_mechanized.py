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


# Follows refresh 0 but not hangs on refresh > 0
br.set_handle_refresh(mc._http.HTTPRefreshProcessor(), max_time=1)

br.addheaders = [('User-Agent', 'Chrome')]
# br.addheaders.append( ['Accept-Encoding','gzip'] )
br.open('https://twitter.com')


