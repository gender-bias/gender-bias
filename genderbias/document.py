#!/usr/bin/env python3

import os
import nltk
from contextlib import redirect_stdout

# Do not print log messages:
with redirect_stdout(open(os.devnull, "w")):
    nltk.download('punkt')
    nltk.download('wordnet')
    nltk.download('averaged_perceptron_tagger')

class Document:
    """
    Base class for Document, a datatype that stores text and enables
    basic textwise feature extraction, such as listing words or sentences.
    """

    def __init__(self, document, **kwargs):
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

        # Set the caches as None
        self._cached_sentences = None
        self._cached_words = None
        self._cached_words_with_indices = None
        self._cached_words_by_pos = None
        self._cached_stemmed_words = None

        # Try to load the document from disk.
        if not os.path.exists(document):
            self._text = document
        else:
            # If you fail to load from disk, it's because it's a string!
            with open(document, 'r') as f:
                self._text = f.read()

    def sentences(self):
        """
        Compute a list of sentences.

        Uses nltk.sent_tokenize.

        Returns:
            List[str]

        """
        # Default to cache, if available:
        if self._use_cache and self._cached_sentences:
            return self._cached_sentences

        result = [s.replace('\n', ' ') for s in nltk.sent_tokenize(self._text)]
        if self._use_cache:
            self._cached_sentences = result
        return result

    def words(self):
        """
        Compute a list of words from this Document.

        Uses nltk.word_tokenize.

        Returns:
            List[str]

        """
        # Default to cache, if available:
        if self._use_cache and self._cached_words:
            return self._cached_words

        result = nltk.word_tokenize(self._text)
        if self._use_cache:
            self._cached_words = result
        return result

    def words_with_indices(self):
        """
        Compute a list of words, with beginning and end indices

        Returns:
            List[Tuple[str, int, int]]
        """
        # Default to cache, if available:
        if self._use_cache and self._cached_words_with_indices:
            return self._cached_words_with_indices

        offset = 0
        token_indices = []
        for word in self.words():
            offset = self._text.find(word, offset)
            token_indices.append((word, offset, offset + len(word)))
            offset += len(word)
        if self._use_cache:
            self._caached_words = token_indices
        return token_indices

    def words_by_part_of_speech(self):
        """
        Compute the parts of speech for each word in the document.

        Uses nltk.pos_tag.

        Returns:
            dict

        """
        # Default to cache, if available:
        if self._use_cache and self._cached_words_by_pos:
            return self._cached_words_by_pos

        words = self.words()
        tagged = nltk.pos_tag(words)
        categories = {}
        for type in {t[1] for t in tagged}:
            categories[type] = [t[0] for t in tagged if t[1] == type]
        if self._use_cache:
            self._cached_words_by_pos = categories
        return categories

    def stemmed_words(self):
        """
        Compute the stems of words.

        Uses nltk.PorterStemmer.

        Returns:
            List

        """
        # Default to cache, if available:
        if self._use_cache and self._cached_stemmed_words:
            return self._cached_stemmed_words

        words = self.words()
        porter = nltk.PorterStemmer()
        result = [porter.stem(w) for w in words]
        if self._use_cache:
            self._cached_stemmed_words = result
        return result
