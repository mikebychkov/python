from sys import warnoptions
import requests
import pprint
from bs4 import BeautifulSoup

def hn(page = 1):

    rsl = []

    res = requests.get(f'https://news.ycombinator.com/?p={page}')
    soup = BeautifulSoup(res.text, 'html.parser')

    titles = soup.select('.titleline')
    sublines = soup.select('.subtext')

    for i, t in enumerate(titles):
        score = sublines[i].select('.score')
        if not score:
            continue
        score = score[0].text
        title = t.text
        link = t.a['href']
        score_int = int(score.replace(' points', ''))
        if score_int > 99:
            rsl.append({"title": title, "score": score_int, "link": link})

    return rsl


tt = []

for n in range(1, 10):
    print(f'Scraping page {n}')
    h = hn(n)
    tt = tt + h

tt.sort(key = lambda k: k['score'], reverse = True)

pprint.pprint(tt)

