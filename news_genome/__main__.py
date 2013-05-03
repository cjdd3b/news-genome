from news_genome.features import metrics
import argparse
import csv
from StringIO import StringIO
from news_genome import ArticleSource
import codecs

class UnicodeWriter:
    """
    A CSV writer which will write rows to CSV file "f",
    which is encoded in the given encoding.
    """

    def __init__(self, f, dialect=csv.excel, encoding="utf-8", **kwds):
        # Redirect output to a queue
        self.queue = StringIO()
        self.writer = csv.writer(self.queue, dialect=dialect, **kwds)
        self.stream = f
        self.encoder = codecs.getincrementalencoder(encoding)()

    def writerow(self, row):
        self.writer.writerow([s.encode("utf-8") for s in row])
        # Fetch UTF-8 output from the queue ...
        data = self.queue.getvalue()
        data = data.decode("utf-8")
        # ... and reencode it into the target encoding
        data = self.encoder.encode(data)
        # write to the target stream
        self.stream.write(data)
        # empty queue
        self.queue.truncate(0)

    def writerows(self, rows):
        for row in rows:
            self.writerow(row)



def generate_report():
    articles = ArticleSource()
    report_file = StringIO()
    report = UnicodeWriter(report_file)
    report.writerow(['article']+[metric.__name__ for metric in metrics])
    for article in articles:
        results = [article.metadata['headline']]
        for metric in metrics:
            results.append(str(metric(article.__str__())))
        report.writerow(results)
    report_file.seek(0)
    print report_file.read()
        

generate_report()
        
