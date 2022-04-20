import math


def wczytaj_dane(tablica: list) -> list:
    """
    :param tablica: lista składająca się z wierszy z danych z pliku tekstowego (x1, x2, ..., xn)
    :return: lista składająca się z kolumn z wczytanych danych (a1, a2, ..., d)
    """
    lista = []
    znak = ","
    for element in tablica:
        lista.append(element.split(znak))

    atrybuty = [[wiersz[i] for wiersz in lista] for i in range(len(lista[0]))]
    return atrybuty


def liczba_wartosci(tab: list) -> dict:
    """
    :param tab: lista składająca się z atrybutów (a1, a2, ..., d), gdzie d to atrybut decyzyjny
    :return: słownik składający się z możliwej liczby wartości dla każdego atrybutu
    """
    return {"a"+f"{i+1}" if i < len(tab)-1 else "d": len(set(v)) for i, v in enumerate(tab)}


def oblicz(plik) -> dict:
    """
    :param plik: plik tekstowy zawierający dane oddzielone przecinkiem
    :return: słownik danych wybranych do zbudowania drzewa
    """
    atrybuty = wczytaj_dane(plik.read().split())
    wartosci = liczba_wartosci(atrybuty)
    print(wartosci)
    slownik = {}
    return slownik
