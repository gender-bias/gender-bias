"""
Tools for identifying mention of publications.
"""
from typing import List, Dict

import re

from genderbias.document import Document
from genderbias.detector import Detector, Report, Flag, Issue


def identify_publications(doc: Document) -> Dict[str, float]:
    """
    Determine entities with high probability of being a publication name.

    Arguments:
        doc (Document): The document to search

    Returns:
        Dict[str, float]: A list of publication names and the probability
            that we believe that we've made a correct assessment. For example,
            {"My Paper Title": 1.0} means that we are 100% sure that this is
            a reference to a publication.
    """
    _DOC_ID_MARKERS = [
        "arxiv:",
        "doi:",
    ]

    _AUTHORSHIP_MARKERS = [
        "et al",
    ]
    potential_publications = {}
    # First, do the very easy thing: Let's look for callouts to arXiv# or DOIs.
    # TODO
    pass

    # Next, look for common markers of authorship, such as "et al".
    # TODO
    pass

    # Anything in quotes get a low probability:
    # TODO: Smart quotes and single quotes
    rxp = re.compile('"[^"]+"')
    for match in re.findall(rxp, doc._text):
        if match not in potential_publications:
            potential_publications[match] = 0.0
        potential_publications[match] += 0.25

    return potential_publications


class PublicationDetector(Detector):
    """
    Detect mention of publications in a document.

    This detector flags documents globally.

    Parameters:
        min_publications (float): The minimum number of publications that must
            be present before the detector will flag a document. This is the
            sum of probabilities of all documents, so if this is set to 0.5,
            two documents each with a probability of 0.25, or ten documents
            with P=0.05, are equally valid.

    """

    def __init__(self, **kwargs) -> None:
        """
        Create a new PubliationDetector.

        Arguments:
            min_publications (float: 0.5): The minimum probability-sum
                of publications required in a document before the detector
                should flag the document. For more information, see the docs
                for PublicationDetector.

        Returns:
            None

        """
        super().__init__()
        self.min_publications = kwargs.get("min_publications", 0.5)

    def get_summary(self, doc: "Document") -> str:
        """
        Returns a string representing summary feedback on publications.
        This will indicate if not enough publications were found.
        Otherwise it will be empty.
        """
        # Sum up all of the probabilities of all publications. This is a bit
        # janky, but it acts as a proxy for the total number of publications
        # mentioned. For example, if there are two potential publications each
        # with a probability of 50%, then we could consider that a mention of
        # one single publication.
        summary = ""
        pub_count = sum(identify_publications(doc).values())
        if pub_count < self.min_publications:
            summary =   "This document does not mention many publications. " + \
                        "Try referencing more concrete publications or work " + \
                        "byproducts, if possible."
        return summary
    
    def get_flags(self, doc: "Document") -> List["Flag"]:
        """
        Flag a document (globally) if we cannot find any research products.

        Returns only a single flag if no publications/resources are mentioned.
        """
        all_flags = []
        # TODO: Any other flags needed here?

        # Sum up all of the probabilities of all publications. This is a bit
        # janky, but it acts as a proxy for the total number of publications
        # mentioned. For example, if there are two potential publications each
        # with a probability of 50%, then we could consider that a mention of
        # one single publication.
        pub_count = sum(identify_publications(doc).values())
        if pub_count < self.min_publications:
            all_flags.append(
                Flag(
                    0,
                    0,
                    Issue(
                        "Publications",
                        "This document does not mention many publications.",
                        "Try referencing more concrete publications or work "
                        "byproducts, if possible.",
                    ),
                )
            )
        return all_flags

    def get_report(self, doc):
        """
        Generate a report on the text based upon mentions of publications.

        Arguments:
            doc (Document): The document to check

        Returns:
            Report

        """
        report = Report("Publications")
        report.set_summary(self.get_summary(doc))
        
        for flag in self.get_flags(doc):
            report.add_flag(flag)
        return report
