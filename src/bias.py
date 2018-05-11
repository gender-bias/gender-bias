
examples = dict(m="../example_letters/letterofRecM",
                f="../example_letters/letterofRec_W")

def test_can_read_examples():
    for file in examples.values():
        with open(file, 'r') as stream:
            assert stream.readable()

from nltk import word_tokenize
import nltk
nltk.download('punkt')
nltk.download('wordnet')

def test_can_tokenize_into_wordlist():
    with open(examples['m'], 'r') as stream:
        words = word_tokenize(stream.read())
        assert isinstance(words, list)
        assert len(words) > 0

porter = nltk.PorterStemmer()

def test_stemming():
    words = ['strangely']
    stemmed = [porter.stem(w) for w in words]
    assert stemmed == ['strang']

wnl = nltk.WordNetLemmatizer()

def test_lemmatizing():
    words = ['strangely']
    stemmed = [porter.stem(w) for w in words]
    lemmaed = [wnl.lemmatize(w) for w in stemmed]
    #assert lemmaed == ['strange']
