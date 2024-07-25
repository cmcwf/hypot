import pytest
import hypot.source as source

# test sqrt
def test_sqrt_1():
    input = 4
    expected_output = 2.0
    output = source.sqrt(input)
    assert output == expected_output

def test_sqrt_2():
    input = 9
    expected_output = 3.0
    output = source.sqrt(input)
    assert output == expected_output

# test hypot