# Jak uniezależnić się od wielkości liter??

grupa = ['zuzanna', 'celina', 'krzysztof']

imie = input('Wpisz imię: ')

if imie.lower() in grupa:  # .lower() zamienia wszystkie litery w stringu na małe
    print(f'"{imie}" już jest na liście')
else:
    grupa.append(imie)

print(grupa)

