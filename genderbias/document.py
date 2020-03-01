#!/usr/bin/env python3

from typing import List, Tuple

import os
import nltk
from contextlib import redirect_stdout

# Do not print log messages:
with redirect_stdout(open(os.devnull, "w")):
    nltk.download('punkt')
    nltk.download('wordnet')
    nltk.download('averaged_perceptron_tagger')

def cached(method):
    """
    Method decorator for the Document class, caching results if enabled
    """
    result = {}
    def wrapper(*args):
        if not args[0]._use_cache:
            return method(*args)
        params = tuple(args)
        if params not in result:
            result[params] = method(*args)
        return result[params]
    return wrapper

class Document:
    """
    Base class for Document, a datatype that stores text and enables
    basic textwise feature extraction, such as listing words or sentences.
    """

    def __init__(self, document: 'Document', **kwargs) -> None:
        """
        Create a new Document.

        Arguments:
            document (str): The string, or a pathlike, to load
            use_cache (bool: True): Cache sentences and words. This is
                especially useful if you anticipate referencing these functions
                commonly. Disable this on ridiculously large documents to save
                on memory usage.

        """
        # Pass `use_cache=False` if you want to disable caching
        self._use_cache = True
        if 'no_cache' in kwargs:
            self._use_cache = not kwargs['no_cache']

        # Try to load the document from disk.
        if not os.path.exists(document):
            self._text = document
        else:
            # If you fail to load from disk, it's because it's a string!
            with open(document, 'r') as f:
                self._text = f.read()


    def text(self) -> str:
        """
        Returns the text of the document.

        Returns:
            str
        """
        return self._text

    @cached
    def sentences(self) -> List[str]:
        """
        Compute a list of sentences.

        Uses nltk.sent_tokenize.

        Returns:
            List[str]

        """
        return [s.replace('\n', ' ') for s in nltk.sent_tokenize(self._text)]

    @cached
    def words(self) -> List[str]:
        """
        Compute a list of words from this Document.

        Uses nltk.word_tokenize.

        Returns:
            List[str]

        """
        return nltk.word_tokenize(self._text)

    @cached
    def words_with_indices(self) -> List[Tuple[str, int, int]]:
        """
        Compute a list of words, with beginning and end indices

        Returns:
            List[Tuple[str, int, int]]
        """
        offset = 0
        token_indices = []
        for word in self.words():
            offset = self._text.find(word, offset)
            token_indices.append((word, offset, offset + len(word)))
            offset += len(word)
        return token_indices

    @cached
    def words_by_part_of_speech(self) -> dict:
        """
        Compute the parts of speech for each word in the document.

        Uses nltk.pos_tag.

        Returns:
            dict

        """
        words = self.words()
        tagged = nltk.pos_tag(words)
        categories = {}
        for type in {t[1] for t in tagged}:
            categories[type] = [t[0] for t in tagged if t[1] == type]
        return categories

    @cached
    def stemmed_words(self) -> List:
        """
        Compute the stems of words.

        Uses nltk.PorterStemmer.

        Returns:
            List

        """
        words = self.words()
        porter = nltk.PorterStemmer()
        return [porter.stem(w) for w in words]
