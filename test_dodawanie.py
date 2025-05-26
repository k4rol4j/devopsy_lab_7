from calculator import dodawanie

def test_dodawanie():
    assert dodawanie(2, 3) == 5
    assert dodawanie(-1, 1) == 0
