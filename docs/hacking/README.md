# Hacking on `genderbias`

If you're reading this page, then welcome to the team!

## Tutorial: Writing a new Detector

In this tutorial, we'll write a new `Detector`. `Detector`s are the tools that this package uses to detect a bias in text.

Let's implement a detector that finds out if the text is calling somebody some type of amphibian. (This is obviously a toy example!)

### Setting up the submodule

First, let's create a new submodule inside the `genderbias` package. In a shell, run:

```
$ cd genderbias/
$ mkdir amphibian
$ touch amphibian/__init__.py
```

If you are unfamiliar with Python submodules and why we use the weird name `__init__.py`, check out [this Python documentation](https://docs.python.org/3/tutorial/modules.html).


### Creating a wordlist

Next, let's construct a word-list of words we want to flag. In a file named `wordlist.txt` in the `amphibian/` directory, write the following, each word on its own line:

```
frog
toad
tadpole
salamander
```

### Creating the detector

In `amphibian/__init__.py`, we'll _inherit_ from the base `Detector` class:

```python
from genderbias.detector import Detector, Flag, Issue


class AmphibianDetector(Detector):

    def get_flags(self, doc: 'Document'):
        pass
```

Let's include the wordlist as a variable named `AMPHIBIAN_WORDS`:

```python
from genderbias.detector import Detector, Flag, Issue

AMPHIBIAN_WORDS = open(_dir + "/wordlist.txt", 'r').readlines()

class AmphibianDetector(Detector):

    def get_flags(self, doc: 'Document'):
        pass
```

### Flagging amphibian-related words

We only have one function to implement: `get_flags`. This function must accept a `Document` and return a list of `Flag`s.

Let's flag any time one of the words from our wordlist comes up:

```python
from genderbias.detector import Detector, Flag, Issue

AMPHIBIAN_WORDS = open(_dir + "/wordlist.txt", 'r').readlines()

class AmphibianDetector(Detector):

    def get_flags(self, doc: 'Document'):
        token_indices = []
        amphibian_flags = []
        words = doc.words()
        offset = 0

        for word in words:
            offset = doc._text.find(word, offset)
            token_indices.append((word, offset, offset + len(word)))
            offset += len(word)

        for word, start, stop in token_indices:
            if word.lower() in AMPHIBIAN_WORDS:
                amphibian_flags.append(
                    Flag(start, stop, Issue(
                        "AmphibianWord",
                        "You shouldn't call someone an amphibian. '{word}' is an amphibian-sounding word.".format(
                            word=word),
                        "Try replacing with phrasing that emphasizes that this person is a human."
                    ))
                )

        return amphibian_flags

```

### Register the `Detector` in the main package

All done! Let's add our `Detector` to the list of detectors in the main module. Open `genderbias/__init__.py` and update `ALL_DETECTORS`:

```python
...
from .personal_life import PersonalLifeDetector
from .amphian import AmphibianDetector                  # ⭐

ALL_DETECTORS = [
    ...
    PersonalLifeDetector,
    AmphibianDetector,                                  # ⭐
]
```

And we're done! Now, when users run `genderbias`, it will detect if they have called someone some sort of amphibian-sounding word:

```shell
$ genderbias --file my-letter.txt
[50-54] AmphibianWord: You shouldn't call someone an amphibian. 'frog' is an amphibian-sounding word. Try replacing with phrasing that emphasizes that this person is a human.
```
