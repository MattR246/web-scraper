import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://news.ycombinator.com/news?p=1')
soup = BeautifulSoup(res.text, 'html.parser')
get_links = soup.select('.storylink')
get_subtext = soup.select('.subtext')


def sort_by_score(custom):
    return sorted(custom, key=lambda k: k['score'], reverse=True)


def custom_feed(links, scores):
    custom = []
    for index, item in enumerate(links):
        title = links[index].getText()
        href = links[index].get('href', None)
        score = get_subtext[index].select('.score')
        if len(score):
            points = int(score[0].getText().replace(' points', ''))
            if points > 99:
                custom.append({'title': title, 'score': points, 'link': href})
    return sort_by_score(custom)


pprint.pprint(custom_feed(get_links, get_subtext))


