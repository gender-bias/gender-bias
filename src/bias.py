
examples = dict(m="../example_letters/letterofRecM",
                f="../example_letters/letterofRec_W")

def test_can_read_examples():
    for file in examples.values():
        with open(file, 'r') as stream:
            assert stream.readable()

from nltk import word_tokenize
import nltk
nltk.download('punkt')

def test_can_tokenize_into_wordlist():
    with open(examples['m'], 'r') as stream:
        words = word_tokenize(stream.read())
        assert isinstance(words, list)
        assert len(words) > 0
