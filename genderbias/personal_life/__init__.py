"""
Check for statements that pertain to personal, rather than profession, life.

Letters for women are more likely to discuss personal life.

Goal: Develop code that can read text for terms related to personal life like
family, children, etc. If the text includes personal life details; return a
summary that directs the author to review the personal life details for
relevance and consider removing them if they are not relevant to the
recommendation or evaluation.
"""

from genderbias.document import Document
from genderbias.detector import Detector, Flag, Issue

PERSONAL_LIFE_TERMS = [
    "child",
    "children",
    "family",
    "girlfriend",
    "maternal",
    "mother",
    "motherly",
    "spouse",
    "wife",
]

class PersonalLifeDetector(Detector):
    """
    This detector checks for words that relate to personal life instead of
    professional life.

    Links:
        https://github.com/molliem/gender-bias/issues/9
        http://journals.sagepub.com/doi/pdf/10.1177/0957926503014002277

    """

    def get_flags(self, doc: 'Document'):
        """
        Flag the text based upon mentions of personal-life-related words.

        Arguments:
            doc (Document): The document to check

        Returns:
            List[Flag]

        """
        token_indices = []
        flags = []
        words = doc.words()
        offset = 0
        for word in words:
            offset = doc._text.find(word, offset)
            token_indices.append((word, offset, offset + len(word)))
            offset += len(word)

        for word, start, stop in token_indices:
            if word.lower() in PERSONAL_LIFE_TERMS:
                flags.append(
                    Flag(start, stop, Issue(
                        "Personal Life",
                        "The word {word} tends to relate to personal life.".format(word=word),
                        "Try replacing with a sentiment about professional life."
                    ))
                )
        return flags


def personal_life_terms_prevalence(doc: 'Document') -> float:
    """
    Returns the prevalence of tems that refer to personal life.

    Returns the floating-point ratio of `personal`/`total`.

    Arguments:
        doc (Document): The document to check

    Returns:
        float: The "concentration" of personal-life terms

    """
    doc_words = doc.words()

    return float(sum([
        word in PERSONAL_LIFE_TERMS
        for word in doc_words
    ])) / len(doc_words)


