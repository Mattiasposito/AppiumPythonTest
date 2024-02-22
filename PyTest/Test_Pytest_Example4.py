import pytest

@pytest.yield_fixture(scope="module")
def beforeClass():
    print("Before a class")
    yield
    print("After class")

@pytest.yield_fixture()
def setUp():
    print("Before a method")
    yield
    print("After Method")

def test_methodA(beforeClass,setUp):
    print("This is method A")

def test_methodB(beforeClass,setUp):
    print("This is method B")