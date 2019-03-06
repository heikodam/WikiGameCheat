import requests
from bs4 import BeautifulSoup


def getAllUrl(urls):

    url = 'https://en.wikipedia.org' + urls

    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')

    linklist = []
    differentlinklist = []

    for link in soup.find_all("a", href=True):

        #cut a tag down to link
        link = str(link)
        linkstart = link.find('href="') + 6
        linkend = link.find('"', linkstart)
        link = link[linkstart: linkend]

        #filter only wiki links and no general wiki pages ':'
        if (link[:5] == '/wiki') and link.find(":") == -1:
            if link.find('#') != -1:
                link = link[:link.find('#')]
            if link not in linklist and link != urls:
                linklist.append(link)           
        elif (link[:5] == '/wiki') and link.find(":"):
            differentlinklist.append(link)
    return linklist

#go into first link
#get all links from that link
#add all links that are not yet in the database to the database
#connect those pages with the known liked pages
#go to second page


# ll, dll = getAllUrl("/wiki/Main_Page")


# for i in ll:
#     print(i)

# if "/wiki/Sochi" in ll:
#     print("Found Sochi")

# print(len(ll))