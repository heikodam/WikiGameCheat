from web_scraper import *

def is_link_in_page(page_to_check, end_link):
    links_on_page = getAllUrl(page_to_check)
    if end_link in links_on_page:
        return True
    else:
        return False


start_link = "/wiki/What_the_Funny"
end_link = "/wiki/Tha_Truth,_Pt._2"
path = [start_link]

links_on_start_page = getAllUrl(start_link)


if is_link_in_page(start_link, end_link):
        print("Found the Page")


for current_page in links_on_start_page:
    if is_link_in_page(current_page, end_link):
        print("Found the Page")
        path.append(current_page)
        break

path.append(end_link)
print(path)