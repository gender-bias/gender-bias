
from .document import Document

from .personal_life import PersonalLifeDetector
from .effort import EffortDetector

ALL_DETECTORS = [
    PersonalLifeDetector,
    EffortDetector
]
