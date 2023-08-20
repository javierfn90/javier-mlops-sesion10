# IMPORT the `operations` module
from operations import divide

def test_divide():
    # Fraction
    # 10/2 = 5
    assert divide(10, 2) == 5


def test_divide_2():
    # Strings and divisions
    # "-15/4" / "1/2" =  -7.5 
    assert divide("-15/4", "1/2") == -7.5


def test_divide_3():
    # Numbers as strings
    # "8"/"16" = 0.5
    assert divide("8", "16") == 0.5

# Run the tests
test_divide()
test_divide_2()
test_divide_3()
