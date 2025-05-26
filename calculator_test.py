from calculator import dodawanie,dzielenie,mnozenie,odejmowanie
def test_dodawanie():
    assert dodawanie(2, 3) == 5
    assert dodawanie(-1, 1) == 0

def test_odejmowanie():
    assert odejmowanie(5, 3) == 2
    assert odejmowanie(1, -1) == 2

def test_mnozenie():
    assert mnozenie(2, 3) == 6
    assert mnozenie(-1, 1) == -1

def test_dzielenie():
    assert dzielenie(6, 3) == 2
    assert dzielenie(1, -1) == -1
    assert dzielenie(1, 0) == "Błąd: dzielenie przez zero!"