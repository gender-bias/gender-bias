import os
import re

from ..detector import Detector, Flag, Issue, Report

_dir = os.path.dirname(__file__)
MALE_WORDS = [
    word.strip() for word in open(_dir + "/Malewords.wordlist", "r").readlines()
]


class MaleDetector(Detector):
    """
    Detect words that are more commonly used to recruit men rather than women.

    """

    def get_report(self, doc):
        male_report = Report("Terms biased towards men:")
        words_with_indices = doc.words_with_indices()
        # print(words_with_indices)

        found = False
        for word, start, stop in words_with_indices:
            word = word.lower()
            for maleword in MALE_WORDS:
                searchTerm = "^" + maleword + ".."
                x = re.search(searchTerm, word)
                if x:
                    # print(x.span(), x.string, x.group())
                    found = True
                    male_report.add_flag(
                        Flag(start, stop, Issue("{word}".format(word=word)))
                    )
        if found:
            male_report.set_summary(
                "Depending on context, these words may be biased towards recruiting men"
            )
        return male_report
