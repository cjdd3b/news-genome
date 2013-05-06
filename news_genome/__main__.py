from news_genome.features import metrics
import argparse
import csv
from StringIO import StringIO
from news_genome import ArticleSource
import codecs

def generate_report():
    articles = ArticleSource()
    report_file = open('genome.csv','w')
    report = csv.writer(report_file) 
    report.writerow([
         'article',
         'word_count',
         'sentence_count',
         'avg_word_length',
         'number_of_grafs',
         'length_of_first_graf',
         'avg_sentence_length',
         'avg_graf_length',
         'punct_count_?',
         'punct_count_!',
         'punct_count_"',
         #'pos_count_NN',
         #'pos_count_VBP',
         #'pos_count_JJ',
         'pos_percentages_NN',
         'pos_percentages_VBP',
         'pos_percentages_JJ',
         'avg_word_syllables',
         'flesch_readability',
         'smog_readability',
         'coleman_liau_readability'
    ])
    for article in articles:
        results = [article.get_headline()] + metrics(article.__str__())
        print results
        report.writerow(results)
        report_file.flush()
    report_file.close()
        

generate_report()
        
