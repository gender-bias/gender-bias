#!/usr/bin/env python3

"""
Check for statements that pertain to effort, rather than accomplishment.

Letters for women are more likely to highlight effort ("she is hard-working")
instead of highlighting accomplishments ("her research is groundbreaking").

Goal: Develop code that can read text for effort statements. If the text
includes more effort statements, than accomplishment statements; return a
summary that directs the author to add statements related to accomplishment.
"""


import os
import spacy

from genderbias.detector import Detector, Flag, Issue, Report, Document

_dir = os.path.dirname(__file__)


ACCOMPLISHMENT_WORDS = [
    w.strip() for w in open(_dir + "/accomplishment_words.wordlist", "r").readlines()
]

EFFORT_WORDS = [
    w.strip() for w in open(_dir + "/effort_words.wordlist", "r").readlines()
]


class EffortDetector(Detector):
    """
    This detector checks for words that relate to effort versus concrete
    accomplishments.

    Links:
        https://github.com/molliem/gender-bias/issues/8
        http://journals.sagepub.com/doi/pdf/10.1177/0957926503014002277

    """

    def get_report(self, doc: Document):
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

        nlp = spacy.load("en_core_web_sm")
        doc = nlp(doc.text)

        # Ignore adjectives about the author.
        # TODO: This is dependent upon the type of writing! If this is a cover-
        # letter, e.g., then these are not good to exclude!
        _PRONOUNS_TO_IGNORE = ["me", "I", "myself"]

        # Keep track of accomplishment- or effort-specific words:
        accomplishment_words = 0
        effort_words = 0

        # Loop over NOUN-ADJ pairs:
        for i, token in enumerate(doc):
            if token.pos_ not in ("NOUN", "PROPN", "PRON"):
                # We don't need to assign a valence to this token
                continue
            if str(token) in _PRONOUNS_TO_IGNORE:
                # If this token IS a noun but it's an ignored pronoun, move on
                continue

            # Find corresponding adjective:
            for j in range(i + 1, len(doc)):
                if doc[j].pos_ == "ADJ":

                    # If accomplishment-flavored, add positive flag.
                    if str(doc[j]) in ACCOMPLISHMENT_WORDS:
                        accomplishment_words += 1
                        warning = (
                            f"The word '{str(doc[j])}' refers to explicit accomplishment rather than effort.",
                        )
                        suggestion = ""
                        bias = Issue.positive_result

                    # If effort-flavored, add negative flag.
                    elif str(doc[j]) in EFFORT_WORDS:
                        effort_words += 1
                        warning = (
                            f"The word '{str(doc[j])}' tends to speak about effort more than accomplishment.",
                        )
                        suggestion = "Try replacing with phrasing that emphasizes accomplishment."
                        bias = Issue.negative_result

                    else:
                        break

                    # Add a flag to the report:
                    report.add_flag(
                        Flag(
                            doc[j].sent.start_char,
                            doc[j].sent.end_char,
                            Issue(
                                "Effort vs Accomplishment",
                                warning,
                                suggestion,
                                bias=bias,
                            ),
                        )
                    )
                    break

        if (
            accomplishment_words == 0 and effort_words > 0
        ) or effort_words / accomplishment_words > 1.2:  # TODO: Arbitrary!
            report.set_summary(
                "This document has a high ratio of words suggesting "
                + f"effort ({effort_words}) to words suggesting "
                + f"concrete accomplishment ({accomplishment_words}).",
            )

        return report
