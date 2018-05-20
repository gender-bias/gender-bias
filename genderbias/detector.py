
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

    def __init__(self, name: str, description: str = "", fix: str = ""):
        """
        Create a new Issue.

        Arguments:
            name (str): The category of the Issue (e.g. 'Personal_Life')
            description (str: ""): A plaintext description of what's wrong with
                this particular passage
            fix (str: ""): An optional recommendation for how to fix the text

        Returns:
            None

        """
        self.name = name
        self.description = description
        self.fix = fix

    def __str__(self):
        """
        Print a stringified version of this Issue.

        Arguments:
            None

        Returns:
            str: The Issue, formatted as: `Name: Description. (Fix)`

        """
        result = self.name
        if self.description:
            result += ": " + self.description
            if self.fix:
                result += " ({})".format(self.fix)
        return result


class Flag:
    """
    A flag is a callout to a particular index in the text. It includes an
    issue (what is wrong with the passage) and start-stop character indices.
    """

    def __init__(self, start: int, stop: int, issue: 'Issue'):
        """
        Create a new Flag.

        Arguments:
            start (int): The start-index of the passage at fault, inclusive
            stop (int): The stop-index of the passage at fault, exclusive
            issue (Issue): The issue to tag on this passage

        Returns:
            None

        """
        self.start = start
        self.stop = stop
        if not isinstance(issue, Issue):
            raise ValueError(
                "Issue must be of type 'genderbias.Issue' but got {}".format(
                    type(issue)
                )
            )
        self.issue = issue

    def __str__(self):
        """
        Stringify the Flag.

        Arguments:
            None

        Returns:
            str: Of the form `[start-stop]: str(Issue)`

        """
        return "[{start}-{stop}]: {msg}".format(
            start=self.start,
            stop=self.stop,
            msg=str(self.issue)
        )


class Detector:
    """
    Abstract class for a detector. Implement this to use.
    For an example implementation tutorial, look at `docs/hacking.md`.
    """

    def __init__(self):
        pass

    @abstractmethod
    def get_flags(self, doc: 'Document'):
        """
        Returns a list of flags for a document.
        """
        raise NotImplementedError()

