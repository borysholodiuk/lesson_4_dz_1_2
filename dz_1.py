"""
1. Потрібно створити БД з назвою Products з полями Назва товару, ціна товару, кількість товару.
2. Потрібно створити програму, в якій користувач зможе:
	1. Добавляти товари.
	2. Видаляти товари.
	3. Редагувати товар.
	4. Переглядати список товарів.
Це потрібно організувати за допомогою умовних конструкцій (if-else, if-elif-else), де користувач має сам вибрати дію, яку хоче зробити.
"""

import sqlite3

products_table = """CREATE TABLE Products (
          product_name VARCHAR(255),
          product_price FLOAT,
          product_quantity INT
        );"""

# з'єднання з БД
conn = sqlite3.connect('products.db')
cursor=conn.cursor()
print("База данных подключена к SQLite")
cursor.execute(products_table)
print("Таблица SQLite создана")


# функція для додавання товару
def add_product():
    name = input("Введіть назву товару: ")
    price = float(input("Введіть ціну товару: "))
    quantity = int(input("Введіть кількість товару: "))
    cursor.execute("INSERT INTO Products (product_name, product_price, product_quantity) VALUES (?, ?, ?)",
                   (name, price, quantity))
    conn.commit()
    print("Товар успішно доданий")


# функція для видалення товару
def delete_product():
    name = input("Введіть назву товару, який потрібно видалити: ")
    cursor.execute("DELETE FROM Products WHERE product_name = ?", (name,))
    conn.commit()
    print("Товар успішно видалений")


# функція для редагування товару
def edit_product():
    name = input("Введіть назву товару, який потрібно змінити: ")
    new_price = float(input("Введіть нову ціну товару: "))
    new_quantity = int(input("Введіть нову кількість товару: "))
    cursor.execute("UPDATE Products SET product_price = ?, product_quantity = ? WHERE product_name = ?",
                   (new_price, new_quantity, name))
    conn.commit()
    print("Товар успішно змінений")


# функція для перегляду списку товарів
def view_products():
    cursor.execute("SELECT * FROM Products")
    products = cursor.fetchall()
    for product in products:
        print(product)


# основна функція, яка запускає програму
def main():
    while True:
        # вивід меню
        print("Оберіть дію:")
        print("1 - Додати товар")
        print("2 - Видалити товар")
        print("3 - Редагувати товар")
        print("4 - Переглянути список товарів")
        print("0 - Вийти з програми")

        choice = int(input("Ваш вибір: "))

        if choice == 1:
            add_product()
        elif choice == 2:
            delete_product()
        elif choice == 3:
            edit_product()
        elif choice == 4:
            view_products

if __name__ == '__main__':
    main()