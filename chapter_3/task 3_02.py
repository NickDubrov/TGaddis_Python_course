# Вправа по програмуванню 3-2
# Площі прямокутників

# Отримання довжини і ширини 1-го прямокутника.
lenght1 = float(input("Довжина 1-го прямокутника: "))
width1 = float(input("Ширина 1-го прямокутника: "))

# Отримання довжини і ширини 2-го прямокутника.
lenght2 = float(input("Довжина 2-го прямокутника: "))
width2 = float(input("Ширина 2-го прямокутника: "))

# Розрахунок площі 1-го прямокутника.
area1 = lenght1 * width1

# Розрахунок площі 2-го прямокутника.
area2 = lenght2 * width2

# Виводимо результати розрахунків на екран.
print(f"\nПлоща 1-го прямокутника: {area1:.2f}")
print(f"Площа 2-го прямокутника: {area2:.2f}")

if area1 > area2:
    print("Площа 1-го прямокутника більше площі 2-го прямокутника.")
elif area1 < area2:
    print("Площа 2-го прямокутника більше площі 1-го прямокутника.")
else:
    print("Площі прямокутників рівні.")
