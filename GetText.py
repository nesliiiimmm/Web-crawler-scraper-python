from requests_html import HTMLSession

url="https://www.nesli.org/"
session=HTMLSession()
r=session.get('https://www.nesli.org/')
def recursivee(str):
    if(str[0]==' '):
        if(len(str)==1):
            return str
        else:
            return recursivee(str[1:])
    else:
        return str
LinksHtml=r.text
bool=False
deneme=''
falan=[]
Kelimeler=[]
for i in LinksHtml:
    if(i=='>'):
        bool=True
    elif(i=='<'):
        bool=False
    if(bool==True):
        if(i!=''):
                if (i != '\n'):
                    if (i != '>'):
                        if (i != '<'):
                            deneme=deneme+i
    if(bool==False):
        if(deneme!=''):
            if(deneme!='&nbsp;'):
                falan.append(deneme)
        deneme=''
#for i in falan:
#    print(i)

for i in falan:
    if(i[0]!=' '):
        #i=recursivee(i)
        #print(i)
        #if(i!=' '):
        #        Kelimeler.append(i)
        if(i[0]!='\r'):
            if(i[0]!='\t'):
                Kelimeler.append(i)
for k in Kelimeler:
    print(k)



























