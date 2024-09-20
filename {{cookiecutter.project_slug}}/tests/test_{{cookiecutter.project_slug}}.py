import pytest

@pytest.fixture
def world():
    return "World"

def test_trivial_hello_world(world):
    assert "Hello" + world == "Hello World"