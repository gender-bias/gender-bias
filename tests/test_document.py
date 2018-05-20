import os

import nltk
from pytest import fixture

from genderbias.document import Document


porter = nltk.PorterStemmer()
wnl = nltk.WordNetLemmatizer()

example_dir = os.path.dirname(__file__) + "/../example_letters/"

# filename, assertions = number-of-sentences, commas
examples = dict(m=dict(file=example_dir + "letterofRecM", sentences=13, commas=12),
                f=dict(file=example_dir + "letterofRecW", sentences=26, commas=29))


@fixture(params=examples.values())
def example_doc(request):
    return request.param

def test_can_read_examples(example_doc):
    with open(example_doc['file'], 'r') as stream:
        assert stream.readable()


def test_words(example_doc):
    t = Document(example_doc['file'])
    words = t.words()
    assert isinstance(words, list)
    assert len(words) > 0


def test_stemming(example_doc):
    t = Document(example_doc['file'])
    assert (sum([len(x) for x in t.words()]) >
            sum([len(x) for x in t.stemmed_words()]))


# def test_lemmatizing():
#     words = ['strangely']
#     stemmed = [porter.stem(w) for w in words]
#     lemmaed = [wnl.lemmatize(w) for w in stemmed]
#     assert lemmaed == ['strange']


def test_sentence(example_doc):
    t = Document(example_doc['file'])
    s = t.sentences()
    for ss in s:
        assert "\n" not in ss
    assert len(s) == example_doc['sentences']


def test_words_by_part_of_speech(example_doc):
    t = Document(example_doc['file'])
    c = t.words_by_part_of_speech()
    assert len(c[',']) == example_doc['commas']
