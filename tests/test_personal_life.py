import unittest

from genderbias import personal_life
from genderbias.document import Document


GOOD_SENTENCE = "NAME is a sensitive and compassionate person."
BAD_SENTENCE = "NAME is a motherly and caring person."


class TestPersonalLife(unittest.TestCase):
    """
    Test genderbias.personal_life
    """

    def test_good_sentence(self):
        """
        Test that the prevalence of family terms is a number,
        and, for a good sentence, is small
        """
        self.assertLessEqual(
            personal_life.personal_life_terms_prevalence(
                Document(GOOD_SENTENCE)
            ),
            0.1
        )

    def test_bad_sentence(self):
        """
        Test that the prevalence of family terms is a number,
        and, for a bad sentence, is large
        """
        self.assertGreaterEqual(
            personal_life.personal_life_terms_prevalence(
                Document(BAD_SENTENCE)
            ),
            0.1
        )
