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
        assert(
            len(PersonalLifeDetector().get_flags(Document(doc))) > 0
        )

def test_good_documents_pass_detector():
    for doc in GOOD_DOCUMENTS:
        assert(
            len(PersonalLifeDetector().get_flags(Document(doc))) == 0
        )
