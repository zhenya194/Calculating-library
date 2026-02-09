from calculating.calc import plus, minus, multiply, divide, dividef, divreminder, degree

def test_plus():
    assert plus(14, 4, 2) == 19

def test_minus():
    assert minus(15, 7, 6) == 2

def test_multiply():
    assert multiply(4, 20) == 80

def test_divide():
    assert divide(25, 5) == 5

def test_dividef():
    assert dividef(27, 5) == 5.4

def test_divreminder():
    assert divreminder(27, 5) == 2

def test_degree():
    assert degree(2, 3) == 8
