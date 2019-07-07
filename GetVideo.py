from requests_html import HTMLSession
import urllib.request
import os

def CreateName(url):
    spl=[]
    spl=url.split('/')
    return spl[len(spl)-1]


url="https://www.hepsiburada.com/apple-iphone-xs-max-64-gb-apple-turkiye-garantili-pm-HB00000E8OSQ"

##Create File
tpath="./Web Crawler/"
if not os.path.exists(tpath):
    os.mkdir(tpath)
newpath = tpath +"Video/"
if not os.path.exists(newpath):
    os.mkdir(newpath)


session = HTMLSession()
r = session.get(url)

aboutvideo = r.html.find('video')

if (aboutvideo != []):
    for abv in aboutvideo:
        try:
            vdo = abv.attrs['src']
            if (vdo != []):
                videoismi = CreateName(vdo)
                try:
                    print("Dowloads Video...")
                    urllib.request.urlretrieve(vdo, newpath + videoismi)
                except:
                    print('Failed to download->  ' + vdo)
        except:
            print("There is no src attrs....")
else:
    print("There is no Video")

