import math

tabDec = open("gielda.txt", "r")
#tabDec = open("testowaTabDec.txt", "r")
tablica = tabDec.read().split()


def podziel_atrybuty(tab: list) -> list:
    """
    :param tab: lista składająca się z wierszy z wczytanych danych (x1, x2, ..., xn)
    :return: lista składająca się z kolumn z wczytanych danych (a1, a2, ..., d)
    """
    lista = []
    znak = ","
    for element in tab:
        lista.append(element.split(znak))

    lista_atrybutow = [[wiersz[i] for wiersz in lista] for i in range(len(lista[0]))]
    return lista_atrybutow


def liczba_wartosci(tab: list) -> dict:
    """
    :param tab: lista składająca się z atrybutów (a1, a2, ..., d)
    :return: słownik składający się z możliwej liczby wartości dla każdego atrybutu
    """
    return {"a"+f"{i+1}" if i < len(tab)-1 else "d": len(set(v)) for i, v in enumerate(tab)}


def liczba_wystapien(tab: list) -> dict:
    """
    :param tab: lista składająca się z atrybutów (a1, a2, ..., d)
    :return: słownik składający się z wystąpień każdej wartości każdego atrybutu
    """
    lista = []
    for idx, element in enumerate(tab):
        elementy = {i: element.count(i) for i in set(element)}
        lista.append(elementy)
    return {"a"+f"{i+1}" if i < len(tab)-1 else "d": lista[i] for i, v in enumerate(tab)}


def podzial(tab: list) -> dict:
    """
    :param tab: lista składająca się z atrybutów (a1, a2, ..., d)
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
    return slownik


def lista_p(x: str, w: dict) -> list:
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


def entropia_decyzyjna(p: list) -> float:
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
    p = lista_p(x, w)
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
        wynik += iloczyn[el]*entropia_decyzyjna(i[el])
    return wynik


def gain(x: str, t: list) -> float:
    wyst = liczba_wystapien(t)
    return entropia_decyzyjna(lista_p("d", wyst)) - info(x, wyst, podzial(t))


def split_info(x: str, t: list) -> float:
    wyst = liczba_wystapien(t)
    p = lista_p(x, wyst)
    return entropia_decyzyjna(p)


def gain_ratio(x: str, t: list):
    return gain(x, t)/split_info(x, t)


atrybuty = podziel_atrybuty(tablica)
wartosci = liczba_wartosci(atrybuty)
wystapienia = liczba_wystapien(atrybuty)
entropia = entropia_decyzyjna(lista_p("d", wystapienia))
obiekty = podzial(atrybuty)

print(f"Lista atrybutów: {atrybuty}")
print(f"Możliwa liczba wartości dla każdego atrybutu: {wartosci}")
print(f"Wystąpienie każdej wartości każdego atrybutu: {wystapienia}")
print(f"Entropia według klas decyzyjnych wynosi: {entropia}")
print(f"Funkcja informacji dla atrybutu a1: {info('a1', wystapienia, obiekty)}")
print(f"Funkcja informacji dla atrybutu a2: {info('a2', wystapienia, obiekty)}")
print(f"Funkcja informacji dla atrybutu a3: {info('a3', wystapienia, obiekty)}")

print(f"Przyrost informacji dla atrybutu a1: {gain('a1', atrybuty)}")
print(f"Przyrost informacji dla atrybutu a2: {gain('a2', atrybuty)}")
print(f"Przyrost informacji dla atrybutu a3: {gain('a3', atrybuty)}")

print(f"Zrównoważony przyrost informacji dla atrybutu a1: {gain_ratio('a1', atrybuty)}")
print(f"Zrównoważony przyrost informacji dla atrybutu a2: {gain_ratio('a2', atrybuty)}")
print(f"Zrównoważony przyrost informacji dla atrybutu a3: {gain_ratio('a3', atrybuty)}")
