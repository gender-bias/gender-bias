import nltk
import unittest

from genderbias.document import Document
##########

# filename, assertions - number-of-sentences, commas
examples = dict(m=("example_letters/letterofRecM", 13, 12),
                f=("example_letters/letterofRec_W", 26, 29))


class test_Document(unittest.TestCase):

    def test_can_read_examples(self):
        for _, (doc, _, _) in examples.items():
            with open(doc, 'r') as stream:
                self.assertTrue(stream.readable())

    def test_words(self):
        for _, (doc, _, _) in examples.items():
            t = Document(doc)
            words = t.words()
            self.assertTrue(isinstance(words, list))
            self.assertTrue(len(words) > 0)

    def test_stemming(self):
        for _, (doc, _, _) in examples.items():
            t = Document(doc)
            self.assertGreater(
                sum([len(x) for x in t.words()]),
                sum([len(x) for x in t.stemmed_words()])
            )

    # def test_lemmatizing(self):
    #     porter = nltk.PorterStemmer()
    #     wnl = nltk.WordNetLemmatizer()
    #     words = ['strangely']
    #     stemmed = [porter.stem(w) for w in words]
    #     lemmaed = [wnl.lemmatize(w) for w in stemmed]
        #assert lemmaed == ['strange']

    def test_sentence(self):
        for _, (doc, sent_count, _) in examples.items():
            t = Document(doc)
            s = t.sentences()
            for ss in s:
                assert "\n" not in ss
            assert len(s) == sent_count

    def test_words_by_part_of_speech(self):
        for _, (doc, _, comma_count) in examples.items():
            t = Document(doc)
            c = t.words_by_part_of_speech()
            assert len(c[',']) == comma_count
