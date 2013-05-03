import urllib,urllib2
import nltk
import json
from nltk.corpus import brown
from datetime import datetime,timedelta
import time
import sys
import collections
import re
from mlstripper import strip_tags

start_date = datetime.utcnow()-timedelta(days=1)
end_date = datetime.utcnow()

class ArticleSource():
    endpt = 'http://glass-output.nytimes.com/glass/outputmanager/v1/query.json?source=scoop&type=article&startdate=%i&enddate=%i' % (time.mktime(start_date.timetuple())*1000,time.mktime(end_date.timetuple())*1000)

    def __init__(self):
        try:
            pages = json.loads(urllib.urlopen(self.endpt).read())
            self.current = 0
            regex = re.compile('nytimes.com/(aponline|external|reuters)')
            self.queue = [key for key,val in pages.items() if not regex.search(key)]
            print '%s articles loaded in queue' % len(self.queue)
        except IOError:
            print 'Connection Error'

    def __iter__(self):
        return self

    def next(self):
        if self.current > len(self.queue):
            raise StopIteration()

        self.current+=1
        url = 'http://glass-api.prd.use1.nytimes.com/glass/api/v1/lookup.json?collection=scoop_article&url=%s' % self.queue[self.current]
        try:
            article_data = json.loads(urllib.urlopen(url).read())
            url,article = article_data.popitem()
            return Article(article)
        except IOError:
            raise StopIteration()


class Article():

    def __init__(self,data):
        self.metadata = data

    def __str__(self):
        return strip_tags(self.metadata['data']['cms']['article']['body'])


if __name__ == '__main__':
    articles = ArticleSource()
    print articles.next()
