#!/usr/bin/env python3

"""
Check for the usage of strange or unnatural gendered words.

"""


import os
from genderbias.detector import Detector, Flag, Issue, Report

_dir = os.path.dirname(__file__)


GENDERED_WORDS = [
    w.strip()
    for w in open(
    _dir + "/genderedwords.wordlist", 'r').readlines()
]


class GenderedWordDetector(Detector):
    """
    This detector checks for words that call unnecessary attention to the
    gender of the letter recipient.

    """

    def get_report(self, doc):
        """
        Report the usage of unnecessarily gendered words.

        Arguments:
            doc (Document): The document to check

        Returns:
            Report

        """
        report = Report("Unnecessarily Gendered Words")

        token_indices = doc.words_with_indices()

        for word, start, stop in token_indices:
            if word.lower() in GENDERED_WORDS:
                report.add_flag(
                    Flag(start, stop, Issue(
                        "Unnecessarily Gendered Words",
                        "The word '{word}' is unneccesarily gendered.".format(
                            word=word),
                        "Replace this term with 'person' or 'individual', or a position-specific phrase like 'doctor' or 'author'.",
                        bias=Issue.negative_result
                    ))
                )

        return report
