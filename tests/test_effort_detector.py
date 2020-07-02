from genderbias.effort import EffortDetector
from genderbias.document import Document

BAD_DOCUMENTS = [
    """NAME always tried her best, was patient, and had great insight.""",
    """Everyone knows that NAME is persistent.""",
]

GOOD_DOCUMENTS = [
    """NAME was professional and innovative.""",
    """NAME consistently delivered results.""",
]


def test_bad_documents_trip_detector():
    for doc in BAD_DOCUMENTS:
        text = str(EffortDetector().get_report(Document(doc)))
        assert "tends to" in text and "The word" in text


def test_good_documents_pass_detector():
    for doc in GOOD_DOCUMENTS:
        report = EffortDetector().get_report(Document(doc))
        report.set_summary("MY_SUMMARY")
        text = str(report)
        assert len(text.split("\n")) == 2
