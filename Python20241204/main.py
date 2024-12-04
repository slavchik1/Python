import sys


class Product:
    count = 0 # Лічильник створених об'єктів
    def __new__(cls, *args, **kwargs):
        cls.count += 1
        return super().new(cls)

    def __init__(self, name, price, quantity):
         self.name = name
         self.price = price
         self.quantity = quantity
         self.id = Product.count # Унікальний ідентифікатор товару


    def __del__(self):
        print(f"Товар '{self.name}' видалено.")


    def __str__(self):
        return f"ID: {self.id}, Назва: {self.name}, Ціна: {self.price}, Кількість: {self.quantity}"

class Inventory:
    def __init__(self):
        self.products = []


    def add_product(self):
        name = input("Введіть назву товару: ")
        try:
            price = float(input("Введіть ціну товару: "))
            quantity = int(input("Введіть кількість товару: "))
        except ValueError:
            print("Невірний формат даних! Спробуйте ще раз.")
            return
        product = Product(name, price, quantity)
        self.products.append(product)
        print(f"Товар '{name}' успішно додано до списку.")

    def remove_product(self):
        try:
            product_id = int(input("Введіть ID товару для видалення"))
        except ValueError:
            print("Невірний ID. Введіть число.")
            return
        for product in self.products:
            if product.id == product_id:
                self.products.remove(product)
                del product
                print(f"Товар з ID {product_id} успішно видалено")
                return
            print("Товар не знайдено.")

    def show_inventory(self):
        if not self.products:
            print("Інвентар порожній.")
            return
        print("Список товарів:")
        for product in self.products:
            print(product)


def main():
    inventory = Inventory()
    while True:
        print("\nОберіть дію:")
        print("1. Додати товар")
        print("2. Видалити товар")
        print("3. Переглянути список товарів")
        print("4. Вийти")

    choice = input("Ваш вибір: ")
    if choice == '1':
        inventory.add_product()
    elif choice == '2':
        inventory.remove_product()
    elif choice == '3':
        inventory.show_inventory()
    elif choice == '4':
        print("Роботу завершено.")
        sys.exit()
    else:
        print("Невірний вибір. Спробуйте ще раз.")

main()
