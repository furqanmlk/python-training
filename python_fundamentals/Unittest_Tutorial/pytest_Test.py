import pytest

@pytest.fixture
def setup_teardown_example():
    print("Setup")
    yield
    print("Teardown")

def test_fixture_example(setup_teardown_example):
    print("Running test")


@pytest.mark.skip(reason="Example of a skipped test")
def test_skipped_example():
    assert 1 + 1 == 3
  

@pytest.mark.smoke
def test_smoke_example():
    assert True

@pytest.mark.regression
def test_regression_example():
    assert False

def test_assertions():
    assert 10 > 5
    assert "pytest" in "powerful testing framework"
    assert [1, 2, 3] == [1, 2, 3]

"""
 Parametrized Testing:
 Parametrized tests allow you to test a function with different input values. 
 pytest.mark.parametrize decorator makes this easy.
"""
def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y

def test_exception_example():
    with pytest.raises(ValueError):
        divide(10, 0)

def multiply(x, y):
    return x * y

@pytest.mark.parametrize("x, y, expected", [
    (2, 3, 6),
    (0, 5, 0),
    (-4, 4, -16),
])
def test_multiplication(x, y, expected):
    assert multiply(x, y) == expected




