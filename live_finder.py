from web_scraper import *
import sys

def is_link_in_page(page_to_check, end_link):
    links_on_page = getAllUrl(page_to_check)
    if end_link in links_on_page:
        return True
    else:
        return False


start_link = "/wiki/What_the_Funny"
end_link = "/wiki/Vegetarianism"
path = [start_link]

links_on_start_page = getAllUrl(start_link)


if is_link_in_page(start_link, end_link):
        print("Found the Page 1")


for current_page in links_on_start_page:
    if is_link_in_page(current_page, end_link):
        print("Found the Page 2")
        path.append(current_page)
        print(path)
        break

for second_degree in links_on_start_page:
    for current_page in getAllUrl(second_degree):
        if is_link_in_page(current_page, end_link):
            print("Found the Page 3")
            path.append(second_degree)
            path.append(current_page)
            path.append(end_link)
            print(path)
            sys.exit()
            break


path.append(end_link)
print(path)