from calculating.calc import plus, minus, multiply, divide, dividef, divreminder, degree

def test_plus():
    assert plus(14, 4, 2) == 20
def test_plus():
    assert plus(0, 0) == 0
def test_plus():
    assert plus(124, 3, 2, 7) == 136
def test_plus():
    assert plus(-1, -5, -3) == -9

def test_minus():
    assert minus(15, 7, 6) == 2
def test_minus():
    assert minus(9, 2) == 7
def test_minus():
    assert minus(100, 200, 13) == -113
def test_minus():
    assert minus(-7, -3) == -4

def test_multiply():
    assert multiply(4, 20) == 80
def test_multiply():
    assert multiply(2, 2, 2) == 8
def test_multiply():
    assert multiply(-3, -5) == 15
def test_multiply():
    assert multiply(4, 2, 5, 1) == 40

def test_divide():
    assert divide(25, 5) == 5
def test_divide():
    assert divide(3, 3) == 1
def test_divide():
    assert divide(100, 10, 5) == 2
def test_divide():
    assert divide(300, 30) == 10

def test_dividef():
    assert dividef(27, 5) == 5.4
def test_dividef():
    assert dividef(25, 5) == 5
def test_dividef():
    assert dividef(100, 30) == 3.3
def test_dividef():
    assert dividef(39, 3) == 13

def test_divreminder():
    assert divreminder(27, 5) == 2
def test_divreminder():
    assert divreminder(29, 2) == 1
def test_divreminder():
    assert divreminder(27, 3) == 0
def test_divreminder():
    assert divreminder(56, 6) == 2

def test_degree():
    assert degree(2, 3) == 8
def test_degree():
    assert degree(5, 2) == 25
def test_degree():
    assert degree(3, 3) == 27
def test_degree():
    assert degree(10, 2) == 100
