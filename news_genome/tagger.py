from timer import Timer
import nltk
from nltk.tokenize import word_tokenize
from mlstripper import strip_tags
from nltk.corpus import brown
from nltk.corpus import treebank
from nltk import tag
from nltk.tag import brill
import random

patterns = [
            (r'(.*ing$|.*ed$|.*es$)', 'V'),
            (r'(.*\'s$|.*s$)','NN'),
            (r'(.*tive$|.*ly$)','JJ'),
            (r'(.*est$)','JJS'),
            (r'(.*er$)','JJR')
        ]


brown_tagged_sents = brown.tagged_sents(categories='news')

def get_tagger():
    d_tagger = nltk.DefaultTagger('NN')
    re_tagger = nltk.RegexpTagger(patterns,backoff=d_tagger)
    # train is the proportion of data used in training; the rest is reserved
    # for testing.
    print("Loading tagged data... ")
    tagged_data =  brown_tagged_sents
    cutoff = int(8000*.8)
    training_data = tagged_data[:cutoff]
    gold_data = tagged_data[cutoff:8000]
    testing_data = [[t[0] for t in sent] for sent in gold_data]
    print("Done loading.")

    bigram_tagger = tag.BigramTagger(training_data,backoff=re_tagger)
    
    templates = [
      brill.SymmetricProximateTokensTemplate(brill.ProximateTagsRule, (1,1)),
      brill.SymmetricProximateTokensTemplate(brill.ProximateTagsRule, (2,2)),
      brill.SymmetricProximateTokensTemplate(brill.ProximateTagsRule, (1,2)),
      brill.SymmetricProximateTokensTemplate(brill.ProximateTagsRule, (1,3)),
      brill.SymmetricProximateTokensTemplate(brill.ProximateWordsRule, (1,1)),
      brill.SymmetricProximateTokensTemplate(brill.ProximateWordsRule, (2,2)),
      brill.SymmetricProximateTokensTemplate(brill.ProximateWordsRule, (1,2)),
      brill.SymmetricProximateTokensTemplate(brill.ProximateWordsRule, (1,3)),
      brill.ProximateTokensTemplate(brill.ProximateTagsRule, (-1, -1), (1,1)),
      brill.ProximateTokensTemplate(brill.ProximateWordsRule, (-1, -1), (1,1)),
      ]
    trainer = brill.FastBrillTaggerTrainer(bigram_tagger, templates, 0)
    brill_tagger = trainer.train(training_data, max_rules=100, min_score=3)

    return brill_tagger



if __name__ == '__main__':
    from news_genome import ArticleSource
    articles = ArticleSource()
    article = articles.next()
    tagger = get_tagger()
    with Timer() as t:
        tags = tagger.tag(word_tokenize(strip_tags(article.__str__())))
        print tags
    print t.interval
    print tagger.evaluate(brown_tagged_sents)
