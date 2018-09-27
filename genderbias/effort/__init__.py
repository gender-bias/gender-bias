#!/usr/bin/env python3

"""
Check for statements that pertain to effort, rather than accomplishment.

Letters for women are more likely to highlight effort (she is hard-working)
instead of highlighting accomplishments (her research is groundbreaking).

Goal: Develop code that can read text for effort statements. If the text
includes more effort statements, than accomplishment statements; return a
summary that directs the author to add statements related to accomplishment.
"""


import os
from genderbias.detector import Detector, Flag, Issue, Report

_dir = os.path.dirname(__file__)


ACCOMPLISHMENT_WORDS = [
    w.strip()
    for w in open(
    _dir + "/accomplishment_words.wordlist", 'r').readlines()
]

EFFORT_WORDS = [
    w.strip()
    for w in open(_dir + "/effort_words.wordlist", 'r').readlines()
]


class EffortDetector(Detector):
    """
    This detector checks for words that relate to effort versus concrete
    accomplishments.

    Links:
        https://github.com/molliem/gender-bias/issues/8
        http://journals.sagepub.com/doi/pdf/10.1177/0957926503014002277

    """

    def get_report(self, doc):
        """
        Generates a report on the text based upon effort vs accomplishment.

        Also adds a summary if there are NO words about accomplishment, or if
        the ratio of effort to accomplishment words is particularly low.

        Arguments:
            doc (Document): The document to check

        Returns:
            Report

        """
        report = Report("Effort vs Accomplishment")
        effort_flags = []
        accomplishment_flags = []

        token_indices = doc.words_with_indices()

        for word, start, stop in token_indices:
            if word.lower() in EFFORT_WORDS:
                effort_flags.append(
                    Flag(start, stop, Issue(
                        "Effort vs Accomplishment",
                        "The word '{word}' tends to speak about effort more than accomplishment.".format(
                            word=word),
                        "Try replacing with phrasing that emphasizes accomplishment.",
                        bias=Issue.negative_result
                    ))
                )
            if word.lower() in ACCOMPLISHMENT_WORDS:
                accomplishment_flags.append(
                    Flag(start, stop, Issue(
                        "Effort vs Accomplishment",
                        "The word '{word}' tends to speak about accomplishment more than effort.".format(
                            word=word),
                        bias=Issue.positive_result
                    ))
                )

        for flag in effort_flags:
            report.add_flag(flag)

        if (
            len(accomplishment_flags) is 0 or
            len(effort_flags) / len(accomplishment_flags) > 1.2  # TODO: Arbitrary!
        ):
            # Avoid divide-by-zero errors
            if len(accomplishment_flags) == 0:
                report.set_summary("This document has too few words about concrete accomplishment.")
            else:
                report.set_summary("This document has a high ratio ({}:{}) of words suggesting effort to words suggesting concrete accomplishment.".format(
                            len(effort_flags), len(accomplishment_flags)
                        )
                    )

        return report
