#!/usr/bin/env python3

import os
import nltk
from contextlib import redirect_stdout


with redirect_stdout(open(os.devnull, "w")):
    nltk.download('punkt')
    nltk.download('wordnet')
    nltk.download('averaged_perceptron_tagger')

class Document:

    def __init__(self, document):
        if not os.path.exists(document):
            self._text = document
        else:
            with open(document, 'r') as f:
                self._text = f.read()

    def sentences(self):
        return [s.replace('\n', ' ') for s in nltk.sent_tokenize(self._text)]

    def words(self):
        return nltk.word_tokenize(self._text)

    def words_by_part_of_speech(self):
        words = self.words()
        tagged = nltk.pos_tag(words)
        categories = {}
        for type in {t[1] for t in tagged}:
            categories[type] = [t[0] for t in tagged if t[1] == type]
        return categories

    def stemmed_words(self):
        words = self.words()
        porter = nltk.PorterStemmer()
        return [porter.stem(w) for w in words]
