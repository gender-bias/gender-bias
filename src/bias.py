import nltk

examples = dict(m="../example_letters/letterofRecM",
                f="../example_letters/letterofRec_W")

def load_text(filename):
    with open(filename, 'r') as f:
        return f.read()

##########

def test_can_read_examples():
    for file in examples.values():
        with open(file, 'r') as stream:
            assert stream.readable()

from nltk import word_tokenize
nltk.download('punkt')
nltk.download('wordnet')

def test_can_tokenize_into_wordlist():
    t = load_text(examples['m'])
    words = word_tokenize(t)
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
