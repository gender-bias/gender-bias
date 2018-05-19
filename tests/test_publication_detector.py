from genderbias import Document
from genderbias.publications import PublicationDetector

BAD_LETTERS = [
    """
    NAME is a prolific researcher, and she published 12 papers during her tenure at UNIVERSITY, including some very well-respected articles in our field.
    """,
]

GOOD_LETTERS = [
    """
    NAME is a prolific researcher, and she published 12 papers during her tenure at UNIVERSITY, including the seminal microbiology paper, "On the Origin of Brie Cheese," and the followup microbotany manuscript, "A Brief History of Thyme."
    """,
]

pub_detector = PublicationDetector()

def test_bad_letters_fail():
    for letter in BAD_LETTERS:
        doc = Document(letter)
        assert pub_detector.get_flags(doc)

def test_good_letters_pass():
    for letter in GOOD_LETTERS:
        doc = Document(letter)
        assert len(pub_detector.get_flags(doc)) == 0
