from web_scraper import *

def is_link_in_page(page_to_check, end_link):
    links_on_page = getAllUrl(page_to_check)
    if end_link in links_on_page:
        return True
    else:
        return False

start_link = "/wiki/What_the_Funny"
end_link = "/wiki/Marlon_Wayans"

print(is_link_in_page(start_link, end_link))


    