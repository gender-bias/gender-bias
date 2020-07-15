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
        doc = nlp(doc.text())

        # Ignore adjectives about the author.
        _PRONOUNS_TO_IGNORE = ["me", "myself", "I"]

        # Keep track of accomplishment- or effort-specific words:
        accomplishment_words = 0
        effort_words = 0

        # Keep track of flags (we'll deduplicate them before reporting)
        flags = set()

        # Loop over tokens to find adjectives to flag:
        for token in doc:
            # Find all tokens whose dependency tag is adjectival complement:
            if token.dep_ == "acomp":
                # Get all dependencies of the head/root of the tagged sentence
                # and look for nouns (which are likely to be the referenced
                # subject of this adjectival complement):
                for reference_token in token.head.children:
                    # If this token IS a noun but it's an ignored pronoun, move on
                    if (
                        reference_token.pos_ in ["PRON", "PROPN"]
                        and reference_token.text not in _PRONOUNS_TO_IGNORE
                    ):
                        print(reference_token, token)
                        # If accomplishment-flavored, add positive flag.
                        if token.text in ACCOMPLISHMENT_WORDS:
                            accomplishment_words += 1
                            warning = (
                                f"The word '{token.text}' refers to "
                                + "explicit accomplishment rather than effort."
                            )
                            suggestion = ""
                            bias = Issue.positive_result

                        # If effort-flavored, add negative flag.
                        elif token.text in EFFORT_WORDS:
                            effort_words += 1
                            warning = (
                                f"The word '{token.text}' tends to speak "
                                + "about effort more than accomplishment."
                            )
                            suggestion = (
                                "Try replacing with phrasing that "
                                + "emphasizes accomplishment."
                            )
                            bias = Issue.negative_result

                        else:
                            continue

                        flags.add(
                            (
                                token.sent.start_char,
                                token.sent.end_char,
                                warning,
                                suggestion,
                                bias,
                            )
                        )

        for (start, stop, warning, suggestion, bias) in flags:
            # Add a flag to the report:
            report.add_flag(
                Flag(
                    start,
                    stop,
                    Issue("Effort vs Accomplishment", warning, suggestion, bias=bias),
                )
            )

        if 0 < effort_words <= accomplishment_words:
            report.set_summary(
                "This document has a high ratio of words suggesting "
                + f"effort ({effort_words}) to words suggesting "
                + f"concrete accomplishment ({effort_words}).",
            )

        return report
