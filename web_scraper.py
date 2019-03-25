import requests
from bs4 import BeautifulSoup


def getAllUrl(urls):

    url = 'https://en.wikipedia.org' + urls

    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')

    linklist = set()

    for link in soup.find_all("a", href=True):
        #cut a tag down to link
        link = str(link)
        linkstart = link.find('href="') + 6
        linkend = link.find('"', linkstart)
        link = link[linkstart: linkend]

        #filter only wiki links and no general wiki pages ':'
        if (link[:5] == '/wiki') and link.find(":") == -1:
            #remove all hashes and on page links
            if link.find('#') != -1:
                link = link[:link.find('#')]
            linklist.add(link)
    return linklist

