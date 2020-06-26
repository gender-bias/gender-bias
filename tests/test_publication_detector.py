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
        assert "Try" in pub_detector.get_summary(doc)

def test_good_letters_pass():
    for letter in GOOD_LETTERS:
        doc = Document(letter)
        assert "Try" not in pub_detector.get_summary(doc)
        assert "at least one" in pub_detector.get_summary(doc)

def test_very_good_letter_passes_higher_thresh_detector():
    # The detector counts quoted strings as publications
    # with probability 0.25, so we need lots of them to exceed 
    # a threshold of 2. 
    veryGoodLetter = "NAME has many publications, including "
    for i in range(1,9):
        veryGoodLetter += '"Publication {}", '.format(i)
        
    picky_detector = PublicationDetector(min_publications=2)
    doc = Document(veryGoodLetter)
    assert "at least 2" in picky_detector.get_summary(doc)        

def test_good_letters_fail_high_thresh_detector():
    picky_detector = PublicationDetector(min_publications=10)
    for letter in GOOD_LETTERS + BAD_LETTERS:
        doc = Document(letter)
        assert "Try" in picky_detector.get_summary(doc)

def test_report_summary():
   for letter in BAD_LETTERS:
        doc = Document(letter)
        report = pub_detector.get_report(doc)
        assert "SUMMARY" in report.to_string()

def test_no_flags():
   for letter in BAD_LETTERS:
        doc = Document(letter)
        report = pub_detector.get_report(doc)
        report_dict = report.to_dict()
        assert not report_dict["flags"]
