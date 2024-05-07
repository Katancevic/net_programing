def func(x):
    return x +1

def test_answer():
    assert func(3) == 5

# mozemo i ovako napisati sa dodavanjem poruke

def func(x):
    return x + 1

def test_answer():
    assert func(3) == 5, "value lower then expected, check input value"