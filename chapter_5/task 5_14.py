# Вправа по програмуванню 5-14
# Кінетична енергія


# Головна функція.
def main():
    # Отримання маси об'єкта.
    mass = float(input("Маса об'єкта в кілограмах: "))

    # Отримання швидкості об'єкта.
    velocity = float(input("Швидкість об'єкта в метрах за секунду: "))

    # Розрахунок кінетичної енергії об'єкта.
    kinet_energy = kinetic_energy(mass, velocity)

    # Виводимо на екран результати розрахунків.
    print(f"\nКінетична енергія тіла рівна {kinet_energy:.2f} джоулям.")


# Функція розраховує і повертає величину кінетичної енергії.
def kinetic_energy(mass, velocity):
    kinet_energy = 0.5 * mass * velocity ** 2
    return kinet_energy


# Виклик головної функції.
main()
