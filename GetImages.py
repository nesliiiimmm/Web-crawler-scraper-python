from requests_html import HTMLSession
import urllib.request
import os


def Analysis(str,url):
   count=0
   array=str.split(' ')
   for i in array:
       if i in url:
          count=count+1
   return count


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



url="https://www.teknosa.com/huawei-mate-10-pro-128gb-kahverengi-akilli-telefon-p-125076663"
SearchTerm="huawei mate 10 pro"

##Create File
tpath="./Web Crawler/"
if not os.path.exists(tpath):
    os.mkdir(tpath)
path = tpath +"Image/"
if not os.path.exists(path):
    os.mkdir(path)
newpath=path+SearchTerm+"/"
if not os.path.exists(newpath):
    os.mkdir(newpath)

session = HTMLSession()
r = session.get(url)

aboutimg = r.html.find('img')

if (aboutimg != []):
    for abi in aboutimg:
        sayac = 0
        img = []
        try:
            alt = abi.attrs['alt']
            calt = Analysis(SearchTerm, alt)
            if (calt > sayac):
                sayac = calt
        except:
            print(" There is no alt attrs...")
        try:
            title = abi.attrs['title']
            ctitle = Analysis(SearchTerm, title)
            if (ctitle > sayac):
                sayac = ctitle
        except:
            print(" There is no title attrs...")
        try:
            img = abi.attrs['src']
            cimg = Analysis(SearchTerm, img)
            if (cimg > sayac):
                sayac = cimg
        except:
            print(" There is no image attrs...")

        if (img != []):
            resimismi = CreateName(img)
        else:
            resimismi = SearchTerm

        if (sayac > 0):
            try:
                urllib.request.urlretrieve(img, newpath + resimismi)
            except:
                try:
                    simg = CreateUrl(url, img)
                    urllib.request.urlretrieve(simg, newpath + resimismi)
                except:
                    print('Failed to download-> ' + img)
        else:
            print("Failed to match words -> " + resimismi)
else:
    print("There is no image")



