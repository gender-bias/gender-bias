"""
Check for words that pertain to technical terms such as "whitelist", "whitelist", "dummy value" which is discriminatory. 

Tools for identifying mention of words / terms that commonly used in Software Artifacts and Developer Communications .

"""

from genderbias.document import Document
from genderbias.detector import Detector, Flag, Issue, Report

TECHNICAL_TERMS = [
    "whitelist",
    "blacklist",
    "master",
    "slave",
    "grandfathered",
    "guys",
    "he",
    "him",
    "his",
    "man hours",
    "sanity check",
    "dummy value",
]

class TechnicalTermsDetector(Detector):
    """
    This detector checks for words that relate to technical terms

    Links:
        https://github.com/gender-bias/gender-bias/issues/87
        https://www.proquest.com/docview/2583118526?pq-origsite=gscholar&fromopenview=true
    """

    def get_report(self, doc): 
        """
        Generate a report on the text based upon mentions of
        technical-term-related words.

        Arguments:
            doc (Document): The document to check

        Returns:
            Report

        """
        report = Report("Technical Terms")

        token_indices = doc.words_with_indices()

        for word, start, stop in token_indices:
            if word.lower() in TECHNICAL_TERMS:
                report.add_flag(
                    Flag(
                        start,
                        stop,
                        Issue(
                            "Technical Terms",
                            f"The word {word} tends to relate to technical terms that is non-inclusive language "
                            + ", is disproportionately included in conversations "
                        ),
                    )
                )
        return report


def Techical_terms_prevalence(doc: "Document") -> str:
    """
    Returns the prevalence of tems that refer to techinical terminology that is discriminatory.

    Arguments:
        doc (Document): The document to check

    Returns:
        str: The "concentration" of technical terms in Software Artifacts and Developer Communications.

    """
    doc_words = doc.words()

    return ([word in TECHNICAL_TERMS for word in doc_words])
