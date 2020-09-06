# Napisz skrypt, który:
# Wczyta z klawiatury imię i wypisze na ekran komunikat "Cześć, <imię>!"
# Jeśli imię będzie miało mniej niż trzy znaki, to poinformuj o tym użytkownika i nie drukuj powitania.

imie = input('Wpisz imię: ')

wiadomosc = f'Cześć {imie.capitalize()}!'

print(wiadomosc)