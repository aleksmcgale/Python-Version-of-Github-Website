import requests
import re
from bs4 import BeautifulSoup

url = 'https://github.com/aleksmcgale?tab=repositories'
total_projects = 0

def search_projects(url):
    html = requests.get(url).text
    soup = BeautifulSoup(html, features="html.parser")
    for script in soup(["script", "style"]):
        script.decompose()
    projects = {}
    n = soup.find_all('a', itemprop="name codeRepository")
    name = [x.text.strip('\n').strip(' ').rstrip() for x in n]
    index = name.index("aleksmcgale.github.io")
    name.remove("aleksmcgale.github.io")
    projects['name'] = name
    d = soup.find_all('p', itemprop="description")
    description = [x.text.strip('\n').strip(' ').rstrip() for x in d]

    projects['description'] = description
    l = soup.find_all('span', itemprop="programmingLanguage")
    language = [x.text.strip('\n').strip(' ').rstrip() for x in l]
    language.pop(index)
    projects['language'] = language


    u = soup.find_all('relative-time')
    update = [x.text.strip('\n').strip(' ').rstrip() for x in u]
    update.pop(index)
    projects['update'] = update

    starter = "https://github.com/aleksmcgale/"
    link = [starter + x for x in name]
    projects['link'] = link




    return projects

def create_project(url):
    projects = search_projects(url)
    x = len(projects['name'])
    i = 0
    final = []
    while i < x:
        f = {}
        f['name'] = projects['name'][i]

        f['description'] = projects['description'][i]
        f['language'] = projects['language'][i]
        f['update'] = projects['update'][i]
        f['link'] = projects['link'][i]
        final.append(f)
        i += 1

    return final


if __name__ == '__main__':
    link = 'https://github.com/aleksmcgale?tab=repositories'
    t = create_project(link)

    print(t)


