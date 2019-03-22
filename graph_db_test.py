#Goes through the whole graph and finds all the paths and the filters to the shortest path

import web_scraper

start_link = "/wiki/Germany"
end_link = "/wiki/Shanghai"

graph = {'A': ['B', 'C'],
             'B': ['C', 'D'],
             'C': ['D'],
             'D': ['C'],
             'E': ['F'],
             'F': ['C']}

web_scraper.getAllUrl(start_link)

def find_shortest_path(graph, start, end, path=[]):
        path = path + [start]
        if start == end:
            return path
        # if start not in graph:
        #     return None
        shortest = None
        for node in graph[start]:
            if node not in path:
                newpath = find_shortest_path(graph, node, end, path)
                if newpath:
                    if not shortest or len(newpath) < len(shortest):
                        shortest = newpath
        return shortest

#print(find_path('/wiki/germany', '/wiki/berlin'))
#print(web_scraper.getAllUrl(start_link))
print(find_shortest_path(graph, "A", "D"))