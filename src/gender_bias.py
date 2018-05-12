import nltk
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')

# filename, assertions - number-of-sentences, commas
examples = dict(m=("../example_letters/letterofRecM", 13, 12),
                f=("../example_letters/letterofRec_W", 26, 29))

class Document:
    def __init__(self, filename):
        with open(filename, 'r') as f:
            self._text = f.read()

    def sentences_from_text(self):
        return [s.replace('\n',' ') for s in nltk.sent_tokenize(self._text)]

    def words_from_text(self):
        return nltk.word_tokenize(self._text)

    def categorize(self):
        words = self.words_from_text()
        tagged = nltk.pos_tag(words)
        categories = {}
        for type in {t[1] for t in tagged}:
            categories[type] = [t[0] for t in tagged if t[1] == type]
        return categories

    def stem(self):
        words = self.words_from_text()
        return [porter.stem(w) for w in words]

##########

from pytest import fixture

@fixture(params = examples.values())
def example_doc(request):
    return request.param

def test_can_read_examples(example_doc):
    with open(example_doc[0], 'r') as stream:
        assert stream.readable()

def test_words_from_text(example_doc):
    t = Document(example_doc[0])
    words = t.words_from_text()
    assert isinstance(words, list)
    assert len(words) > 0

porter = nltk.PorterStemmer()

def test_stemming(example_doc):
    t = Document(example_doc[0])
    stemmed = t.stem()
    assert sum([len(x) for x in t.words_from_text()]) > sum([len(x) for x in stemmed])

wnl = nltk.WordNetLemmatizer()

def test_lemmatizing():
    words = ['strangely']
    stemmed = [porter.stem(w) for w in words]
    lemmaed = [wnl.lemmatize(w) for w in stemmed]
    #assert lemmaed == ['strange']

def test_sentence(example_doc):
    t = Document(example_doc[0])
    s = t.sentences_from_text()
    for ss in s:
        assert "\n" not in ss
    assert len(s) == example_doc[1]

def test_categorization(example_doc):
    t = Document(example_doc[0])
    c = t.categorize()
    assert len(c[',']) == example_doc[2]
