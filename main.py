class Wezel:
    potomkowie = None
    atrybut = None
    wartosc = None
    klasa = None


def wyswietl_drzewo(drzewo, przesuniecie):
    if drzewo.atrybut is not None:
        print(" "*przesuniecie, end="")
        if drzewo.wartosc:
            print(drzewo.wartosc, end=" -> ")
        print("Atrybut", drzewo.atrybut)
        for p in drzewo.potomkowie:
            wyswietl_drzewo(p, przesuniecie + 4)
    else:
        print(" "*przesuniecie, end="")
        print(drzewo.wartosc, "->", drzewo.klasa)


def buduj(test):
    w = Wezel()
    w.potomkowie = []
    klucz, element = test.popitem()
    w.atrybut = klucz
    for t in element:
        if isinstance(element[t], dict):
            nowy_wezel = buduj(element[t])
            nowy_wezel.wartosc = t
            w.potomkowie.append(nowy_wezel)
        else:
            nowy_wezel = Wezel()
            nowy_wezel.wartosc = t
            nowy_wezel.klasa = element[t]
            w.potomkowie.append(nowy_wezel)
    return w

test = {1:{"n":"tak", "m":{2:{"a":"nie", "b":"tak"}}, "o":"nie"}} #testowe dane
test = {1: {'old': 'down', 'mid': {2: {'yes': 'down', 'no': 'up'}}, 'new': 'up'}}

w = buduj(test)
wyswietl_drzewo(w, 0)