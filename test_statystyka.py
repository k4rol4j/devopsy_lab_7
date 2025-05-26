from calculator import average, median

def test_average():
    assert average([1, 2, 3, 4]) == 2.5

def test_median():
    assert median([3, 1, 2]) == 2
