class ShoppingCart:
    def __init__(self):
        self.items = []
    def add_item(self, item):
        self.items.append(item)
    def remove_item(self, item):
        def foundByName(list, name):
            for i in range(len(list)):
                if list[i] == name:
                    return i
            return "Не знайдено жодного елементу"

        self.items.pop(foundByName(self.items, item))
    def show_items(self):
        print(self.items)

cart = ShoppingCart()
cart.add_item("Apple")
cart.add_item("Banana")
cart.remove_item("Apple")
cart.show_items()