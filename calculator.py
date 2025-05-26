import numpy as np
import pandas as pd

# Funkcje z numpy
def dodawanie(liczba1, liczba2):
    return np.add(liczba1, liczba2)

def odejmowanie(liczba1, liczba2):
    return np.subtract(liczba1, liczba2)

def mnozenie(liczba1, liczba2):
    return np.multiply(liczba1, liczba2)

def dzielenie(liczba1, liczba2):
    if liczba2 != 0:
        return np.divide(liczba1, liczba2)
    else:
        return "Błąd: dzielenie przez zero!"

# Nowe funkcje z pandas
def average(values):
    return pd.Series(values).mean()

def median(values):
    return pd.Series(values).median()
