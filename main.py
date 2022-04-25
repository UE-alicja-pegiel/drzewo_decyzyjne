from moduly import wizualizacja as wiz, obliczenia as obl

#test = {1:{"n":"tak", "m":{2:{"a":"nie", "b":"tak"}}, "o":"nie"}} #testowe dane
test = {1: {'old': 'down', 'mid': {2: {'yes': 'down', 'no': 'up'}}, 'new': 'up'}}

tab = open("gielda.txt", "r")

print("\nNiestety nie zdążyłam zrobić poprawnego drzewa. \nWszystkie obliczenia znajdują się w pliku 'proby.py' i "
      "tam testowałam wartości, które wychodzą dobrze. \nNiestety nie będę miała dostępu do komputera"
      "w czasie 27.04-09.05.2022, dlatego muszę wysłać projekt w obecnym stanie. \n"
      "Spodobała mi się praca nad drzewem, więc na pewno spróbuję go później jeszcze naprawić :)\n")

test1 = obl.drzewo(tab)
print(test1)

w = wiz.buduj(test1)
wiz.wyswietl_drzewo(w, 0)
