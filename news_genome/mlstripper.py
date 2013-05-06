from timer import Timer
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

def timeme(fn):
    @wraps(fn)
    def wrapper(*args,**kwargs):
        with Timer() as t:
            ret = fn(*args,**kwargs)
        print '%s: %s' % (fn.__name__,t.interval)
        return ret
    return wrapper
