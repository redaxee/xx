import cookielib
import urllib2
import mechanize

br = mechanize.Browser()
cookiejar = cookielib.LWPCookieJar()
br.set_cookiejar( cookiejar )
br.set_handle_equiv( True )
br.set_handle_gzip( True )
br.set_handle_redirect( True ) 
br.set_handle_referer( True )
br.set_handle_robots( False )

br.set_handle_refresh( mechanize._http.HTTPRefreshProcessor(), max_time = 1)
br.addheaders = [ ( 'User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1' ) ]

user = "EMAIL"
pass = "PASSWORD"
url = "https://www.facebook.com/login.php"

#Open URL and submit
br.open(url)
br.select_form(nr=0)
br.form['email'] = user
br.form['pass'] = pass
response = br.submit()

#Opens website and write source to html-output.txt
fileobj = open("HTML-OUTPUT.txt","wb")
fileobj.write(response.read())
fileobj.close()
