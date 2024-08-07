# Вправа по програмуванню 5-2
# Модернізація програми розрахунку податку з продажу

# Іменовані константи.
FED_TAX_RATE = 0.05
REG_TAX_RATE = 0.025


# Головна функція.
def main():
    # Отримання суми покупки.
    purchase_amount = float(input("Введіть суму покупки: "))

    # Розрахунок федерального податку.
    fed_tax = calculate_federal_tax(purchase_amount)

    # Розрахунок регіонального податку.
    reg_tax = calculate_regional_tax(purchase_amount)

    # Розрахунок загальної суми продажу.
    total_amount = calculate_total_amount(purchase_amount, fed_tax, reg_tax)

    # Виводимо на екран результати розрахунків.
    print(f"\nСума покупки: {purchase_amount:,.2f}")
    print(f"Федеральний податок: {fed_tax:,.2f}")
    print(f"Регіональний податок: {reg_tax:,.2f}")
    print(f"Загальна сума продажу: {total_amount:,.2f}")


# Функція розраховує і повертає федеральний податок.
def calculate_federal_tax(purchase_amount):
    return purchase_amount * FED_TAX_RATE


# Функція розраховує і повертає регіональний податок.
def calculate_regional_tax(purchase_amount):
    return purchase_amount * REG_TAX_RATE


# Функція розраховує і повертає загальну суму продажу.
def calculate_total_amount(purchase_amount, federal_tax, regional_tax):
    return purchase_amount + federal_tax + regional_tax


# Виклик головної функції.
main()
