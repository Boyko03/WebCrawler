import sys
from pprint import pprint
from time import sleep


import requests
from bs4 import BeautifulSoup


servers = {}


def get_page_urls(links, visited):
    new_links = []

    for link in links:
        try:
            r = requests.get(link)

            soup = BeautifulSoup(r.content.decode('ISO-8859-1'), 'html.parser')
        except Exception as exc:
            print('===================================================')
            print(link)
            print(exc)
            print('===================================================')

            pprint(servers)
            exit()

        server = r.headers["Server"]
        if server in servers:
            servers[server] += 1
        else:
            servers[server] = 1

        visited.append(link)

        for n_link in soup.find_all('a'):
            href = n_link.get('href')
            if href != None and href != '' and not href.startswith('#') and href not in visited and href not in new_links:
                if not href.startswith('http'):
                    href = link + href
                new_links.append(href)

    # pprint(new_links)

    return get_page_urls(new_links, visited)

def main():
    args = sys.argv
    if len(args) != 2:
        print('You must provide url as an arguement of the program.')
        exit()

    url = args[1]

    visited = []

    get_page_urls([url], visited)

    pprint(servers)


if __name__ == '__main__':
    main()
