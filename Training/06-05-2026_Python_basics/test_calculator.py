from calculator import add, subtract

def test_add():
    assert add(5,4) == 9

def test_subtract():
    assert subtract(5,4) == 1