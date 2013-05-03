from HTMLParser import HTMLParser
from functools import wraps

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

def nohtml(fn):
    @wraps(fn)
    def wrapper(text,*args,**kwargs):
        text = strip_tags(text)
        return fn(text,*args,**kwargs)
    return wrapper

