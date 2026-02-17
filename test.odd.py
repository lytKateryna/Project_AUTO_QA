import pytest

@pytest.fixture
def EvenOddChecker():
    return EvenOddChecker()


def test_sum_positive_numbers(EvenOddChecker):
    assert EvenOddChecker.is_even(2) is True
    assert EvenOddChecker.is_even(3) is False
    assert EvenOddChecker.is_even(-2) is False