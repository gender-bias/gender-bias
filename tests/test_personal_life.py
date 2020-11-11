from genderbias.personal_life import PersonalLifeDetector
from genderbias.document import Document

BAD_DOCUMENTS = [
    """NAME was a mother to the lab.""",
    """Our team was glad to welcome NAME to the family.""",
]

GOOD_DOCUMENTS = [
    """NAME was professional and courteous.""",
    """It is always a pleasure working with NAME.""",
]


def test_bad_documents_trip_detector():
    for doc in BAD_DOCUMENTS:
        text = str(PersonalLifeDetector().get_report(Document(doc)))
        assert len(text.split("\n")) == 2


def test_good_documents_pass_detector():
    for doc in GOOD_DOCUMENTS:
        report = PersonalLifeDetector().get_report(Document(doc))
        assert len(report.get_flags()) == 0
