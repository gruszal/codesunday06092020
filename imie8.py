# Bazując na skrypcie imie7.py sprawdź, czy imie już znajduje się na liście.
# Jeśli tak, nie dodawaj do i poinformuj o tym użytkownika

grupa = ['Zuzanna', 'Celina', 'Krzysztof']

imie = input('Wpisz imię: ')

if imie in grupa:
    print(f'"{imie}" już jest na liście')
else:
    grupa.append(imie)

print(grupa)

