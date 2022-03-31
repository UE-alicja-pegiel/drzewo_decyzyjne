import math

tabDec = open("testowaTabDec.txt", "r")
tablica = tabDec.read().split()
print(tablica)


def podziel_atrybuty(tab: list) -> list:
    lista = []
    znak = ","
    for element in tab:
        lista.append(element.split(znak))

    lista_atrybutow = [[wiersz[i] for wiersz in lista] for i in range(len(lista[0]))]
    return lista_atrybutow


def liczba_wartosci(tab: list) -> dict:
    return {"a"+f"{i+1}" if i < len(tab)-1 else "d": len(set(v)) for i, v in enumerate(tab)}


def liczba_wystapien(tab: list) -> dict:
    lista = []
    for idx, element in enumerate(tab):
        elementy = {i: element.count(i) for i in sorted(set(element))}
        lista.append(elementy)
    return {"a"+f"{i+1}" if i < len(tab)-1 else "d": lista[i] for i, v in enumerate(tab)}


def prawdopodobienstwa(d: int, w: dict) -> list:
    p = []
    for i in w:
        p.append(w[i]/d)
    return p


def entropia(p: list) -> float:
    wynik = 0
    for el in p:
        wynik += el*math.log2(el)
    return -1*wynik


def info(atrybut: str, t: int) -> float:
    wynik = 0
    pass


atrybuty = podziel_atrybuty(tablica)
wartosci = liczba_wartosci(atrybuty)
wystapienia = liczba_wystapien(atrybuty)
t = len(atrybuty[-1])
p = prawdopodobienstwa(t, wystapienia["d"])
e = entropia(p)

print(f"Lista atrybutów: {atrybuty}")
print(f"Możliwa liczba wartości dla każdego atrybutu: {wartosci}")
print(f"Wystąpienie każdej wartości każdego atrybutu: {wystapienia}")
print(f"Entropia dla atrybutu decyzyjnego wynosi: {e}")
print(info("a1", t))