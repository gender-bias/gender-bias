"""
Tools for determining how much a letter talks about personal life.
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

    def get_flags(self, doc: 'Document'):
        """
        Flag
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
                    )
                ))
        return flags


def personal_life_terms_prevalence(doc: 'Document') -> float:
    """
    Returns the prevalence of tems that refer to personal life,
    as a ratio of `personal`/`total`.

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


