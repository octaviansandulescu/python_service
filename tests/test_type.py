from src.test import add


def test_add():
    assert add(5, 10) == 15
    assert add("cat", "dog") == "catdog"
