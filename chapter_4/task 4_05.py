# Вправа по програмуванню 4-5
# Середня кількість дощових опадів

# Ініціалізація накопичувальної змінної.
total = 0

# Отримання кількості років для збору даних.
years = int(input("Кількість років: "))

# Отримання кількості щомісячних опадів.
for year in range(years):
    print(f"\nРік - {year}:")
    for month in range(12):
        print(f"Кількість опадів за {month + 1}-ий місяць: ", end="")
        rainfall = int(input())
        total += rainfall

# Розрахунок кількості місяців в періоді.
months = years * 12

# Розрахунок середньої кількості опадів на місяць.
average = total / months

# Виводимо результати на екран.
print(f"\nКількість місяців в періоді: {months}")
print(f"Кількість опадів за весь період: {total:.2f} мм")
print(f"Середня кількість опадів на місяць: {average:.2f} мм")