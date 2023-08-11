import pytest

"""
Assertions:
Use powerful assertions to validate different conditions.
"""
def test_assertions():
    assert 10 > 5
    assert "pytest" in "powerful testing framework"
    assert [1, 2, 3] == [1, 2, 3]


"""
Fixture and Setup/Teardown:
Fixtures help in setting up and cleaning up resources required for testing
"""
@pytest.fixture
def setup_teardown_example():
    print("Setup")
    yield # Here test function will run
    print("Teardown")

@pytest.fixture
def database_connection():
    # Set up a temporary database connection
    print("Creating Database Connection")
    yield 
    # Tear down the database connection
    print("Closing Database connection object")

# Pass the pytest.fixture method if you want to run it before and after
def test_fixture_example1(setup_teardown_example):
    print("Running test")

def test_fixture_example2(database_connection):
    print("Running test")


"""
Skipping Tests:
You can use @pytest.mark.skip decorator to skip specific tests
"""
@pytest.mark.skip(reason="Example of a skipped test")
def test_skipped_example():
    assert 1 + 1 == 3
  

"""
Marking Tests:
Use custom markers to categorize tests and run specific groups of tests.
"""
@pytest.mark.smoke
def test_smoke_example():
    assert True

@pytest.mark.regression
def test_regression_example():
    assert False



"""
Exception Testing:
You can test if a specific exception is raised using pytest.raises.
"""
def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y

def test_exception_example():
    with pytest.raises(ValueError):
        divide(10, 0)


"""
Parametrized Testing:
Parametrized tests allow you to test a function with different input values. 
pytest.mark.parametrize decorator makes this easy.
"""
def multiply(x, y):
    return x * y

@pytest.mark.parametrize("x, y, expected", [
    (2, 3, 6),
    (0, 5, 0),
    (-4, 4, -16),
])
def test_multiplication(x, y, expected):
    assert multiply(x, y) == expected




