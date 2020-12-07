import os
import argparse
import csv
import pandas as pd
import spacy
from spacy.lang.en import English
from spacy.pipeline import Sentencizer
from sentence_transformers import SentenceTransformer

parser = argparse.ArgumentParser(description="what")
parser.add_argument('--path', type=str, help='path to the folder with files')
parser.add_argument('--flatten', type=int, help='return a list of sentences(1) or a list of paragraphs(0)', default=1)
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
    """Preprocesses the corpus and flattens it."""
    corpus = [item.rstrip() for article in corpus for item in article]
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

if __name__ == '__main__':
    print("Loading BERT model")
    model = SentenceTransformer('bert-base-nli-cls-token')
    path_name = args.path
    documents = load_corpus(path_name)
    documents = preprocess(documents)
    if args.flatten == 1:
        documents = flatten(documents)
        print("Number of sentences:", len(documents))
        print("Calculating embeddings...")
        embedding = pd.Series([model.encode(str(document)) for document in documents])
        text = pd.Series(str(document) for document in documents)
        df = pd.DataFrame({"text":text, "embedding":embedding})
        df.to_csv('corpus_sentences.csv')
    else:
        print("Number of paragraphs:", len(documents))
        print("Calculating embeddings...")
        embedding = pd.Series([model.encode(str(document)) for document in documents])
        text = pd.Series(str(document) for document in documents)
        df = pd.DataFrame({"text":text, "embedding":embedding})
        df.to_csv('corpus_paragraphs.csv')
    print("Done!")
