import pytest

from genderbias.detector import Flag, Issue

def test_flag_requires_issue():
    with pytest.raises(ValueError):
        f = Flag(100, 200, "Invalid issue")


def test_flag_stringify():
    f1 = Flag(100, 200, Issue("Issue", "Description.", fix="Fix Me!"))
    assert(
        str(f1) == "[100-200]: Issue: Description. (Fix Me!)"
    )

    f2 = Flag(100, 200, Issue("Issue", "Description."))
    assert(
        str(f2) == "[100-200]: Issue: Description."
    )

    f3 = Flag(100, 200, Issue("Issue"))
    assert(
        str(f3) == "[100-200]: Issue"
    )
