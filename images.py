import urllib
import urllib.request
from bs4 import BeautifulSoup
import os
from string import ascii_lowercase
i=1
def make_soup(url):
    thepage= urllib.request.urlopen(url)
    soupdata = BeautifulSoup(thepage, "html.parser")
    return soupdata
#1 Nawzaz:
##soup = make_soup("https://wikibio.in/nawazuddin-siddiqui/")
##for img in soup.findAll('img'):
##    temp=img.get('src')
##    if temp[:1]=="/":
##        image = "https://wikibio.in/nawazuddin-siddiqui/" + temp
##    else:
##        image = temp
##
##    print(image)


#2 Ayushmann:
##soup = make_soup("https://wikibio.in/ayushmann-khurrana/")
##for img in soup.findAll('img'):
##    temp=img.get('src')
##    if temp[:1]=="/":
##        image = "https://wikibio.in/ayushmann-khurrana/" + temp
##    else:
##        image = temp
##
##    print(image)

#3 RajkummarRao:
soup = make_soup("https://wikibio.in/rajkummar-rao/")
for img in soup.findAll('img'):
    temp=img.get('src')
    if temp[:1]=="/":
        image = "https://wikibio.in/rajkummar-rao/" + temp
    else:
        image = temp

    print(image)



    nametemp = img.get('alt')
    if len(nametemp)==0:
        filename=str(i)
        i=i+1
    else:
        filename=nametemp


    imagefile = open(filename + ".jpeg", 'wb')
    imagefile.write(urllib.request.urlopen(image).read())
    imagefile.close()
