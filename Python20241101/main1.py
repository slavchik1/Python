class Goods:
    def __init__(self, name, type, weight, price):
        self.name = name
        self.type = type
        self.weight = weight
        self.price = price

goods = Goods("Яблуко", "Фрукт", 0.5, 35)

setattr(goods, "description", "Яблуко (англ. Apple) — це їжа, що випадає з дубового і темно дубового листя.")

goods.price = 2048

print(getattr(goods, "description"))

delattr(goods, "name")
