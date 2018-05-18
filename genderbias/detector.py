
from abc import abstractmethod

class Issue:
    """
    An Issue is a call-out to a specific failure of a text.

    Think of an Issue as a red squiggly, and optionally, a list of
    autocorrect suggestions. For example,

        Issue(
            "Personal Life",
            "Words that reference a person's personal life",
            fix="Reference professional merits instead.
        )

    """

    def __init__(self, name, description="", fix=""):
        self.name = name
        self.description = description
        self.fix = fix

    def __str__(self):
        result = self.name
        if self.description:
            result += ": " + self.description
            if self.fix:
                result += " ({})".format(self.fix)
        return result


class Flag:

    def __init__(self, start: int, stop: int, issue: 'Issue'):
        self.start = start
        self.stop = stop
        if not isinstance(issue, Issue):
            raise ValueError("Issue must be of type 'genderbias.Issue' but got {}".format(type(issue)))
        self.issue = issue

    def __str__(self):
        return "[{start}-{stop}]: {msg}".format(
            start=self.start,
            stop=self.stop,
            msg=str(self.issue)
        )


class Detector:

    def __init__(self):
        pass

    @abstractmethod
    def get_flags(self, doc: 'Document'):
        """
        Returns a list of flags for a document.
        """
        raise NotImplementedError()

