# Napisz skrypt, który:
# Wczyta z klawiatury imię i wypisze na ekran komunikat "Cześć, <imię>!"
# Jeśli imię będzie miało mniej niż trzy znaki, to poinformuj o tym użytkownika i nie drukuj powitania.
# użyj funkcji wbudowanej len()

imie = input('Wpisz imię: ')

if len(imie) > 2:
    wiadomosc = f'Cześć {imie.capitalize()}!'
else:
    wiadomosc = 'Wprowadzone imię ma mniej niż trzy znaki'

print(wiadomosc)
