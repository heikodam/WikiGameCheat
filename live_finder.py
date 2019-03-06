from web_scraper import *

start_link = "/wiki/What_the_Funny"
end_link = "/wiki/Marlon_Wayans"

links_on_page = getAllUrl(start_link)

if end_link in links_on_page:
    print("Found Website")