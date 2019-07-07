from requests_html import HTMLSession
import urllib.request
import os

def CreateName(url):
    spl=[]
    spl=url.split('/')
    return spl[len(spl)-1]


def CreateUrl(url,WrongUrl):

    word = CreateName(url)
    num = len(url) - len(word)
    final = url[:num]
    ret = final + WrongUrl
    return ret



url="https://scholar.google.com.tr/scholar?q=kar%C4%B1nca+kolonisi+algoritmas%C4%B1&hl=tr&as_sdt=0&as_vis=1&oi=scholart"

#CreateFile
tpath="./Web Crawler/"
if not os.path.exists(tpath):
    os.mkdir(tpath)
newpath = tpath +"Pdf/"
if not os.path.exists(newpath):
    os.mkdir(newpath)


session = HTMLSession()
r = session.get(url)

aboutHref = r.html.find('a')

if (aboutHref != []):
    for abp in aboutHref:
        try:
            href = abp.attrs['href']
            if (href != []):
                if (href[len(href) - 4:] == '.pdf'):
                    pdfname = CreateName(href)

                    try:
                        urllib.request.urlretrieve(href, newpath + pdfname)
                    except:
                        try:
                            spdf = CreateUrl(url, href)
                            print("Dowloads..->"+spdf)
                            urllib.request.urlretrieve(spdf, newpath + pdfname)
                        except:
                            print('Failed to download-> ' + spdf)
        except:
            print(" There is no href attrs...")
else:
    print("There is no Link or Pdf")
