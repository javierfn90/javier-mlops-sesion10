# IMPORT the `operations` module
from operations import substract

def test_substract():
    # Float numbers
    # "0.5" - "0.5" = 0
    assert substract("0.5", "0.5") == 0


def test_substract_2():
    # Fraction numbers
    # "1/2" - "1" = -0.5
    assert substract("1/2", "1") == -0.5


def test_substract_3():
    # Result negative
    # "10" - "5" = 5
    assert substract("10", "5") == 5

# Run the tests
test_substract()
test_substract_2()
test_substract_3()
