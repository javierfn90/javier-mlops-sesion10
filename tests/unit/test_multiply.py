# IMPORT the `operations` module
from operations import multiply

def test_multiply():
    # Negative numbers
    # "-2" * "3" = -6
    assert multiply("-2", "3") == -6


def test_multiply_2():
    # Fractions
    # "1/2" * "8/4" = 1
    assert multiply("1/2", "8/4") == 1


def test_multiply_3():
    # Positive numbers
    # "10" * "5" = 50
    assert multiply("10", "5") == 50

# Run the tests
test_multiply()
test_multiply_2()
test_multiply_3()

