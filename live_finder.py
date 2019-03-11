import web_scraper
import sys

def is_link_in_page(page_to_check, end_link):
    links_on_page = web_scraper.getAllUrl(page_to_check)
    if end_link in links_on_page:
        return True
    else:
        return False


start_link = "/wiki/By-product"
end_link = "/wiki/Electric_motor"
path = [start_link]

links_on_start_page = web_scraper.getAllUrl(start_link)


if is_link_in_page(start_link, end_link):
        print("Found the Page 1")
        path.append(end_link)
        print(path)
        sys.exit()


for current_page in links_on_start_page:
    if is_link_in_page(current_page, end_link):
        print("Found the Page 2")
        path.append(current_page)
        path.append(end_link)
        print(path)
        sys.exit()
        break

for second_degree in links_on_start_page:
    for current_page in web_scraper.getAllUrl(second_degree):
        if is_link_in_page(current_page, end_link):
            print("Found the Page 3")
            path.append(second_degree)
            path.append(current_page)
            path.append(end_link)
            print(path)
            sys.exit()
            break

for second_degree in links_on_start_page:
    for third_degree in web_scraper.getAllUrl(second_degree):
        for current_page in web_scraper.getAllUrl(third_degree):
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



#Heiko kann nicht coden, weil er seine Taskleiste nicht ausblendet!!!
#Heiko kann nicht coden, weil er seine Taskleiste nicht ausblendet!!!
#Heiko kann nicht coden, weil er seine Taskleiste nicht ausblendet!!!
#Heiko kann nicht coden, weil er seine Taskleiste nicht ausblendet!!!
#Heiko kann nicht coden, weil er seine Taskleiste nicht ausblendet!!!
#Heiko kann nicht coden, weil er seine Taskleiste nicht ausblendet!!!
#Heiko kann nicht coden, weil er seine Taskleiste nicht ausblendet!!!
#Heiko kann nicht coden, weil er seine Taskleiste nicht ausblendet!!!
#Heiko kann nicht coden, weil er seine Taskleiste nicht ausblendet!!!
#Heiko kann nicht coden, weil er seine Taskleiste nicht ausblendet!!!
#Heiko kann nicht coden, weil er seine Taskleiste nicht ausblendet!!!
#Heiko kann nicht coden, weil er seine Taskleiste nicht ausblendet!!!
#Heiko kann nicht coden, weil er seine Taskleiste nicht ausblendet!!!










