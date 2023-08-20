# IMPORT the `operations` module
from operations import sum

def test_sum():
    # Floats
    # "0.5" + "0.5" = 1
    assert sum("0.5", "0.5") == 1

def test_sum_2():
    # Negative numbers
    # "-3" + "-3" = -6
    assert sum("-3", "-3") == -6

def test_sum_3():
    # Positive numbers
    # "4" + "6" = 10
    assert sum("4", "6") == 10

# Run the tests
test_sum()
test_sum_2()
test_sum_3()
