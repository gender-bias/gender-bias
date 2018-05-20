import os

import nltk
from pytest import fixture

from genderbias.document import Document


porter = nltk.PorterStemmer()
wnl = nltk.WordNetLemmatizer()

example_dir = os.path.dirname(__file__) + "/../example_letters/"

# filename, assertions = number-of-sentences, commas
examples = dict(m=dict(file=example_dir + "letterofRecM", sentences=13, commas=12, words=446),
                f=dict(file=example_dir + "letterofRecW", sentences=26, commas=29, words=693))


@fixture(params=examples.values())
def example_doc(request):
    return dict(request.param, document=Document(request.param['file']))


def test_can_read_examples(example_doc):
    with open(example_doc['file'], 'r') as stream:
        assert stream.readable()


def test_words(example_doc):
    words = example_doc['document'].words()
    assert isinstance(words, list)
    assert len(words) == example_doc['words']


def test_words_with_indices(example_doc):
    words_with_indices = example_doc['document'].words_with_indices()
    assert len(words_with_indices) == example_doc['words']
    latest_start = -1
    latest_stop = 0
    for word, start, stop in words_with_indices:
        assert stop > start
        assert stop > latest_stop
        latest_stop = stop
        assert start > latest_start
        latest_start = start


def test_stemming(example_doc):
    assert (sum([len(x) for x in example_doc['document'].words()]) >
            sum([len(x) for x in example_doc['document'].stemmed_words()]))


# def test_lemmatizing():
#     words = ['strangely']
#     stemmed = [porter.stem(w) for w in words]
#     lemmaed = [wnl.lemmatize(w) for w in stemmed]
#     assert lemmaed == ['strange']


def test_sentence(example_doc):
    s = example_doc['document'].sentences()
    for ss in s:
        assert "\n" not in ss
    assert len(s) == example_doc['sentences']


def test_words_by_part_of_speech(example_doc):
    c = example_doc['document'].words_by_part_of_speech()
    assert len(c[',']) == example_doc['commas']
