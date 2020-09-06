liczba = 15
# liczba = 50

# UWAGA, TO DZIALA ŹLE

if liczba % 3 == 0:
    print(f'Liczba {liczba} jest podzielna przez 3')
elif liczba % 5 == 0:
    print(f'Liczba {liczba} jest podzielna przez 5')  # to się nie wydrukuje dla liczby 15

print('Koniec programu')