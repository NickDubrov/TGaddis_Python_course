# Вправа по програмуванню 4-6
# Таблиця відповідності між градусами Цельсія та градусами Фаренгейта

# Розраховуємо і виводимо результати на екран.
print("Цельсій\t\tФаренгейт")
print("-------------------------")

for celsius in range(21):
    fahrenheit = ((9 * celsius) / 5) + 32
    print(celsius, '\t\t', fahrenheit)
