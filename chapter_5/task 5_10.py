# Вправа по програмуванню 5-10
# Конвертер футів в дюйми


# Головна функція.
def main():
    # Отримання кількості футів.
    feet = float(input("Кількість футів: "))

    # Розрахунок кількості дюймів.
    inches = feet_to_inches(feet)

    # Виводимо на екран результати розрахунків.
    print(f"{feet:.1f} футів дорівнює {inches:.1f} дюймам.")


# Функція розраховує і повертає кількість дюймів.
def feet_to_inches(feet):
    return feet * 12


# Виклик головної функції.
main()