import urllib,urllib2
import nltk
import json
from nltk.corpus import brown
from HTMLParser import HTMLParser

class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()

data = json.loads(urllib.urlopen('http://glass-api.prd.use1.nytimes.com/glass/api/v1/lookup.json?collection=scoop_article&url=http://www.nytimes.com/2013/02/14/us/dorner-california-remains-police-shootout.html').read())

key,article = data.popitem()

summary = nltk.word_tokenize(article['data']['cms']['article']['summary'])
body = nltk.word_tokenize(strip_tags(article['data']['cms']['article']['body']))

print nltk.pos_tag(body)
