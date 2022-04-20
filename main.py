from moduly import wizualizacja as wiz, obliczenia as obl

#test = {1:{"n":"tak", "m":{2:{"a":"nie", "b":"tak"}}, "o":"nie"}} #testowe dane
test = {1: {'old': 'down', 'mid': {2: {'yes': 'down', 'no': 'up'}}, 'new': 'up'}}

tab = open("gielda.txt", "r")

test1 = obl.oblicz(tab)
print(test)
print(test1)

w = wiz.buduj(test)
wiz.wyswietl_drzewo(w, 0)
