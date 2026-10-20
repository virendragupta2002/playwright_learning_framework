import pytest

@pytest.fixture(scope="function")
def setup():
    print("This is pre test setup")

def test_firstPytestProgram(setup):
    print("Hello World!")

def test_secondProgram(preSetupWork):
    print("How are you")