from calculator import dzielenie

def test_dzielenie():
    assert dzielenie(6, 3) == 2
    assert dzielenie(1, -1) == -1
    assert dzielenie(1, 0) == "Błąd: dzielenie przez zero!"
