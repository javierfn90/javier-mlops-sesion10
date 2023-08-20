# IMPORT the `operations` module
from operations import get_fractions

def test_get_fractions():
    # Number as a string
    # "10" = 10
    assert get_fractions("10") == 10


def test_get_fractions_2():
    # Numbers as a string and with / operator
    # "7/4" = 1.75
    assert get_fractions("7/4") == 1.75

def test_get_fractions_3():
    # Negative number as a string
    # "-1" = -1
    assert get_fractions("-1") == -1

# Run the tests
test_get_fractions()
test_get_fractions_2()
test_get_fractions_3()

