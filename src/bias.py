import nltk
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')

# filename, assertions - number-of-sentences, commas
examples = dict(m=("../example_letters/letterofRecM", 13, 12),
                f=("../example_letters/letterofRec_W", 26, 29))

def load_text(filename):
    with open(filename, 'r') as f:
        return f.read()

def sentences_from_text(text):
    return [s.replace('\n',' ') for s in nltk.sent_tokenize(text)]

def words_from_text(text):
    return nltk.word_tokenize(text)

def categorize(text):
    words = words_from_text(text)
    tagged = nltk.pos_tag(words)
    categories = {}
    for type in {t[1] for t in tagged}:
        categories[type] = [t[0] for t in tagged if t[1] == type]
    return categories

##########

from pytest import fixture

@fixture(params = examples.values())
def example_doc(request):
    return request.param

def test_can_read_examples(example_doc):
    with open(example_doc[0], 'r') as stream:
        assert stream.readable()

def test_words_from_text(example_doc):
    t = load_text(example_doc[0])
    words = words_from_text(t)
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

def test_sentence(example_doc):
    t = load_text(example_doc[0])
    s = sentences_from_text(t)
    for ss in s:
        assert "\n" not in ss
    assert len(s) == example_doc[1]

def test_categorization(example_doc):
    t = load_text(example_doc[0])
    c = categorize(t)
    assert len(c[',']) == example_doc[2]
