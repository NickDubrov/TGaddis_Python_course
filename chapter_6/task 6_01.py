# Вправа по програмуванню 6-1
# Виведення файлу на екран


# Головна функція.
def main():
    # Відкриття файлу для читання.
    infile = open(
        r"E:\Python\TGaddis_Python_course\chapter_6\data\numbers.txt")

    # Читання файлу та збереження його вмісту в змінній.
    contents = infile.read()

    # Виводимо на екран вміст файлу.
    print(contents)

    # Закриття файлу.
    infile.close()


# Виклик головної функції.
main()
