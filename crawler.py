import sys
from pprint import pprint


import requests
from bs4 import BeautifulSoup


def main():
    args = sys.argv
    if len(args) != 2:
        print('You must provide url as an arguement of the program.')
        exit()

    url = args[1]

    r = requests.get(url)
    soup = BeautifulSoup(r.content.decode('utf-8'), 'html.parser')

    links = []
    visited = [url]

    for link in soup.find_all('a'):
        href = link.get('href')
        if href != None and href[0] != '#' and href not in visited:
            links.append(link.get('href'))

    pprint(links)

if __name__ == '__main__':
    main()
