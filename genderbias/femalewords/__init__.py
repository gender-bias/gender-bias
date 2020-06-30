import os
import re

from ..detector import Detector, Flag, Issue, Report

_dir = os.path.dirname(__file__)
FEMALE_WORDS = [
    word.strip() for word in open(_dir + "/Femalewords.wordlist", "r").readlines()
]


class FemaleDetector(Detector):
    """
    A detector for words that tend to be used more frequently for recruiting
    women than for recruiting men.

    """

    def get_report(self, doc):
        female_report = Report("\nTerms biased towards women")
        words_with_indices = doc.words_with_indices()

        found = False
        for word, start, stop in words_with_indices:
            word = word.lower()
            for femaleword in FEMALE_WORDS:
                searchTerm = "^" + femaleword + ".."
                x = re.search(searchTerm, word)
                if x:
                    found = True
                    female_report.add_flag(
                        Flag(start, stop, Issue("{word}".format(word=word)))
                    )

        if found:
            female_report.set_summary(
                "Depending on context, these words may be biased towards recruiting women"
            )
        return female_report
