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
    :param tab: lista składająca się z atrybutów (a1, a2, ..., d)
    :return: słownik składający się z możliwej liczby wartości dla każdego atrybutu
    """
    return {"a"+f"{i+1}" if i < len(tab)-1 else "d": len(set(v)) for i, v in enumerate(tab)}


def liczba_wartosci_decyzyjnych(tab: dict, x: str) -> dict:
    """
    :param tab: słownik
    :return: słownik składający się z możliwej liczby wartości dla każdego atrybutu
    """
    wynik = {}
    for idx, element in enumerate(tab[x]):
        temp = {f"{el}": tab[x][element] for i, el in enumerate(tab[x][element]) if tab[x][element][el] != 0}
        wynik[element] = len(temp)
    return wynik


def liczba_wystapien(tab: list) -> dict:
    """
    :param tab: lista składająca się z atrybutów (a1, a2, ..., d), gdzie d to atrybut decyzyjny
    :return: słownik składający się z wystąpień każdej wartości każdego atrybutu
    """
    lista = []
    for idx, element in enumerate(tab):
        elementy = {i: element.count(i) for i in set(element)}
        lista.append(elementy)
    return {"a"+f"{i+1}" if i < len(tab)-1 else "d": lista[i] for i, v in enumerate(tab)}


def bez_zer(slownik):
    nowy = {}
    for element in slownik:
        nowy[element] = {i: {j: slownik[element][i][j] for j in slownik[element][i] if slownik[element][i][j] != 0}
                         for i in slownik[element]}
    return nowy


def liczba_wystapien_decyzyjnych(tab: list) -> dict:
    """
    :param tab: lista składająca się z atrybutów (a1, a2, ..., d), gdzie d to atrybut decyzyjny
    :return: słownik wystąpień wartości atrybutów decyzyjnych dla poszczególnych atrybutów
    """
    slownik = {}

    for idx, element in enumerate(tab[:len(tab)-1]):
        elementy = {i: {j: 0 for j in tab[-1]} for i in set(element)}
        slownik["a"+f"{idx+1}"] = elementy

    for d in set(tab[-1]):
        for i, element in enumerate(tab[:len(tab)-1]):
            for idx, el in enumerate(tab[-1]):
                if el == d:
                    slownik["a" + f"{i + 1}"][element[idx]][d] += 1
    return bez_zer(slownik)


def atrybuty_slownik(tab: list) -> dict:
    return {"a"+f"{i+1}" if i < len(tab)-1 else "d": tab[i] for i, v in enumerate(tab)}


def wartosci_prawdopodobienstw(x: str, w: dict) -> list:
    """
    :param x: nazwa atrybutu
    :param w: słownik wystąpień wartości atrybutów
    :return: lista prawdopodobieństw wystąpień wartości danego atrybutu
    """
    p = []
    wystapienia = w[x]
    d = sum(wystapienia.values())
    for idx, klucz in enumerate(wystapienia):
        p.append(wystapienia[klucz]/d)
    return p


def wartosci_prawdopodobienstw_decyzyjne(x: str, w: dict, o: dict) -> dict:
    """
    :param x: nazwa atrybutu
    :param w: słownik wystąpień wartości atrybutów
    :param o: słownik wystąpień wartości atrybutów decyzyjnych dla poszczególnych atrybutów
    :return: słownik prawdopodobieństw wystąpień wartości danego atrybutu
    """
    p = {}
    wystapienia = o[x]
    for element in set(w[x]):
        temp = []
        d = sum(wystapienia[element].values())
        for idx, klucz in enumerate(wystapienia[element]):
            temp.append(wystapienia[element][klucz] / d)
        p[element] = temp
    return p


def entropia(p: list) -> float:
    """
    :param p: lista prawdopodobieństw wystąpień wartości danego atrybutu
    :return: wartość entropii
    """
    wynik = 0
    for el in p:
        if el != 0:
            wynik += el*math.log2(el)
    return -1*wynik


def info(x: str, w: dict, o: dict) -> float:
    """
    :param x: nazwa atrybutu
    :param w: słownik wystąpień wartości atrybutów
    :param o: słownik wystąpień wartości atrybutów decyzyjnych dla poszczególnych atrybutów
    :return: wartość informacji dla danego atrybutu
    """
    p = wartosci_prawdopodobienstw(x, w)
    iloczyn = {element: p[idx] for idx, element in enumerate(set(w[x]))}
    i = {}
    wystapienia = o[x]
    wynik = 0
    for el in set(w[x]):
        temp = []
        d = sum(wystapienia[el].values())
        for idx, klucz in enumerate(wystapienia[el]):
            temp.append(wystapienia[el][klucz] / d)
        i[el] = temp
    for idx, el in enumerate(i.keys()):
        wynik += iloczyn[el]*entropia(i[el])
    return wynik


def gain(x: str, t: list) -> float:
    wyst = liczba_wystapien(t)
    return entropia(wartosci_prawdopodobienstw("d", wyst)) - info(x, wyst, liczba_wystapien_decyzyjnych(t))


def split_info(x: str, t: list) -> float:
    wyst = liczba_wystapien(t)
    p = wartosci_prawdopodobienstw(x, wyst)
    return entropia(p)


def gain_ratio(x: str, t: list):
    return gain(x, t)/split_info(x, t)


def maks_idx(wartosci: dict) -> str:
    maks = 0
    i = 0
    for element in wartosci:
        if wartosci[element] > maks:
            maks = wartosci[element]
            i = element
    return i


def oblicz_wybor(atrybuty, wystapienia):
    przyrosty = {}
    for idx, element in enumerate(wystapienia.keys()):
        if element != 'd':
            przyrosty[element] = gain_ratio(element, atrybuty)
    wybor = maks_idx(przyrosty)
    return wybor


def rek(poziom, wystapienia_decyzyjne, nazwy, idx):
    lw = liczba_wartosci_decyzyjnych(wystapienia_decyzyjne, nazwy[idx])
    return {poziom: {i: list(wystapienia_decyzyjne[nazwy[idx]].get(i).keys())[0]
    if len(list(wystapienia_decyzyjne[nazwy[idx]].get(i).keys())) == 1
    else list(wystapienia_decyzyjne[nazwy[idx]].get(i).keys()) for i in lw}}


def drzewo(plik) -> dict:
    """
    :param plik: plik tekstowy zawierający dane oddzielone przecinkiem
    :return: słownik danych wybranych do zbudowania drzewa
    """
    atrybuty = wczytaj_dane(plik.read().split())
    wystapienia = liczba_wystapien(atrybuty)
    wystapienia_decyzyjne = liczba_wystapien_decyzyjnych(atrybuty)
    wybor = oblicz_wybor(atrybuty, wystapienia)
    liczba = liczba_wartosci(atrybuty)
    nazwy = list(liczba.keys())
    nazwy = nazwy[:len(nazwy)-1]
    idx = nazwy.index(wybor)
    slownik = rek(1, wystapienia_decyzyjne, nazwy, idx)
    return slownik
