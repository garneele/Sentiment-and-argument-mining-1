import os
import argparse
import re
import csv
import pandas as pd
from spacy.lang.en import English
from spacy.pipeline import Sentencizer

parser = argparse.ArgumentParser(description="what")
parser.add_argument('--path', type=str, help='path to the folder with files')
args = parser.parse_args()

def load_corpus(DIR_NAME):
    '''Loads all articles and into a list.'''
    articles = []
    for folder in os.listdir(DIR_NAME):
        if not folder.startswith('.'):
            folder = os.path.join(DIR_NAME, folder)
            for article in os.listdir(folder):
                articles.append(open(os.path.join(folder,article), mode='r', encoding='utf-8-sig').readlines())
    return articles

def preprocess(corpus):
    """Preprocesses the corpus."""
    corpus = [re.sub('\n', '', str(item)) for article in corpus for item in article]
    corpus = [item for item in corpus if item != ""]
    return corpus

def flatten(corpus):
    """Flattens the corpus, one sentence per list."""
    nlp = English()
    sentencizer = Sentencizer()
    temp = []
    for index, element in enumerate(corpus):
        try:
            sentences = list(sentencizer(nlp(element)).sents)
        except ValueError:
            pass
        for sent in sentences:
            temp.append(sent)
    return temp

# def tokenize(corpus)
# tokenizer = Tokenizer(nlp.vocab)

# accept an argument that defines what's being returned: articles on a sentence level,
# or articles on an article level
# If on a sentence level, the results could be saved inside a csv file?

if __name__ == '__main__':
    path_name = args.path
    articles = load_corpus(path_name)
    articles = preprocess(articles)
    articles = flatten(articles)
    df = pd.DataFrame(pd.Series(str(article) for article in articles))
    df.to_csv('articles.csv')
