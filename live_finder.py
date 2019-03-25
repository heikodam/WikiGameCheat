import web_scraper
import sys

def is_link_in_page(page_to_check, end_link):
    links_on_page = web_scraper.getAllUrl(page_to_check)
    if end_link in links_on_page:
        return True
    else:
        return False


start_link = "/wiki/Flour"
link = start_link
end_link = "/wiki/Flour"
path = [[start_link]]

links_on_start_page = web_scraper.getAllUrl(start_link)


def get_all_degree_links(degree, start_degree_pages):
    current_degree_pages = []
    if degree == 0:
        return start_degree_pages
    for page in start_degree_pages:
        current_degree_pages += web_scraper.getAllUrl(page)
    return get_all_degree_links(degree - 1, current_degree_pages)


degree_count = 0
while True:
    path.append(get_all_degree_links(degree_count, start_link[degree_count]))
    if end_link in path[degree_count]):
        print("They are {} clicks away".format(degree_count + 1))
    degree_count += 1


# def get_all_degree_links(degree, start_degree_pages):
#     current_degree_pages = []
#     if degree == 0:
#         return start_degree_pages
#     for page in start_degree_pages:
#         current_degree_pages += web_scraper.getAllUrl(page)
#     return get_all_degree_links(degree - 1, current_degree_pages)


# degree_count = 0
# while True:
#     if end_link in get_all_degree_links(degree_count, start_link):
#         print("They are {} clicks away".format(degree_count))
#     degree_count += 1
        
    
    
    




# if is_link_in_page(start_link, end_link):
#         print("Found the Page 1")
#         path.append(end_link)
#         print(path)
#         sys.exit()


# for current_page in links_on_start_page:
#     if is_link_in_page(current_page, end_link):
#         print("Found the Page 2")
#         path.append(current_page)
#         path.append(end_link)
#         print(path)
#         sys.exit()
#         break

# for second_degree in links_on_start_page:
#     for current_page in web_scraper.getAllUrl(second_degree):
#         if is_link_in_page(current_page, end_link):
#             print("Found the Page 3")
#             path.append(second_degree)
#             path.append(current_page)
#             path.append(end_link)
#             print(path)
#             sys.exit()
#             break

# for second_degree in links_on_start_page:
#     for third_degree in web_scraper.getAllUrl(second_degree):
#         for current_page in web_scraper.getAllUrl(third_degree):
#             if is_link_in_page(current_page, end_link):
#                 print("Found the Page 3")
#                 path.append(second_degree)
#                 path.append(current_page)
#                 path.append(end_link)
#                 print(path)
#                 sys.exit()
#                 break


# path.append(end_link)
# print(path)

# degree = 0
# while True:
#         for i in range(degree):


#pseudo code for better looking algorythim

#start with degree 1

#check witch degree on
#go into first link that many times as the degree
#check all links on that page if they match
#for to the end of links
        #go back one degree then go to the next page
        #check all links on that page if they match



# check first degree

# for each degree (starting at one and increasing)      until the end link is found
#      check each link of that degree


    
                









