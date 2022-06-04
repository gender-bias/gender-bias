from genderbias.technical_terms import TechnicalTermsDetector
from genderbias.document import Document

BAD_DOCUMENTS_BEFORE_DETECTION = [
    """Currently we are making sure that a seperate file works, 
    then we will split on the classList thing you suggested """,
]

GOOD_DOCUMENTS_BEFORE_DETECTION = [
    """Currently we are making sure that a seperate file works, 
    then we will split on the REPLACED thing you suggested """,
]

def test_bad_documents_false_detector():
    for doc in BAD_DOCUMENTS_BEFORE_DETECTION:
        text = TechnicalTermsDetector().get_report(Document(doc)).to_string()
        print(text)
        assert "Technical Terms" in text


def test_good_documents_pass_detector():
    for doc in GOOD_DOCUMENTS_BEFORE_DETECTION:
        report = TechnicalTermsDetector().get_report(Document(doc))
        assert len(report.get_flags()) == 0

