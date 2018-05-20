#!/usr/bin/env python3

import os
from genderbias.detector import Detector, Flag, Issue

_dir = os.path.dirname(__file__)


ACCOMPLISHMENT_WORDS = open(
    _dir + "/accomplishment_words.txt", 'r').readlines()
EFFORT_WORDS = open(_dir + "/effort_words.txt", 'r').readlines()


class EffortDetector(Detector):

    def get_flags(self, doc: 'Document'):
        """
        Flag the text based upon effort vs accomplishment.
        """
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
                        "Try replacing with phrasing that emphasizes accomplishment."
                    ))
                )
            if word.lower() in ACCOMPLISHMENT_WORDS:
                accomplishment_flags.append(
                    Flag(start, stop, Issue(
                        "Effort vs Accomplishment",
                        "The word '{word}' tends to speak about accomplishment more than effort.".format(
                            word=word)
                    ))
                )

        if (
            len(accomplishment_flags) is 0 or
            len(effort_flags) / len(accomplishment_flags) > 1.2  # TODO: Arbitrary!
        ):
            effort_flags = [
                Flag(0, 0, Issue(
                    "This document has a high ratio ({}:{}) of words suggesting effort to words suggesting concrete accomplishment.".format(
                        len(effort_flags), len(accomplishment_flags)
                    )
                ))
            ] + effort_flags

        return effort_flags
